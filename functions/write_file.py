import os
from google.genai import types

def write_file(working_directory, file_path, content=None):
    abs_working_directory = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    # Check if the file is inside the working directory
    if not target_file.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    target_dir = os.path.dirname(target_file)
    if not os.path.exists(target_dir):
        try:
            os.makedirs(target_dir)  # Create the directory if it doesn't exist
        except Exception as e:
            return f"Error: Unable to create directory '{target_dir}'. Error details: {str(e)}"

    try:
        with open(target_file, "w") as f:
                if content:
                    f.write(content)  # Write the user-provided content into the file
                else:
                    f.write("") 
        content_length = len(content) if content else 0
        return f'Successfully wrote to "{file_path}" ({content_length} characters written)'
    except Exception as e:
        return f'Error: Unable to create file "{file_path}". Error details: {str(e)}'
    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file in the working directory, overwriting its current content.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to write to, relative to the working directory."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file. It will overwrite the existing content."
            ),
        },
    ),
)