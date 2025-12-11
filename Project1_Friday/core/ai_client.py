from openai import OpenAI

# Initialize OpenAI client once
client = OpenAI(
    api_key="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"
)

def openai_response(command: str) -> str:
    """
    Sends the command to OpenAI and returns the text response.
    """

    try:
        response = client.responses.create(
            model="gpt-5-nano",
            input=command
        )

        # Extract the text from the response
        output = response.output_text.strip()
        print("AI Response:", output)
        return output

    except Exception as e:
        print("OpenAI Error:", e)
        return "Sorry, I couldn't get an AI response."
