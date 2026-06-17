import json
import pandas as pd

from parser import parse_conversation
from topic_detector import detect_topics
from summarizer import summarize_topic

df = pd.read_csv("conversations.csv", header=None)

all_topics = []

for idx, row in df.head(20).iterrows():

    conversation = row[0]

    messages = parse_conversation(conversation)

    topics = detect_topics(messages)

    for topic in topics:

        summary = summarize_topic(
            topic["messages"]
        )

        all_topics.append({
            "conversation_id": idx + 1,
            "topic_id": topic["topic_id"],
            "start_message":
                topic["messages"][0]["msg_id"],
            "end_message":
                topic["messages"][-1]["msg_id"],
            "summary": summary
        })

with open(
    "topic_checkpoints.json",
    "w"
) as f:

    json.dump(
        all_topics,
        f,
        indent=4
    )

print(
    f"Saved {len(all_topics)} topic checkpoints"
)