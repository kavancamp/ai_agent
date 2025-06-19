import os

def get_files_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    
    if file_path:
        # Resolve the absolute path for the target file
        target_file = os.path.abspath(os.path.join(working_directory, file_path))

    # Check if the file is inside the working directory
    if not target_file.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    # Check if the file exists and is a regular file
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    # Set the maximum number of characters to read from the file
    MAX_CHARS = 10000
    try:
        with open(target_file, "r") as f_content:
            file_content_string = f_content.read(MAX_CHARS)

            # If the file content exceeds MAX_CHARS, add the truncation message
            if len(f_content.read()) > 0:
                file_content_string += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    except IOError as e:
            return f"Error: Unable to read the file '{file_path}'. Error details: {str(e)}"
    except Exception as e:
            return f"Error: {str(e)}"
    return file_content_string