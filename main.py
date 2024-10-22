import json 
from pyfiglet import Figlet

file = json.load(open("python_guide_examples.json"))

TOPICS = [t for t in file.keys()]
WELCMOE_MESSAGE = """
+-------------------------------------------------------------+
|  Welcome to PyExampler!                                     |
|  This is a program to assist you with your python teaching. |
|  Just choose items from the menu below                      |
|  and PyExampler will generate you cool examples             |
|  that you can use for your class!                           |
|                                                             |
|  - By ErfanRajati                                           |
+-------------------------------------------------------------+
"""


fig = Figlet(font='standard')

print(fig.renderText('PyExampler'))
print(WELCMOE_MESSAGE)




def main():
    while True:
        print("\nAvailable Topics:")
        for i in range(1, len(TOPICS)+1):
            print(f"{i}. {TOPICS[i-1]}")

        while True:
            userIn = input("\n>>> ")

            if userIn not in file.keys():
                print("Wrong input, type the topic you want to see.")
            else: break

        for e in file[userIn]:
            print()
            print(e)
            print()
            print("------------------------")

        while True:
            print()
            print("More examples? (yes/no)")
            userIn = input(">>> ")
            if userIn == "no":
                break
            elif userIn == "yes":
                continue
            else:
                print("Wrong input!")
        
        
if __name__ == "__main__":
    main()