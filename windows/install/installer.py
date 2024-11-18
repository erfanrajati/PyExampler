import shutil
import os
import sys

def move_to_program_files(source_file, folder_name="PyExampler"):
    program_files = "C:\\Program Files (x86)"
    
    destination_folder = os.path.join(program_files, folder_name)
    
    if not os.path.exists(destination_folder):
        try:
            os.makedirs(destination_folder)
            print(f"Created directory: {destination_folder}")
        except PermissionError:
            print("Error: You need administrator privileges to create this folder.")
            sys.exit(1)
    
    try:
        shutil.move(source_file, destination_folder)
        print(f"Moved {source_file} to {destination_folder}")
    except PermissionError:
        print("Error: You need administrator privileges to move files to this folder.")
    except FileNotFoundError:
        print(f"Error: Source file {source_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_files = [
    os.getcwd() + "\\PyExampler.exe",
    os.getcwd() + "\\python_guide_examples.json",
    os.getcwd() + "\\addpath.exe"
]

for file in source_files:
    move_to_program_files(file, folder_name="PyExampler")

# Doesn't work currectly
# os.system('"c:\\Program Files (x86)\\addpath.exe"')
