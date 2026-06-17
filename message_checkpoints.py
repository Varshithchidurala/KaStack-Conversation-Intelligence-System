import json
import pandas as pd

from parser import parse_conversation

df = pd.read_csv(
    "conversations.csv",
    header=None
)

all_messages = []

# For testing use first 20 conversations
for _, row in df.head(20).iterrows():

    conversation = row[0]

    messages = parse_conversation(
        conversation
    )

    for msg in messages:

        all_messages.append(
            msg["text"]
        )

print(
    f"Total Messages: {len(all_messages)}"
)

checkpoints = []

for i in range(
    0,
    len(all_messages),
    100
):

    chunk = all_messages[i:i+100]

    summary = " ".join(
        chunk[:10]
    )[:300]

    checkpoints.append({
        "start_message": i + 1,
        "end_message":
            min(
                i + 100,
                len(all_messages)
            ),
        "summary": summary
    })

with open(
    "100_message_checkpoints.json",
    "w"
) as f:

    json.dump(
        checkpoints,
        f,
        indent=4
    )

print(
    f"Created {len(checkpoints)} checkpoints"
)