import os


def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    abs_full_path = os.path.abspath(full_path)
    abs_working_directory = os.path.abspath(working_directory)

    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'

    if not abs_full_path.startswith(abs_working_directory + os.sep) and abs_full_path != abs_working_directory:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    files_list = []
    for file in os.path.listdir(abs_full_path):
        file_size = os.path.getsize(file)
        is_dir = os.path.isdir(file)
        files_list.append(f"{file}: file_size:{file_size}, is_dir={is_dir}")

    return abs_full_path
