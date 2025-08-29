import os


def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    abs_full_path = os.path.abspath(full_path)
    abs_working_directory = os.path.abspath(working_directory)

    if not os.path.isdir(abs_full_path):
        return f'Error: "{abs_full_path}" is not a directory'

    if not abs_full_path.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    try:
        files_list = []
        for file in os.listdir(abs_full_path):
            relative_full_path = os.path.join(abs_full_path, file)
            file_size = os.path.getsize(relative_full_path)
            is_dir = os.path.isdir(relative_full_path)
            files_list.append(f"- {file}: file_size:{file_size}, is_dir={is_dir}")

    except Exception as e:
        return f"Error listing files files: {e}"

    return "\n".join(files_list)


# print(get_files_info("calculator", "pkg"))
