import os

folder_path = "/Users/rougeboy/Documents/repos/Portfolio/jpeg-optimized"  # replace with your folder path
word_to_remove = "jpeg-optimizer_"

for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".JPG"):
        old_file_path = os.path.join(folder_path, filename)
        new_filename = filename.replace(word_to_remove, "")
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(old_file_path, new_file_path)
        print(f"Removed word {word_to_remove} from file {filename}. Renamed to {new_filename}")
