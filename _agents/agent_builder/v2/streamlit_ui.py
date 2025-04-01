import uuid

from langgraph.types import Command

from agent_mafia.classes.streamlit_ui import streamlit_ui, st

from graph import agentic_flow


@st.cache_resource
def get_thread_id():
    return str(uuid.uuid4())


thread_id = get_thread_id()


async def run_agent_with_streaming(user_input: str):
    """
    Run the agent with streaming text for the user_input prompt,
    while maintaining the entire conversation in `st.session_state.messages`.
    """
    config = {"configurable": {"thread_id": thread_id}}

    # First message from user
    if len(st.session_state.messages) == 1:
        async for msg in agentic_flow.astream(
            {"latest_user_message": user_input}, config, stream_mode="custom"
        ):
            yield msg
    # Continue the conversation
    else:
        async for msg in agentic_flow.astream(
            Command(resume=user_input), config, stream_mode="custom"
        ):
            yield msg
