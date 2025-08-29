import os
from config import MAX_CHARS


def get_files_content(working_directory, file_path):
    target_directory = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_dir = os.path.abspath(working_directory)

    if not target_directory.startswith(abs_working_dir):
        f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_directory):
        f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(target_directory, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if os.path.getsize(target_directory) > MAX_CHARS:
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_content_string
    except Exception as e:
        return f"Error reading file: '{file_path}': '{e}'"
