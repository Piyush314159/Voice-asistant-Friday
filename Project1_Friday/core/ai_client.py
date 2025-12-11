from openai import OpenAI
import os

# Use environment variable instead of hardcoded key
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")  # Set this in your environment
)

def openai_response(command: str) -> str:
    """
    Sends the command to OpenAI and returns the text response.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Fixed: Use real model
            messages=[
                {"role": "user", "content": command}
            ],
            max_tokens=150
        )

        # Fixed: Correct response structure
        output = response.choices[0].message.content.strip()
        print("AI Response:", output)
        return output

    except Exception as e:
        print("OpenAI Error:", e)
        return "Sorry, I couldn't get an AI response."
