import os


from dotenv import load_dotenv
from agent_mafia.routes.pydantic import generate_pydantic_agent

load_dotenv()

base_url: str = os.getenv("BASE_URL", "https://api.openai.com/v1")
api_key: str = os.getenv("LLM_API_KEY", "no-llm-api-key")

reasoner_model_name = os.getenv("REASONER_LLM_MODEL", "03-mini")

reasoner_agent = generate_pydantic_agent(
    model_name=reasoner_model_name,
    base_url=base_url,
    api_key=api_key,
    system_prompt="You are an expert at coding AI agents with Pydantic AI and defining the scope for doing so.",
)
