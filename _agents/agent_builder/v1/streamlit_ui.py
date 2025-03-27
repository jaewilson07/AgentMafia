from dotenv import load_dotenv

from pydantic_ai.messages import (
    ModelResponse,
    TextPart,
)

from v1.pydantic_ai_coder import (
    pydantic_ai_coder,
    PydanticAIDependencies,
    PydanticAgent,
    dependencies,
)

from agent_mafia.classes.streamlit_ui import streamlit_ui, st


load_dotenv()


async def run_agent_with_streaming(
    agent: PydanticAgent, user_input: str, dependencies: PydanticAIDependencies
):
    """
    Run the agent with streaming text for the user_input prompt,
    while maintaining the entire conversation in `st.session_state.messages`.
    """

    async with pydantic_ai_coder.run_stream(
        user_prompt=user_input,
        deps=dependencies,
        message_history=st.session_state.messages[
            :-1
        ],  # pass entire conversation so far
    ) as result:
        # gather partial text to show streaming results incrementally

        partial_text = ""

        message_placeholder = st.empty()

        # render partial_text as it arrives
        async for chunk in result.stream_text(delta=True):
            partial_text += chunk
            message_placeholder.markdown(partial_text)

        # add new messages excluding initial user_prompt
        filtered_messages = [
            msg
            for msg in result.new_messages()
            if not (
                hasattr(msg, "parts")
                and any(part.part_kind == "user-prompt" for part in msg.parts)
            )
        ]
        st.session_state.messages.extend(filtered_messages)

        # Add the final response to the messages
        st.session_state.messages.append(
            ModelResponse(parts=[TextPart(content=partial_text)])
        )
