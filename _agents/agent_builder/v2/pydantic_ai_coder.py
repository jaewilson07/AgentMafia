import os
from dotenv import load_dotenv
import sys

from pydantic_ai import RunContext

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


load_dotenv()

from v1.pydantic_ai_coder import pydantic_ai_coder


@pydantic_ai_coder.system_prompt
def add_reasoner_output(ctx: RunContext[str]) -> str:
    return f"""
    
    Additional thoughts/instructions from the reasoner LLM. 
    This scope includes documentation pages for you to search as well: 
    {ctx.deps.reasoner_output}
    """
