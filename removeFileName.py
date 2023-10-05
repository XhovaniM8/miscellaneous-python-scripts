"""
This is a Python code that renames all JPEG files in a folder by removing a specific word from their filename.

Here is a step-by-step explanation of what the code does:

The code starts by importing the 'os' module, which provides a way of interacting with the file system.
The folder_path variable holds the path to the folder containing the JPEG files. You will need to replace this variable's value with your folder path.
The word_to_remove variable holds the string to be removed from the filename of each JPEG file in the folder.
The for loop iterates over each file in the folder specified by folder_path.
If a file ends with the extension ".jpg" or ".jpeg" or ".JPG", the code enters the if statement.
Inside the if statement, the code gets the old_file_path by joining the folder_path and the filename together.
The new_filename variable is created by replacing the word_to_remove string in the filename with an empty string.
The new_file_path variable is created by joining the folder_path and the new_filename together.
The os.rename() function is used to rename the file from old_file_path to new_file_path.
Finally, the code prints a message stating the word that was removed from the filename and the new filename.
In summary, this code renames all JPEG files in a folder by removing a specific word from their filename.
"""

import os

folder_path = ""  # replace with your folder path
word_to_remove = "jpeg-optimizer_"

for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".JPG"):
        old_file_path = os.path.join(folder_path, filename)
        new_filename = filename.replace(word_to_remove, "")
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(old_file_path, new_file_path)
        print(f"Removed word {word_to_remove} from file {filename}. Renamed to {new_filename}")


