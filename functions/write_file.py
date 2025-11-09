import os
from google.genai import types

def write_f(file_path, content):
    try:
        with open(file_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error : {str(e)}"


def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    dir_name = os.path.dirname(target_file_path)
    
    
    os.makedirs(dir_name , exist_ok=True)
    return write_f(target_file_path , content)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write into a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="to write into a file, an ECHO into a file",
            ),
        },
    ),
)
    
    



        
