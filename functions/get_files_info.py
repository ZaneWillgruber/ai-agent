import os


def get_files_info(working_directory, directory="."):
    string = f"Result for '{directory}' directory:\n"
    # check we are in a directory that we are allowed in
    absolute_path = os.path.abspath(os.path.join(working_directory, directory))
    if not absolute_path.startswith(os.path.abspath(working_directory)):
        string += f'Error: Cannot list "{
            directory}" as it is outside the permitted working directory\n'
        return string

    # check it is a valid directory
    if not os.path.isdir(absolute_path):
        string += f'Error: "{directory}" is not a directory\n'
        return string

    # get contents
    contents = os.listdir(absolute_path)
    for item in contents:
        working_file = os.path.join(absolute_path, item)
        # file_size={os.path.getsize(item)} is_dir={os.path.isdir(item)}\n"
        string += f"- {item}: file_size={os.path.getsize(working_file)} bytes, is_dir={
            os.path.isdir(working_file)}\n"

    return string
