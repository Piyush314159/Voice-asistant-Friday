from core.ai_client import openai_response
from core.speech import speak

def fallback_action(command: str):
    response = openai_response(command)
    return speak(response)