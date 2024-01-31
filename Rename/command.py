import os
import pathlib

folder_location = "D:\\codeing\\python2\\Maze\\changeName\\pic"
def change_name(location):
    i = 1
    for file in os.listdir(location):
        file_path = os.path.join(location, file)

        file_name,file_type = os.path.splitext(file)
        if file_type == '':
            new_location = os.path.join(location, file_name)
            change_name(new_location)
        elif file_type.lower() in ('.jpg', '.png'):
            new_name = f"pic{i:03d}{file_type}"
            new_path = os.path.join(location, new_name)
            os.rename(file_path, new_path)
            i += 1
        
change_name(folder_location)