import os
import subprocess

def run_python_file(working_directory, file_path):
    
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    abs_working_directory = os.path.abspath(working_directory)
    py_file = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not py_file.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    # Check if the file exists
    if not os.path.isfile(py_file):
        return f'Error: File "{file_path}" not found.'
    #check if its a python file


    try:
        result = subprocess.run(
            ['python3', py_file], 
            cwd=abs_working_directory,
            capture_output=True,
            text=True,
            timeout=30
        )
        stdout = result.stdout.strip()
        stderr = result.stderr.strip()
        
        # Format
        output = []
        
        if stdout:
            output.append(f'STDOUT: {stdout}')
        else:
            output.append('No output produced')
        if stderr:
            output.append(f'STDERR: {stderr}')    
        if result.returncode != 0:
            output.append(f'Process exited with code {result.returncode}')   
        return '\n'.join(output)
    except subprocess.TimeoutExpired:
        return "Error: Execution timed out after 30 seconds."
    except Exception as e:
        return f"Error: executing Python file: {e}"