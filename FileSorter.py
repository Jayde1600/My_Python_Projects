import os
import shutil

# Make sure to change the folder_path based on the files you want to sort
# This is for windows and your file path will be different to mine so find
# your file path.

folder_path = 'C:/Users/neome/Downloads'


def createFolder(folder_path, sub_folder):
    sub_folder_path = os.path.join(folder_path, sub_folder)
    if not os.path.exists(sub_folder_path):
        os.makedirs(sub_folder_path)
    return sub_folder_path


def sortingFiles(folder_path):
    for files in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, files)):
            extension = files.split('.')[-1].lower()
            if extension:
                sub_folder = f"{extension.upper()} Files"
                sub_folder_path = createFolder(folder_path, sub_folder)
                file_path = os.path.join(folder_path, files)
                create_loc = os.path.join(sub_folder, files)

                if not os.path.exists(create_loc):
                    shutil.move(file_path, sub_folder_path)
                    print(f"Moved {files} to -> {sub_folder}/")
                else:
                    print(f"Skipped: {files} already exists in {sub_folder}/")


sortingFiles(folder_path)
