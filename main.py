from agents import researcher, writer, editor
from tasks import research_task_description, writing_task_description, editing_task_description
import os
import json
import logging
from dotenv import load_dotenv

# -------------------------
# Setup logging
# -------------------------
logging.basicConfig(
    filename="workflow.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# -------------------------
# Load environment variables
# -------------------------
load_dotenv()


def validate_input(task_description: str, field_name: str) -> None:
    """
    Validate that task descriptions are not empty.
    """
    if not task_description or not isinstance(task_description, str):
        raise ValueError(f"❌ Invalid {field_name}: Task description must be a non-empty string")


def validate_json_structure(data: str, field_name: str) -> None:
    """
    Validate JSON response structure before processing.
    Ensures that it is valid JSON and has expected structure.
    """
    try:
        parsed = json.loads(data)
        if not isinstance(parsed, dict):
            raise ValueError(f"❌ {field_name} must return a JSON object, got {type(parsed)}")
    except json.JSONDecodeError:
        raise ValueError(f"❌ {field_name} returned invalid JSON")


def run_research() -> str:
    """
    Executes the Researcher agent.
    """
    logging.info("Running research task...")
    validate_input(research_task_description, "Research Task")
    research_result = researcher.execute_task(research_task_description)

    # Optional: Validate JSON if your researcher returns JSON
    # validate_json_structure(research_result, "Research Result")

    return research_result


def run_writing(research_result: str) -> str:
    """
    Executes the Writer agent.
    """
    logging.info("Running writing task...")
    validate_input(writing_task_description, "Writing Task")
    article_result = writer.execute_task(writing_task_description, research_result)
    return article_result


def run_editing(article_result: str) -> str:
    """
    Executes the Editor agent.
    """
    logging.info("Running editing task...")
    validate_input(editing_task_description, "Editing Task")
    final_result = editor.execute_task(editing_task_description, article_result)
    return final_result


def save_output(research: str, draft: str, final: str) -> None:
    """
    Save workflow outputs to a file.
    """
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("RESEARCH FINDINGS:\n")
        f.write("=" * 50 + "\n")
        f.write(research)
        f.write("\n\n" + "=" * 50 + "\n")
        f.write("DRAFT ARTICLE:\n")
        f.write("=" * 50 + "\n")
        f.write(draft)
        f.write("\n\n" + "=" * 50 + "\n")
        f.write("FINAL ARTICLE:\n")
        f.write("=" * 50 + "\n")
        f.write(final)


def main():
    """
    Main function to run the simple agent workflow with Google Gemini.
    """

    try:
        # Security: Check if API key is set
        if not os.getenv("GOOGLE_API_KEY"):
            raise EnvironmentError("❌ GOOGLE_API_KEY not found in environment variables. "
                                   "Please set it in a .env file")

        print("🚀 Starting Simple Agent Workflow with Google Gemini...")
        print("=" * 60)

        # Step 1: Research
        print("🔍 Step 1: Research Analyst is gathering information...")
        research_result = run_research()
        print("✅ Research completed!")
        print(f"Research Summary: {research_result[:200]}...")
        print("=" * 60)

        # Step 2: Writing
        print("✍️  Step 2: Content Writer is creating the article...")
        article_result = run_writing(research_result)
        print("✅ Article written!")
        print(f"Article Preview: {article_result[:200]}...")
        print("=" * 60)

        # Step 3: Editing
        print("📝 Step 3: Content Editor is reviewing and polishing...")
        final_result = run_editing(article_result)
        print("✅ Editing completed!")
        print("=" * 60)

        # Display final result
        print("📄 FINAL ARTICLE:")
        print("=" * 60)
        print(final_result)
        print("=" * 60)

        # Save results
        save_output(research_result, article_result, final_result)
        print("\n💾 All outputs saved to 'output.txt'")
        print("🎉 Workflow completed successfully!")

    except Exception as e:
        logging.error("Workflow failed", exc_info=True)
        print(f"❌ Error during workflow execution: {str(e)}")
        print("Please check your API key, internet connection, or task inputs.")


if __name__ == "__main__":
    main()
