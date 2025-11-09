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
    description="Write into a file , accepts a content argument. Overwrites a new file, if it does not exists, it creates a path and a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="This is the path to write into",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="the content to be written into",
            ),
        },
    ),
)
    
    



        
