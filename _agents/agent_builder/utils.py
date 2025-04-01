# import os

# from dataclasses import dataclass

# from pydantic_ai import Agent as PydanticAgent
# from pydantic_ai.models.openai import OpenAIModel

# from openai import AsyncOpenAI
# from openai import AsyncClient as AsyncOpenaiClient

# from supabase import AsyncClient as AsyncSupabaseClient

# from agent_mafia.utils import files as amfi

# openai_api_key = os.getenv("OPENAI_API_KEY")


# @dataclass
# class PydanticAIDependencies:
#     async_supabase_client: AsyncSupabaseClient
#     async_openai_client: AsyncOpenaiClient
#     reasoner_output: str = None


# def generate_open_ai_client(
#     base_url: str, api_key: str, is_ollama: bool = False
# ) -> AsyncOpenAI:

#     if is_ollama:
#         return AsyncOpenAI(
#             api_key=api_key,
#             base_url=base_url,
#         )

#     return AsyncOpenAI(api_key=openai_api_key)


# def generate_agent(
#     model_name, base_url, api_key, system_prompt, retries=0, debug_prn: bool = False
# ) -> PydanticAgent:
#     if debug_prn:

#         print(
#             {
#                 "agent_config": {
#                     "model_name": model_name,
#                     "base_url": base_url,
#                     "api_key": api_key,
#                     # "system_prompt": system_prompt,
#                     "retries": 0,
#                 }
#             }
#         )

#     model = OpenAIModel(
#         provider="openai",
#         model_name=model_name,
#         base_url=base_url,
#         api_key=api_key,
#     )

#     # print(model)
#     return PydanticAgent(
#         model=model,
#         system_prompt=system_prompt,
#         deps_type=PydanticAIDependencies,
#         retries=retries,
#     )


# def save_to_markdown(markdown_path, data):
#     amfi.upsert_folder(markdown_path)

#     with open(markdown_path, "w", encoding="utf-8") as f:
#         f.write(data)
