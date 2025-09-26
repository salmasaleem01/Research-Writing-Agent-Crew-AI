from agents import researcher, writer, editor
from tasks import research_task_description, writing_task_description, editing_task_description
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    """
    Main function to run the simple agent workflow with Google Gemini
    """
    
    # Check if API key is set
    if not os.getenv("GOOGLE_API_KEY"):
        print("❌ Error: GOOGLE_API_KEY not found in environment variables")
        print("Please set your Google API key in a .env file")
        print("Example: GOOGLE_API_KEY=your_api_key_here")
        return
    
    print("🚀 Starting Simple Agent Workflow with Google Gemini...")
    print("=" * 60)
    
    try:
        # Step 1: Research
        print("🔍 Step 1: Research Analyst is gathering information...")
        print("-" * 40)
        research_result = researcher.execute_task(research_task_description)
        print("✅ Research completed!")
        print(f"Research Summary: {research_result[:200]}...")
        print("\n" + "=" * 60)
        
        # Step 2: Writing
        print("✍️  Step 2: Content Writer is creating the article...")
        print("-" * 40)
        article_result = writer.execute_task(writing_task_description, research_result)
        print("✅ Article written!")
        print(f"Article Preview: {article_result[:200]}...")
        print("\n" + "=" * 60)
        
        # Step 3: Editing
        print("📝 Step 3: Content Editor is reviewing and polishing...")
        print("-" * 40)
        final_result = editor.execute_task(editing_task_description, article_result)
        print("✅ Editing completed!")
        print("\n" + "=" * 60)
        
        # Display final result
        print("📄 FINAL ARTICLE:")
        print("=" * 60)
        print(final_result)
        print("=" * 60)
        
        # Save result to file
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write("RESEARCH FINDINGS:\n")
            f.write("=" * 50 + "\n")
            f.write(research_result)
            f.write("\n\n" + "=" * 50 + "\n")
            f.write("DRAFT ARTICLE:\n")
            f.write("=" * 50 + "\n")
            f.write(article_result)
            f.write("\n\n" + "=" * 50 + "\n")
            f.write("FINAL ARTICLE:\n")
            f.write("=" * 50 + "\n")
            f.write(final_result)
        
        print(f"\n💾 All outputs saved to 'output.txt'")
        print("🎉 Workflow completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during workflow execution: {str(e)}")
        print("Please check your API key and internet connection")

if __name__ == "__main__":
    main()

