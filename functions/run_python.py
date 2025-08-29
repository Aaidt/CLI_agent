import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    target_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_directory = os.path.abspath(working_directory)

    if not target_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(target_path):
        return f'Error: File "{file_path}" not found.'

    file_name = os.path.dirname(file_path)
    if not file_name.endsWith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    result = subprocess.run(["uv", "run", target_path], capture_output=True, text=True, timeout=30, shell=False)
    print(f"Output: {result.stdout}")
    print(f"Error: {result.stderr}")
