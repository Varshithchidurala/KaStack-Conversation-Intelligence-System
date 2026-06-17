import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

with open(
    "topic_checkpoints.json",
    "r"
) as f:
    topics = json.load(f)

query = input("Ask: ")

query_embedding = model.encode(query)

scores = []

for topic in topics:

    topic_embedding = model.encode(
        topic["summary"]
    )

    score = cosine_similarity(
        [query_embedding],
        [topic_embedding]
    )[0][0]

    scores.append(
        (score, topic)
    )

scores.sort(
    reverse=True,
    key=lambda x: x[0]
)

print("\nTop Results:\n")

for score, topic in scores[:3]:

    print(
        f"Score: {score:.2f}"
    )

    print(
        topic["summary"]
    )

    print("-" * 40)