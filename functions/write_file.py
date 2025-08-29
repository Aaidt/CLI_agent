import os


def write_file(working_directory, file_path, content):
    target_path = os.path.abspath(os.path.join(working_directory, file_path))
    try:
        file_path_exists = os.path.exists(target_path)
        if not file_path_exists:
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
    except Exception as e:
        return f"Error in creating '{target_path}': '{e}'"

    abs_working_directory = os.path.abspath(working_directory)
    if not target_path.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        with open(target_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error writing to: '{file_path}': '{e}'"
