import os
from dotenv import load_dotenv
from google import genai


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)


def main():
    print("Hello from cli-agent!")
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", contents="just checking if u work. say hi if u do."
    )
    print(response.text)
    print(f"The amount of tokens used for the req: {response.usage_metadata.prompt_token_count}")
    print(f"The amount of tokens used for the response: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
