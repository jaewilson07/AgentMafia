from agent_mafia.routes.pydantic import generate_pydantic_agent

# Add the parent directory to sys.path
import os
from dotenv import load_dotenv

load_dotenv()

base_url: str = os.getenv("BASE_URL", "https://api.openai.com/v1")
api_key: str = os.getenv("LLM_API_KEY", "no-llm-api-key")
primary_model_name = os.getenv("PRIMARY_MODEL", "gpt-40-mini")


router_agent = generate_pydantic_agent(
    model_name=primary_model_name,
    base_url=base_url,
    api_key=api_key,
    system_prompt="Your job is to route the user message either to the end of the conversation or to continue coding the AI agent.",
)
