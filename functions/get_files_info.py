import os

def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.join(working_directory, directory)
        abs_full_path = os.path.abspath(full_path)
        work_dir_abs_path = os.path.abspath(working_directory)

        if not abs_full_path.startswith(work_dir_abs_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
        if not os.path.isdir(abs_full_path):
            print(abs_full_path)
            return f'Error: "{directory}" is not a directory'
    
        dir_list = os.listdir(full_path)
        item_string_list = []
        for item in dir_list:
            joined_path = os.path.join(full_path, item)
            item_string_list.append(f'- {item}: file_size={os.path.getsize(joined_path)} bytes, is_dir={os.path.isdir(joined_path)}')
        return "\n".join(item_string_list)
    except:
        return f"Error: library function command"
