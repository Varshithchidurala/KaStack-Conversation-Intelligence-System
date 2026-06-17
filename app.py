import streamlit as st
import json

from rag_utils import retrieve_topics

st.set_page_config(
    page_title="KaStack Conversation Intelligence System",
    page_icon="🤖",
    layout="wide"
)

# Load data
with open("persona.json", "r") as f:
    persona = json.load(f)

with open("topic_checkpoints.json", "r") as f:
    topics = json.load(f)

with open("100_message_checkpoints.json", "r") as f:
    checkpoints = json.load(f)

# Header
st.title("🤖 KaStack Conversation Intelligence System")

st.markdown("""
A Retrieval-Augmented Generation (RAG) system that:
- Detects topic changes
- Creates topic checkpoints
- Creates 100-message checkpoints
- Extracts user persona
- Answers questions using retrieval
""")

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Topic Checkpoints", len(topics))

with col2:
    st.metric("100 Msg Checkpoints", len(checkpoints))

with col3:
    st.metric("Habits Extracted", len(persona["habits"]))

st.divider()

# Question
question = st.text_input(
    "Ask a question",
    placeholder="What kind of person is this user?"
)

if question:

    q = question.lower()

    st.header("Answer")

    # User profile
    if "person" in q:

        st.subheader("👤 User Profile")

        st.info(
            "The user appears to be a student who frequently discusses studying and work-related topics."
        )

        st.subheader("📌 Personal Facts")

        for fact in persona["personal_facts"]:
            st.write(f"• {fact['fact']}")
            st.caption(f"Evidence: {fact['evidence']}")

        st.subheader("⭐ Habits")

        for habit in persona["habits"]:
            st.write(f"• {habit['habit']}")
            st.caption(f"Evidence: {habit['evidence']}")

        st.subheader("🌟 Personality Traits")

        for trait in persona["personality_traits"]:
            st.write(f"• {trait['trait']}")
            st.caption(f"Evidence: {trait['evidence']}")

    # Habits
    elif "habit" in q:

        st.subheader("⭐ User Habits")

        for habit in persona["habits"]:
            st.write(f"• {habit['habit']}")
            st.caption(f"Evidence: {habit['evidence']}")

    # Communication
    elif "talk" in q or "communication" in q:

        st.subheader("💬 Communication Style")

        style = persona["communication_style"]

        st.write(
            f"Average words/message: {style['average_words_per_message']}"
        )

        st.write(
            f"Message style: {style['message_style']}"
        )

        st.caption(style["evidence"])

    else:
        st.info(
            "Showing information retrieved from conversation checkpoints."
        )

    # RAG Retrieval
    st.subheader("🔍 Related Retrieved Topics")

    results = retrieve_topics(question)

    for score, topic in results:

        st.write(f"• {topic}")
        st.caption(f"Similarity Score: {score:.2f}")

    # Message checkpoints
    st.subheader("📚 Message Checkpoint Samples")

    for checkpoint in checkpoints[:3]:

        st.write(
            f"Messages {checkpoint['start_message']} - {checkpoint['end_message']}"
        )

        st.caption(checkpoint["summary"])