# Simple Multi-Agent System with Google Gemini

A simple multi-agent system using Google Gemini API as the LLM provider, inspired by Crew.AI concepts but without the dependency requirements.

## Project Structure

```
├── agents.py          # Agent definitions
├── tasks.py           # Task definitions
├── main.py           # Main execution script
├── requirements.txt   # Python dependencies
├── env_example.txt    # Environment variables template
└── README.md         # This file
```

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get Google Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the API key

### 3. Configure Environment Variables

Create a `.env` file in the project root and add your API key:

```bash
# Create .env file
echo "GOOGLE_API_KEY=your_actual_api_key_here" > .env
echo "GEMINI_MODEL=gemini-2.5-flash" >> .env
```

Or manually create a `.env` file with:

```
GOOGLE_API_KEY=your_actual_api_key_here
GEMINI_MODEL=gemini-2.5-flash
```

### 4. Run the Crew

```bash
python main.py
```

## How It Works

This system consists of three agents working sequentially:

1. **Research Analyst**: Gathers information about AI in healthcare using Google Gemini
2. **Content Writer**: Creates an engaging article based on research findings
3. **Content Editor**: Reviews and polishes the final content

The workflow produces a comprehensive article about "The Future of Artificial Intelligence in Healthcare" using Google Gemini 2.5 Flash model.

## Output

The final result will be:
- Displayed in the terminal
- Saved to `output.txt` file

## Customization

You can easily modify:
- **Topics**: Change the research topic in `tasks.py`
- **Agents**: Add new agents or modify existing ones in `agents.py`
- **Tasks**: Create new tasks or modify existing ones in `tasks.py`
- **Model**: Change the Gemini model in the `.env` file

## Troubleshooting

- Ensure your Google API key is valid and has access to Gemini
- Check your internet connection
- Verify all dependencies are installed correctly

