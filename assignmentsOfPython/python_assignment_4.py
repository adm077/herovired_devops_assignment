
'''
●       Implement a Python script called backup.py that takes a source directory and a destination directory as command-line arguments.

●       The script should copy all files from the source directory to the destination directory.

●       Before copying, check if the destination directory already contains a file with the same name. If so, append a timestamp to the file name to ensure uniqueness.

●       Handle errors gracefully, such as when the source directory or destination directory does not exist.

Sample Command:

python backup.py /path/to/source /path/to/destination

By running the script with the appropriate source and destination directories, it should create backups of the files in the source directory, ensuring unique file names in the destination directory.
'''



import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, destination_dir):
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print("Source directory does not exist.")
        return

    # Check if destination directory exists, create if not
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Get list of files in the source directory
    files = os.listdir(source_dir)

    for file in files:
        source_path = os.path.join(source_dir, file)
        destination_path = os.path.join(destination_dir, file)

        # Check if the destination file already exists
        if os.path.exists(destination_path):
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            file_name, file_extension = os.path.splitext(file)
            new_file_name = f"{file_name}_{timestamp}{file_extension}"
            destination_path = os.path.join(destination_dir, new_file_name)

        # Copy the file to the destination directory
        try:
            shutil.copy2(source_path, destination_path)
            print(f"Copied {file} to {destination_path}")
        except Exception as e:
            print(f"Error copying {file}: {str(e)}")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Please provide source and destination directories as command-line arguments.")
    else:
        source_directory = sys.argv[1]
        destination_directory = sys.argv[2]
        backup_files(source_directory, destination_directory)