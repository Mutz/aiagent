import os
import pathlib

def write_file(working_directory, file_path, content):
    """
    Write content to a file, ensuring the file is within the working directory.
    
    Args:
        working_directory (str): The permitted working directory
        file_path (str): Path to the file to write
        content (str): Content to write to the file
    
    Returns:
        str: Success message or error message
    """
    try:
        # Convert paths to absolute paths and resolve any symbolic links
        working_dir_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.abspath(file_path)
        
        # Check if the file path is within the working directory
        try:
            # Use pathlib to check if file_path is relative to working_directory
            pathlib.Path(file_path_abs).relative_to(working_dir_abs)
        except ValueError:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        # Create the directory structure if it doesn't exist
        os.makedirs(os.path.dirname(file_path_abs), exist_ok=True)
        
        # Write the content to the file
        with open(file_path_abs, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except OSError as e:
        return f'Error: Failed to write to "{file_path}": {str(e)}'
    except Exception as e:
        return f'Error: Unexpected error while writing to "{file_path}": {str(e)}'