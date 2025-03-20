import os
import sys


from dotenv import load_dotenv


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to sys.path
sys.path.append(parent_dir)
import utils

load_dotenv()

base_url: str = os.getenv("BASE_URL", "https://api.openai.com/v1")
is_ollama = "localhost" in base_url.lower()
api_key: str = os.getenv("LLM_API_KEY", "no-llm-api-key")

primary_model_name = os.getenv("PRIMARY_MODEL", "gpt-40-mini")

end_conversation_agent = utils.generate_agent(
    model_name=primary_model_name,
    base_url=base_url,
    api_key=api_key,
    system_prompt="Your job is to end a conversation for creating an AI agent by giving instructions for how to execute the agent and they saying a nice goodbye to the user.",
)
