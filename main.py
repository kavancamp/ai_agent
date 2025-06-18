import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

def main():
    load_dotenv()
    
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        print("API key not found. Please check your .env file.")
        return
    
    client = genai.Client(api_key=api_key)
    
    # Check for verbose flag and capture prompt arguments
    verbose_flag = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    
    if len(args) > 0: 
        user_prompt = " ".join(args)  # Combine arguments into a single user prompt
    else:
        print("Error: No command-line argument provided.")
        sys.exit(1)  # Exit the program with exit code 1
    
    # Prepare message for the model
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]              
    
    # Generate the response
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages  # Pass the prompt as a list
    )
    
    # If "--verbose" flag is set, print detailed information
    if verbose_flag: 
        print(f"User prompt: {user_prompt}\n")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    # Print the response text
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()