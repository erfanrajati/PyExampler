import shutil
import os
import sys

def move_to_program_files(source_file, folder_name="MyApp"):
    # Path to "C:\Program Files"
    program_files = "C:\\Program Files (x86)"
    
    # Create a subdirectory for your app
    destination_folder = os.path.join(program_files, folder_name)
    
    # Check if the destination folder exists, create it if it doesn't
    if not os.path.exists(destination_folder):
        try:
            os.makedirs(destination_folder)
            print(f"Created directory: {destination_folder}")
        except PermissionError:
            print("Error: You need administrator privileges to create this folder.")
            sys.exit(1)
    
    # Move the file to the Program Files folder
    try:
        shutil.move(source_file, destination_folder)
        print(f"Moved {source_file} to {destination_folder}")
    except PermissionError:
        print("Error: You need administrator privileges to move files to this folder.")
    except FileNotFoundError:
        print(f"Error: Source file {source_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage
source_file = os.getcwd() + "<FILE NAME HERE>"
move_to_program_files(source_file, folder_name="MyAppFolder")
