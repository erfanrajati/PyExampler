from classes import *
import json
import os
import sys

def get_resource_path(filename):
    """
    Get the absolute path to the resource (JSON file) in the same directory as the executable.
    """
    # Get the directory of the currently running script or executable
    base_path = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(__file__)
    return os.path.join(base_path, filename)

def read_json_file(filename):
    # Get the absolute path to your JSON file
    json_path = get_resource_path(filename)

    try:
        with open(json_path) as json_file:
            data = json.load(json_file)
            # print("JSON data successfully loaded.")
            return data
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_path}.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

GOODBYE_MESSAGE = open(
    get_resource_path("goodbye_message.txt"),
    'r'
).read().split('|')

WELCMOE_MESSAGE = """
+-------------------------------------------------------------+
|  Welcome to PyExampler!                                     |
|  This is a program to assist you with your python teaching. |
|  Just choose items from the menu below                      |
|  and PyExampler will generate you cool examples             |
|  that you can use for your class!                           |
|                                                             |
|  - By Erfan Rajati                                          |
+-------------------------------------------------------------+
"""

db:dict = read_json_file('python_guide_examples.json')

python = Language(name="Python", json_dict=db)



menu = MainMenu(language=python, goodbye_message=GOODBYE_MESSAGE)

menu.main_loop()
menu.goodbye()