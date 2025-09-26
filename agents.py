import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

class SimpleAgent:
    """Simple agent class that uses Google Gemini"""
    
    def __init__(self, role, goal, backstory, model="gemini-2.5-flash"):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.model_name = model
        self.api_key = os.getenv("GOOGLE_API_KEY")
        
        # Configure Gemini
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(self.model_name)
    
    def execute_task(self, task_description, context=""):
        """Execute a task using Gemini"""
        prompt = f"""
        You are a {self.role}.
        
        Your goal: {self.goal}
        
        Your background: {self.backstory}
        
        Task: {task_description}
        
        Context from previous work: {context}
        
        Please complete this task with high quality output.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error executing task: {str(e)}"

# Define Agents
researcher = SimpleAgent(
    role='Research Analyst',
    goal='Gather and analyze information on given topics',
    backstory='You are an experienced research analyst with expertise in data collection and analysis. You excel at finding relevant information and presenting it in a clear, structured manner.'
)

writer = SimpleAgent(
    role='Content Writer',
    goal='Create engaging and informative content based on research findings',
    backstory='You are a skilled content writer who specializes in transforming research data into compelling narratives. You have a talent for making complex information accessible and engaging.'
)

editor = SimpleAgent(
    role='Content Editor',
    goal='Review and refine content for clarity, accuracy, and quality',
    backstory='You are a meticulous editor with an eye for detail. You ensure content is polished, accurate, and meets high quality standards before publication.'
)

