import os
import shutil

# Path to your folder
path = r"C:/Users/shawn/OneDrive/Desktop/python tutorial/" # best to create a new folder and try it as an exxample
file_name = os.listdir(path)


folder_mapping = {
    "images": [".png", ".jpg", ".jpeg", ".gif"],
    "documents": [".doc", ".docx", ".pdf", ".txt"],
    "spreadsheets": [".xls", ".xlsx", ".csv"],
    "presentations": [".ppt", ".pptx"],
}


for folder in folder_mapping.keys():
    folder_path = os.path.join(path, f"{folder} files")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created: {folder_path}")
    else:
        print(f"Already exists: {folder_path}")


for file in file_name:
    file_path = os.path.join(path, file)  
    file_ext = os.path.splitext(file)[1].lower() 

    moved = False 

    for folder, extensions in folder_mapping.items():
        if file_ext in extensions:  
            dest_folder = os.path.join(path, f"{folder} files")
            dest_path = os.path.join(dest_folder, file)
            if not os.path.exists(dest_path):  
                shutil.move(file_path, dest_path)
                print(f"Moved: {file} to {folder} files")
                moved = True
                break  # Exit the loop once the file is moved

    if not moved:
        print(f"File {file} does not match any known category or has already been moved.")


import hashlib


def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def is_duplicate(file_path, folder):
    # Check all files in the folder for duplicates
    for root, _, files in os.walk(folder):
        for file in files:
            existing_file_path = os.path.join(root, file)
            if calculate_md5(file_path) == calculate_md5(existing_file_path):
                return True
    return False


# Example usage in the loop
for file in file_name:
    file_path = os.path.join(path, file)
    file_ext = os.path.splitext(file)[1].lower()

    moved = False
    for folder, extensions in folder_mapping.items():
        if file_ext in extensions:
            dest_folder = os.path.join(path, f"{folder} files")
            if not is_duplicate(file_path, dest_folder):
                shutil.move(file_path, os.path.join(dest_folder, file))
                print(f"Moved: {file} to {folder} files")
            else:
                print(f"Duplicate found: {file} not moved.")
            moved = True
            break

