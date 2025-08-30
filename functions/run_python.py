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
    description="Runs the python file passed through the file_path along with the arguements.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file that is to be executed.",
            ),
            "args": types.Schema(
                type=types.Types.LIST,
                description="The arguements to be passed while executing the file."
            )
        },
    ),
)
