import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path, args=[]):
    target_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_directory = os.path.abspath(working_directory)

    if not target_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(target_path):
        return f'Error: File "{file_path}" not found.'

    if not target_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(["uv", "run", target_path], capture_output=True, text=True, timeout=30, shell=False)
        print(f"STDOUT: {result.stdout}")
        print(f"STDERR: {result.stderr}")
        if result.returncode == 0:
            return f"Process exited with code {result.returncode}"
        if not result:
            print("No output produced.")
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)
