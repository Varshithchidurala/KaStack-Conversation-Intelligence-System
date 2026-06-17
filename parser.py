import re

def parse_conversation(text):

    pattern = r"(User \d+):\s*(.*?)(?=(?:User \d+:)|$)"

    matches = re.findall(
        pattern,
        text,
        re.DOTALL
    )

    messages = []

    for i, (speaker, msg) in enumerate(matches):
        messages.append({
            "msg_id": i + 1,
            "speaker": speaker,
            "text": msg.strip()
        })

    return messages