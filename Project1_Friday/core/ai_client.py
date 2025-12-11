from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def openai_response(command: str) -> str:
    """
    Sends the command to OpenAI and returns the text response.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-5-nano",
            messages=[
                {"role": "user", "content": command}
            ]
        )

        output = response.choices[0].message["content"].strip()
        print("AI Response:", output)
        return output

    except Exception as e:
        print("OpenAI Error:", e)
        return "Sorry, I couldn't get an AI response."
