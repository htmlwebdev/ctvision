import os

def rename_files_and_folders(directory):
    """
    Rename all files and folders in the given directory, replacing 'oxpin' with 'ctv'
    
    Args:
        directory (str): Path to the directory where renaming should occur
    """
    # Walk through directory
    for root, dirs, files in os.walk(directory, topdown=False):
        # Rename files first
        for file_name in files:
            if 'oxpin' in file_name:
                old_path = os.path.join(root, file_name)
                new_name = file_name.replace('oxpin', 'ctv')
                new_path = os.path.join(root, new_name)
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed file: {file_name} -> {new_name}")
                except OSError as e:
                    print(f"Error renaming {file_name}: {e}")

        # Then rename directories
        for dir_name in dirs:
            if 'oxpin' in dir_name:
                old_path = os.path.join(root, dir_name)
                new_name = dir_name.replace('oxpin', 'ctv')
                new_path = os.path.join(root, new_name)
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed directory: {dir_name} -> {new_name}")
                except OSError as e:
                    print(f"Error renaming {dir_name}: {e}")

# Example usage
if __name__ == "__main__":
    directory_path = "." # Current directory. Change this to your target directory path
    rename_files_and_folders(directory_path)