import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    abs_working_directory = os.path.abspath(working_directory)
    target_dir = abs_working_directory

    if directory:
            target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            # Check if the directory exists
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'


    try:
        # If directory is valid (or None), list files
        entries = os.listdir(target_dir if directory else abs_working_directory)
    except FileNotFoundError:
        return f'Error: Directory "{target_dir or abs_working_directory}" not found.'
    except PermissionError:
        return f'Error: Permission denied when accessing "{target_dir or abs_working_directory}".'
    except Exception as e:
        return f"Error: {str(e)}"
    
    # Build the string representation of the directory contents
    result = []
    for entry in entries:
        try:
            entry_path = os.path.join(target_dir or abs_working_directory, entry)
            is_dir = os.path.isdir(entry_path)
            file_size = os.path.getsize(entry_path) if not is_dir else 0

            result.append(f"{entry}: file_size={file_size} bytes, is_dir={is_dir}")
            
        except FileNotFoundError:
            return f"Error: File or directory '{entry}' not found."
        except PermissionError:
            return f"Error: Permission denied when accessing '{entry}'."
        except Exception as e:
            return f"Error: {str(e)}"

    return "\n".join(result)

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            'directory': types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
