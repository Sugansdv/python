import json
from core.utils import log_chat

class Chatbot:
    def __init__(self, response_file):
        self.responses = {}
        self.load_responses(response_file)

    def load_responses(self, path):
        try:
            with open(path, "r") as f:
                self.responses = json.load(f)
        except FileNotFoundError:
            print("Response file not found.")
        except json.JSONDecodeError:
            print("Invalid JSON format in response file.")

    @log_chat
    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        for key in self.responses:
            if key in user_input:
                return self.responses[key]
        return "I'm not sure how to respond to that."

    def response_generator(self):
        for key, value in self.responses.items():
            yield f"If user says '{key}', I reply: '{value}'"
