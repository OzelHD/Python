# 1️⃣ Write a script that renames all .txt files in a folder to file_0.txt, file_1.txt, etc.
# 2️⃣ Ensure it handles errors (e.g., folder doesn’t exist).

import os

folder_path = "./testfolder/"  
try:

    files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]

    for i, file in enumerate(files):
        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, f"file_{i}.txt")
        os.rename(old_path, new_path)

    print("Files renamed successfully!")

except FileNotFoundError:
    print(f"Error: The folder '{folder_path}' or one of the files was not found.")
except PermissionError:
    print(f"Error: Insufficient permissions to rename files in '{folder_path}'.")
except FileExistsError:
    print("Error: A file with the same name already exists.")
except OSError as e:
    print(f"An OS error occurred: {e}")