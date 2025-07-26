import streamlit as st
import openai

# Initialize OpenAI with your secret API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Set the app title
st.title("📊 Master Data Management Assistant")

# Initialize chat history with a MDM-focused system prompt
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are an expert AI assistant specialized in Master Data Management (MDM). "
                "You assist users with questions related to MDM concepts, tools, best practices, governance, "
                "data domains, implementation strategies, and enterprise use cases. "
                "You must only answer queries related to Master Data Management. "
                "If the user asks something unrelated to MDM, reply with: "
                "'I'm here to assist only with Master Data Management-related questions. "
                "Please ask about MDM concepts, tools, data governance, or implementation.' "
                "If a question is ambiguous or unclear, ask the user to clarify in the context of MDM."
            )
        }
    ]

# Display all previous messages
for msg in st.session_state.messages[1:]:  # Skip system prompt in UI
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask anything about Master Data Management...")

# Function to get AI response
def get_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message["content"]

# Process user input
if user_input:
    # Add user's message to history and show
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get AI response
    response = get_response(st.session_state.messages)
    
    # Add assistant response to history and show
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

# Optional: Add footer disclaimer
st.markdown("---")
st.markdown(
    "ℹ️ **Note:** This assistant is focused only on Master Data Management (MDM). For other topics, please consult the appropriate resources.",
    unsafe_allow_html=True
)
