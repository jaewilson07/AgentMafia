# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/routes/pydantic.ipynb.

# %% auto 0
__all__ = ['PydanticAIDependencies', 'generate_pydantic_agent']

# %% ../../nbs/routes/pydantic.ipynb 1
from dataclasses import dataclass


from openai import AsyncClient as AsyncOpenaiClient
from supabase import AsyncClient as AsyncSupabaseClient

from pydantic_ai import Agent as PydanticAgent
from pydantic_ai.models.openai import OpenAIModel


# %% ../../nbs/routes/pydantic.ipynb 2
@dataclass
class PydanticAIDependencies:
    async_supabase_client: AsyncSupabaseClient
    async_openai_client: AsyncOpenaiClient
    reasoner_output: str = None


# %% ../../nbs/routes/pydantic.ipynb 3
def generate_pydantic_agent(
    model_name,
    base_url,
    api_key,
    system_prompt,
    retries=0,
    provider="openai",
    debug_prn: bool = False,
) -> PydanticAgent:

    if debug_prn:
        print(
            {
                "agent_config": {
                    "model_name": model_name,
                    "base_url": base_url,
                    "api_key": api_key,
                    # "system_prompt": system_prompt,
                    "retries": retries,
                }
            }
        )

    model = OpenAIModel(
        provider=provider,
        model_name=model_name,
        base_url=base_url,
        api_key=api_key,
    )

    return PydanticAgent(
        model=model,
        system_prompt=system_prompt,
        deps_type=PydanticAIDependencies,
        retries=retries,
    )
