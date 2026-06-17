from collections import Counter
import re

STOPWORDS = {
    "that","there","this","with","have","from","your",
    "about","going","really","would","could","should",
    "what","when","where","which","into","they","them",
    "their","been","being","very","just","also"
}

def summarize_topic(messages):

    text = " ".join(
        msg["text"]
        for msg in messages
    )

    words = re.findall(
        r"\b[a-zA-Z]{4,}\b",
        text.lower()
    )

    words = [
        w for w in words
        if w not in STOPWORDS
    ]

    common = Counter(words).most_common(5)

    keywords = [
        word
        for word, count in common
    ]

    return (
        "Discussion about: "
        + ", ".join(keywords)
    )