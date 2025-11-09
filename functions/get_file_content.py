import os
MAX_CHARS = 10000
from google.genai import types


def get_file_content(working_directory , file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile( target_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
   
    try:
        with open(target_file_path, "r") as f:
            content = f.read()  # read once

            if len(content) > MAX_CHARS:
                file_content_string = content[:MAX_CHARS] + f"\n[...File \"{target_file_path}\" truncated at 10000 characters]"
            else:
                file_content_string = content
    except Exception as e:
        return f"Error: {str(e)}"
    
    return file_content_string

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the files content.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="this is the path of the file",
            ),
        },
    ),
)

    



        
        
    

