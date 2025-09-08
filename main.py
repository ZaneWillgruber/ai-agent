import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    # make sure user passed an arg
    if len(sys.argv) <= 1:
        print("Make sure to pass and argument")
        sys.exit(1)

    # set variables
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    flags = sys.argv[2:]
    client = genai.Client(api_key=api_key)
    prompt = sys.argv[1]
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)]),]

    # talk to the llm
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages)

    print(response.text)

    if "--verbose" in flags:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {
              response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
