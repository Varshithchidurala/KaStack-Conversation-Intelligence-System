import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

with open(
    "100_message_checkpoints.json",
    "r"
) as f:
    checkpoints = json.load(f)


def retrieve_message_checkpoints(
    query,
    top_k=3
):

    query_embedding = model.encode(query)

    scores = []

    for checkpoint in checkpoints:

        checkpoint_embedding = model.encode(
            checkpoint["summary"]
        )

        score = cosine_similarity(
            [query_embedding],
            [checkpoint_embedding]
        )[0][0]

        scores.append(
            (score, checkpoint)
        )

    scores.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return scores[:top_k]