"""Streamlit interface for the DecodeLabs Rule-Based AI Chatbot."""

import streamlit as st

from chatbot import BOT_NAME, get_response


st.set_page_config(
    page_title=f"{BOT_NAME} - Rule-Based AI Chatbot",
    page_icon="🤖",
)

st.title(f"🤖 {BOT_NAME}")
st.caption(
    "A rule-based AI chatbot developed for the "
    "DecodeLabs Artificial Intelligence Internship."
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                f"Hello! I'm {BOT_NAME}, your rule-based AI chatbot. "
                "Type 'help' to see what you can ask."
            ),
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_message = st.chat_input("Type your message here")

if user_message:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message,
        }
    )

    with st.chat_message("user"):
        st.write(user_message)

    response, should_exit = get_response(user_message)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )

    with st.chat_message("assistant"):
        st.write(response)

    if should_exit:
        st.info("The conversation has ended. Start a new chat to continue.")

if st.sidebar.button("Start new chat"):
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                f"Hello! I'm {BOT_NAME}. "
                "Type 'help' to see what you can ask."
            ),
        }
    ]
    st.rerun()

with st.sidebar:
    st.subheader("Example questions")
    st.write("• hello")
    st.write("• how are you")
    st.write("• what is your name")
    st.write("• what can you do")
    st.write("• what is artificial intelligence")
    st.write("• what is a rule based chatbot")
    st.write("• tell me about this project")
    st.write("• help")
    st.write("• exit")
