import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    # check that we have access
    absolute_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not absolute_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    # check it is a valid file
    if not os.path.isfile(absolute_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    with open(absolute_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) >= MAX_CHARS:
            file_content_string += f'\n[...File "{
                file_path}" truncated at 10000 characters]'

    return file_content_string
