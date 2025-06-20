from dotenv import load_dotenv
import os
import sys
from google import genai
from google.genai import types
from functions.call_function import call_function, available_functions
from prompt import system_prompt


def main():
    load_dotenv()
        
    # Check for verbose flag and capture prompt arguments
    verbose_flag = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    
    if len(args) > 0: 
        user_prompt = " ".join(args)  # Combine arguments into a single user prompt
    else:
        print("Code Assistant") 
        print('\nUsage: python main.py "Enter your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)  # Exit the program with exit code 1
        
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    model_name = 'gemini-2.0-flash-001'    
    
    if not api_key:
        print("API key not found. Please check your .env file.")
        return

    # Prepare the initial message for the model
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]              
    
    iteration_count = 0
    conversation_complete = False
    MAX_ITER = int(os.environ.get("MAX_ITERATIONS", 20)) # Default to 20 if not found
    while not conversation_complete and iteration_count < MAX_ITER:
        try:
            final_response = gen_content(client, messages, verbose_flag)
            if final_response:
                print("Final response:")
                print(final_response)
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")
            break

        iteration_count += 1

def gen_content(client, messages, verbose_flag):
    # Generate the response with the system instructions
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], 
            system_instruction=system_prompt
        ),
    )

    # If verbose is set, print the result of the function call
    if verbose_flag and response:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    # Check for candidates (possible answers) in the response
    if response.candidates:
        new_content = False
        for candidate in response.candidates:
            function_content = candidate.content
            messages.append(function_content)
    if not response.function_calls:
        return response.text

    function_responses = []
    # Process function calls in the response
    for function_call in response.function_calls:
        # Call the function and get the result
        function_call_result = call_function(function_call, verbose=verbose_flag)
        
        # Ensure the function call result is valid
        if (not function_call_result.parts or not function_call_result.parts[0].function_response):
            raise Exception("Empty function call result")
        
        # If verbose, print the function response
        if verbose_flag:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])
    
    if not function_responses:
        raise Exception("No function responses generated, exiting.")
    
    # Add the function responses to the messages list
    messages.append(types.Content(role="tool", parts=function_responses))



if __name__ == "__main__":
    main()
