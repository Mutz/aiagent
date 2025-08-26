import os
import subprocess
import sys

def run_python_file(working_directory, file_path, args=[]):
    """
    Execute a Python file within the permitted working directory.
    
    Args:
        working_directory (str): The permitted working directory
        file_path (str): Path to the Python file to execute
        args (list): Command line arguments to pass to the Python file
    
    Returns:
        str: Output from the Python execution or error message
    """
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    # Check if file is within working directory
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    # Check if file exists
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    # Check if file is a Python file
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        # Prepare the command to execute the Python file
        cmd = [sys.executable, abs_file_path] + args
        
        # Execute the Python file and capture output
        completed_process = subprocess.run(
            cmd,
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=30  # 30 second timeout
        )
        
        # Format the output
        output_parts = []
        
        # Add stdout if present
        if completed_process.stdout:
            output_parts.append(f"STDOUT:\n{completed_process.stdout}")
        
        # Add stderr if present
        if completed_process.stderr:
            output_parts.append(f"STDERR:\n{completed_process.stderr}")
        
        # Add return code information if non-zero
        if completed_process.returncode != 0:
            output_parts.append(f"Process exited with code {completed_process.returncode}")
        
        # Return formatted output or "No output produced."
        if output_parts:
            return "\n".join(output_parts)
        else:
            return "No output produced."
        
    except Exception as e:
        return f"Error: executing Python file: {e}"

