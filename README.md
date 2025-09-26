# Research-Writing-Agent-Crew-AI

This project demonstrates a **multi-agent workflow** powered by **Google Gemini**.
The workflow includes three agents — **Researcher, Writer, and Editor** — that collaborate to generate polished content from research to final output.

---

## 🚀 Features

* **Research Agent** – Gathers information based on a given research task description.
* **Writer Agent** – Drafts an article using the research findings.
* **Editor Agent** – Reviews and polishes the article for clarity and quality.
* **Automated Workflow** – Runs the entire pipeline sequentially.
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
└── output.txt   (generated after running main.py)
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

### 4. Set up your API key

Create a `.env` file in the project root and add your **Google Gemini API key**:

```
GOOGLE_API_KEY=your_api_key_here
```

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

---

## 🛠️ Requirements

* Python 3.9+
* Google Gemini API key
* Dependencies listed in `requirements.txt`

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

---

## 📜 License

This project is licensed under the **MIT License**.

