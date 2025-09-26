
# Simple Agent Workflow with Google Gemini

This project demonstrates a **multi-agent workflow** powered by **Google Gemini**.
The workflow includes three agents — **Researcher, Writer, and Editor** — that collaborate to generate polished content from research to final output.

The workflow is designed with **robust error handling, modular structure, input validation, JSON validation, and secure API management**.

---

## 🚀 Features

* **Research Agent** – Gathers information based on a given research task description.
* **Writer Agent** – Drafts an article using the research findings.
* **Editor Agent** – Reviews and polishes the article for clarity and quality.
* **Robust Error Handling** – Failures are caught, logged, and reported gracefully.
* **Input Validation** – Ensures task descriptions and responses are valid.
* **JSON Validation** – Validates response structure before processing.
* **Security** – API keys are loaded from environment variables, not hardcoded.
* **Logging** – Detailed logs are stored in `workflow.log`.
* **Output Storage** – Saves research findings, draft article, and final article into `output.txt`.

---

## 📂 Project Structure

```
.
├── agents/
│   ├── researcher.py
│   ├── writer.py
│   └── editor.py
├── tasks/
│   ├── research_task_description.py
│   ├── writing_task_description.py
│   └── editing_task_description.py
├── main.py
├── .env
├── workflow.log   (generated at runtime for errors and execution details)
└── output.txt     (generated after successful workflow run)
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/simple-agent-gemini.git
cd simple-agent-gemini
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate    # On Mac/Linux
venv\Scripts\activate       # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and add your **Google Gemini API key**:

```
GOOGLE_API_KEY=your_api_key_here
```

⚠️ **Do not commit your `.env` file** to version control.

---

## ▶️ Usage

Run the workflow with:

```bash
python main.py
```

The script will:

1. Perform research
2. Generate a draft article
3. Edit the draft into a final version
4. Save all results into `output.txt`
5. Log execution details and errors into `workflow.log`

---

## 📄 Output Example

After execution, `output.txt` will contain:

```
RESEARCH FINDINGS:
==================================================
...

DRAFT ARTICLE:
==================================================
...

FINAL ARTICLE:
==================================================
...
```

If an error occurs, check `workflow.log` for details.

---

## 🛡️ Error Handling & Validation

* **Error Handling:** All workflow steps are wrapped in `try...except`, and errors are logged with stack traces in `workflow.log`.
* **Input Validation:** Ensures task descriptions are non-empty strings before execution.
* **JSON Validation:** Optional validation to ensure OpenAI/Gemini responses return valid JSON.
* **Security:** API keys are stored in `.env` file using `python-dotenv`.

---

## 🛠️ Requirements

* Python 3.9+
* Google Gemini API key
* Dependencies listed in `requirements.txt`

---

## 🤝 Contributing

Contributions are welcome! Please submit issues or pull requests to improve functionality.

---

## 📜 License

This project is licensed under the **MIT License**.
