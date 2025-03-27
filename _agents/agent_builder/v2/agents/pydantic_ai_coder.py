from dotenv import load_dotenv
from pydantic_ai import RunContext

load_dotenv()

import sys

sys.path.append("../../")
from ...v1.pydantic_ai_coder import pydantic_ai_coder


@pydantic_ai_coder.system_prompt
def add_reasoner_output(ctx: RunContext[str]) -> str:
    return f"""
    
    Additional thoughts/instructions from the reasoner LLM. 
    This scope includes documentation pages for you to search as well: 
    {ctx.deps.reasoner_output}
    """
