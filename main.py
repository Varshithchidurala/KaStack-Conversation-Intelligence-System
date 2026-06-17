import pandas as pd

from parser import parse_conversation
from topic_detector import detect_topics
from summarizer import summarize_topic

df = pd.read_csv(
    "conversations.csv",
    header=None
)

conversation = df.iloc[0, 0]

messages = parse_conversation(
    conversation
)

topics = detect_topics(
    messages
)

for topic in topics:

    summary = summarize_topic(
        topic["messages"]
    )

    print("\n==========")

    print(
        f"Topic {topic['topic_id']}"
    )

    print(
        f"Messages: {len(topic['messages'])}"
    )

    print(
        f"Summary: {summary}"
    )