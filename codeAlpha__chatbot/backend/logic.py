import json
import re

def load_intents():
    with open("data/intents.json") as f:
        return json.load(f)

def get_response(message):
    intents = load_intents()
    for item in intents:
        for pattern in item["patterns"]:
            if re.search(pattern, message, re.IGNORECASE):
                return item["response"]
    return "🤔 I'm not sure how to answer that."
