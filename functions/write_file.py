import os
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
    
