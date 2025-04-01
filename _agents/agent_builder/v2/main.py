import asyncio

from streamlit_ui import (
    streamlit_ui,
    run_agent_with_streaming,
)


async def main():
    await streamlit_ui(
        title="Agent Builder",
        description="Describe an agent and I'll code it for you.",
        default_chat_input="What questions do you have about Pydantic AI?",
        run_agent_with_streaming=run_agent_with_streaming,
    )


if __name__ == "__main__":
    asyncio.run(main())
