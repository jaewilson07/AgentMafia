import os
import sys

from dotenv import load_dotenv

load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import utils


base_url: str = os.getenv("BASE_URL", "https://api.openai.com/v1")
is_ollama = "localhost" in base_url.lower()
api_key: str = os.getenv("LLM_API_KEY", "no-llm-api-key")


reasoner_model_name = os.getenv("REASONER_LLM_MODEL", "03-mini")
primary_model_name = os.getenv("PRIMARY_MODEL", "gpt-40-mini")

reasoner_agent = utils.generate_agent(
    model_name=reasoner_model_name,
    base_url=base_url,
    api_key=api_key,
    system_prompt="You are an expert at coding AI agents with Pydantic AI and defining the scope for doing so.",
)


# Scope Defi