import json
import requests

# def load_conversation_data():
    
#     with open("conversation2.json", encoding="utf-8") as f:
#         json_file = json.load(f)
#         extraction = lambda x: f"x{['speaker']}, x{['message']}"
#         conversation = list(map(extraction, json_file))
#         conversation_string = "\n".join(conversation)

#         return conversation_string

def load_conversation_data():
    with open("conversation2.json", encoding="utf-8") as f:
        json_file = json.load(f)
        extraction = lambda x: f"{x['speaker']}: {x['message']}"
        conversation = [extraction(entry) for entry in json_file]
        conversation_string = "\n".join(conversation)
        return conversation_string

    
conversation_string = load_conversation_data()    

prompt ={
    """Your goal is to summarize the given conversation to roughly 300 words. it is from a conversation between two or more people"""
}

OLLAMA_ENDPOINT  = "http://localhost:11434/api/generate"

OLLAMA_PROMPT = f"{prompt}, {conversation_string}"

OLLAMA_DATA = {
    "model" : "gemma:2b",
    "prompt": OLLAMA_PROMPT,
    "stream": False,
    "keep_alive" : "1m",
}

response = requests.post(OLLAMA_ENDPOINT, json = OLLAMA_DATA)
print(response.json()["response"])