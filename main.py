import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from call_function import available_functions
from prompts import system_prompt


def main():

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    verbose = "--verbose" in sys.argv

    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: uv run main.py "your prompt here" [--verbose]')
        print('Example: uv run main.py "How do I build a calculator app?"')
        sys.exit(1)

    client = genai.Client(api_key=api_key)
    user_prompt = " ".join(args)
    if user_prompt == []:
        print("No prompt provided.")
        sys.exit(1)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]
    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=[system_prompt])
    )
    if verbose:
        print(f"Request tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    print("Response: ")
    print(response.text)

    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")


if __name__ == "__main__":
    main()
