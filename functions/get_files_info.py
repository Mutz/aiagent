import os

def get_files_info(working_directory, directory="."):
    try:
        # Create the full path by joining working_directory with directory
        full_path = os.path.join(working_directory, directory)
        
        # Get absolute paths to properly compare boundaries
        abs_working_dir = os.path.abspath(working_directory)
        abs_full_path = os.path.abspath(full_path)
        
        # Validate that the directory stays within working_directory boundaries
        if not abs_full_path.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        # Check if the path exists and is a directory
        if not os.path.exists(abs_full_path):
            return f'Error: "{directory}" does not exist'
        
        if not os.path.isdir(abs_full_path):
            return f'Error: "{directory}" is not a directory'
        
        # Get directory contents
        entries = os.listdir(abs_full_path)
        entries.sort()  # Sort for consistent output
        
        # Build the result string
        result_lines = []
        for entry in entries:
            entry_path = os.path.join(abs_full_path, entry)
            file_size = os.path.getsize(entry_path)
            is_dir = os.path.isdir(entry_path)
            result_lines.append(f"- {entry}: file_size={file_size} bytes, is_dir={is_dir}")
        
        return "\n".join(result_lines)
        
    except Exception as e:
        return f"Error: {str(e)}"
