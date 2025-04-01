import os
from agent_mafia.routes.pydantic import generate_pydantic_agent
from dotenv import load_dotenv

import sys


base_url: str = os.getenv("BASE_URL", "https://api.openai.com/v1")
api_key: str = os.getenv("LLM_API_KEY", "no-llm-api-key")
primary_model_name = os.getenv("PRIMARY_MODEL", "gpt-40-mini")

end_conversation_agent = generate_pydantic_agent(
    model_name=primary_model_name,
    base_url=base_url,
    api_key=api_key,
    system_prompt="Your job is to end a conversation for creating an AI agent by giving instructions for how to execute the agent and they saying a nice goodbye to the user.",
)
