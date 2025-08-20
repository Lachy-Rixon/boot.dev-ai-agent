import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        abs_file_path = os.path.abspath(file_path)
        abs_work_dir = os.path.abspath(working_directory)
        joint_path = os.path.join(abs_work_dir, file_path)
        if not joint_path.startswith(abs_work_dir):
            return f"Error: Cannot read {file_path} as it is outside the permitted working directory"

        if not os.path.isfile(joint_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    
        with open(joint_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)


        if len(file_content_string) == MAX_CHARS:
            file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_content_string
    except:
        return f"Error: Couldn't get file content"