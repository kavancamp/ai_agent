from dotenv import load_dotenv
import os
from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_content import get_file_content, schema_get_file_content
from functions.run_python_file import run_python_file, schema_run_python_file
from functions.write_file import write_file, schema_write_file
from google.genai import types


# Load environment variables from the .env file
load_dotenv()

    # Declare available functions
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ]
)
   
# Define the call_function
def call_function(function_call_part, verbose=False):
    
    WORK_DIR = os.environ.get("WORKING_DIRECTORY") 
    # Extract function name and arguments
    function_name = function_call_part.name
    function_args = function_call_part.args

    # Add the "working_directory" argument
    function_args["working_directory"] = WORK_DIR  # Hardcoded working directory
    
    # Define a dictionary to map function names to actual functions
    function_dict = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file
    }
    
    # Check if the function name is valid
    if function_name not in function_dict:
        # Return an error response if the function name is invalid
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"}
                )
            ]
        )
    
    # Get the function reference from the dictionary
    function = function_dict[function_name]
    
    # If verbose is specified, print the function name and arguments
    if verbose:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    # Call the function with the arguments and capture the result
    try:
        function_result = function(**function_args)
    except Exception as e:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": str(e)}
                )
            ]
        )
    
    # Return the function result in the required format
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result}
            )
        ]
    )
