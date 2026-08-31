import streamlit as st
import ollama

st.set_page_config(
    page_title="Biology Chatbot",
    page_icon="🧬"
)

st.title("🧬 Biology Chatbot")
st.write("Ask me a biology question.")

# Store conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Enter your biology question...")

if prompt:

    # Display user question
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Instructions for the AI
    system_prompt = """
You are a Biology Chatbot.

Your ONLY job is to answer biology-related questions.

You can answer questions about:
- Cell biology
- Human biology
- Animal biology
- Plant biology
- Genetics
- Ecology
- Evolution
- Microbiology
- Zoology
- Botany
- Anatomy
- Physiology
- Reproduction
- Classification
- Nutrition
- Photosynthesis
- Respiration
- Diseases caused by microorganisms
- Biotechnology
- Environmental biology

IMPORTANT RULES:

1. Answer ONLY biology-related questions.
2. Always answer in English.
3. Explain biology answers clearly and simply.
4. Do not answer mathematics, programming, computer science,
   history, geography, politics, business, or other non-biology questions.
5. If the question is not related to biology, reply exactly:

"I don't know. I can only answer biology questions."

6. Do not pretend to know an answer when you are unsure.
7. For biology questions, provide a clear and educational answer.
"""

    try:
        response = ollama.chat(
            model="qwen2.5:0.5b",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                *st.session_state.messages
            ]
        )

        answer = response["message"]["content"]

    except Exception as e:
        answer = (
            "I cannot connect to Ollama. "
            "Please make sure Ollama is running "
            "and qwen2.5:0.5b is installed."
        )

    # Display AI answer
    with st.chat_message("assistant"):
        st.markdown(answer)

    # Save AI answer
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
