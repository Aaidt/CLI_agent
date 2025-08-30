import os
from google.genai import types


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
            return "\n".join(files_list)
    except Exception as e:
        return f"Error listing files files: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
# print(get_files_info("calculator", "pkg"))
