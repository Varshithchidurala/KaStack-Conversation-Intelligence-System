from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


def detect_topics(messages, threshold=0.35):

    topics = []

    current_topic = [messages[0]]

    current_embedding = model.encode(
        messages[0]["text"]
    )

    topic_id = 1

    for msg in messages[1:]:

        msg_embedding = model.encode(
            msg["text"]
        )

        similarity = cosine_similarity(
            [current_embedding],
            [msg_embedding]
        )[0][0]

        if similarity < threshold:

            topics.append({
                "topic_id": topic_id,
                "messages": current_topic
            })

            topic_id += 1

            current_topic = [msg]

            current_embedding = msg_embedding

        else:

            current_topic.append(msg)

            current_embedding = np.mean(
                [
                    current_embedding,
                    msg_embedding
                ],
                axis=0
            )

    topics.append({
        "topic_id": topic_id,
        "messages": current_topic
    })

    return topics