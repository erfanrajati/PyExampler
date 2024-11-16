import json 
from pyfiglet import Figlet
import random
import os
import sys

def get_resource_path(filename):
    """
    Get the absolute path to the resource (JSON file) in the same directory as the executable.
    """
    # Get the directory of the currently running script or executable
    base_path = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(__file__)
    return os.path.join(base_path, filename)

def read_json_file():
    # Get the absolute path to your JSON file
    json_path = get_resource_path('python_guide_examples.json')

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

file = read_json_file()

TOPICS = [t for t in file.keys()]
WELCMOE_MESSAGE = """
+-------------------------------------------------------------+
|  Welcome to PyExampler!                                     |
|  This is a program to assist you with your python teaching. |
|  Just choose items from the menu below                      |
|  and PyExampler will generate you cool examples             |
|  that you can use for your class!                           |
|                                                             |
|  - By Erfan Rajati                                           |
+-------------------------------------------------------------+
"""
GOODBYE_MESSAGE = open("goodbye_message.txt", 'r').read().split(',')


fig = Figlet(font='standard')

# To execute the correct shell command based on Operating System
os.system("cls" if os.name == 'nt' else "clear")

print(fig.renderText('PyExampler'))
print(WELCMOE_MESSAGE)

def main():
    while True:
        print("\nChoose from available topics (0 to exit, default 0):")
        for i in range(1, len(TOPICS)+1):
            print(f"{i}. {TOPICS[i-1]}")

        while True:
            try:
                userIn = input("\n>>> ")
                userIn = int(userIn)-1 if userIn else -1
                if userIn == -1 : return
                if TOPICS[userIn]: break
            except:
                print("Wrong input, type the number of the topic you want to see. (0 to exit)")

        for e in file[TOPICS[userIn]]:
            print()
            print(e)
            print()
            print("------------------------")

        while True:
            print()
            print("More examples? (yes/no, default no)")
            userIn = input(">>> ")
            userIn = userIn if userIn else "no"
            if userIn == "no":
                return
            elif userIn == "yes":
                os.system("cls" if os.name == 'nt' else "clear")
                print(fig.renderText('PyExampler'))
                break
            else:
                print("Wrong input!")
        
        
if __name__ == "__main__":
    main()
    os.system("cls" if os.name == 'nt' else "clear")
    print(fig.renderText('PyExampler'))
    input(F"\n{random.choice(GOODBYE_MESSAGE)}\n\n")

# pyinstaller --onefile --name PyExampler --workpath ./PyExampler_build/build --distpath ./PyExampler_build/dist --specpath ./PyExampler_build myscript.py
# pyinstaller --onefile --name PyExampler --add-data "C:\Users\Erfan\AppData\Local\Programs\Python\Python312\Lib\site-packages\pyfiglet\fonts;pyfiglet/fonts" --workpath ./PyExampler_build/build --distpath ./PyExampler_build/dist --specpath ./PyExampler_build main.py