import os
from dotenv import load_dotenv
from google import genai
import sys

def main():

    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    if len(sys.argv) > 1: 
        prompt = [sys.argv[0]]
    else:
        print("No command-line argument provided.")
        
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=prompt
    )

    print("\nPrompt:", prompt[0])
    # Print the text response
    print("\nResponse:", response.text)
    # Print the token counts
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")

    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")




if __name__ == "__main__":
    main()