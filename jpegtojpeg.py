"""
Here's what the code does step-by-step:

The code imports the 'os' module, which provides a way of interacting with the file system.
The folder_path variable holds the path to the folder containing the files. You will need to replace this variable's value with your folder path.
The for loop iterates over each file in the folder specified by folder_path.
If a file ends with the extension ".JPG", the code enters the if statement.
Inside the if statement, the code gets the old_file_path by joining the folder_path and the filename together.
The new_filename variable is created by replacing the ".JPG" extension in the filename with ".jpeg".
The new_file_path variable is created by joining the folder_path and the new_filename together.
The os.rename() function is used to rename the file from old_file_path to new_file_path.
Finally, the code prints a message stating the original filename and the new filename.
Note: This code only changes the extension to lower case, but it does not modify the contents of the file. 
If you need to modify the contents of the file, you will need to use a different method.

"""
import os

folder_path = "/Users/rougeboy/Documents/repos/rougeboy.github.io/photography"  # replace with your folder path

for filename in os.listdir(folder_path):
    if filename.endswith(".JPG"):
        old_file_path = os.path.join(folder_path, filename)
        new_filename = filename.replace(".JPG", ".jpg")
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(old_file_path, new_file_path)
        print(f"Renamed {filename} to {new_filename}")
