from pyfiglet import Figlet
import os
import random

class Example:
    def __init__(self, value:str):
        self.value = value


class Topic:
    def __init__(self, name, list):
        self.name = name
        self.examples = [Example(item) for item in list]


class Language: # for later use when support for a programming language became dynamic.
    def __init__(self, name, json_dict: dict):
        self.name = name
        self.topics = [Topic(key, list) for key, list in json_dict.items()]

    def show_topics(self) -> list[str]:
        result = []
        for t in self.topics:
            result.append(t.name)
        return result
    
    def show_examples(self, topic_index:int) -> list[str]:
        result = []
        for e in self.topics[topic_index].examples:
            result.append(e.value)
        return result
    

class MainMenu:
    def __init__(self, language: Language, welcome_message, goodbye_message):
        fig = Figlet(font='standard')
        self.title = fig.renderText("PyExampler")
        self.message = welcome_message
        self.goodbye_message = goodbye_message
        self.language = language
        self.topics = self.language.show_topics()

    def main_loop(self):
        while True:
            # Show welcome message and list of topics
            os.system("cls" if os.name == 'nt' else "clear")
            print(self.title)
            print(self.message)
            print("\nChoose from available topics (q to exit):")
            for i, t in enumerate(self.topics):
                print(f"{i}. {t}")
            
            # Get and handle user choice
            while True: 
                userIn = input("\n>>> ")
                if userIn == 'q': return
                try:
                    userIn = int(userIn)
                    if self.topics[userIn]: break
                except:
                    print("Wrong input, type the number of the topic you want to see. (q to exit)")
            
            # Show the Examples to the user
            for e in self.language.show_examples(userIn):
                print()
                print(e)
                print()
                print("------------------------")
            
            # Check if user wants to continue
            while True:
                print()
                print("More examples? (yes/no, default no)")
                userIn = input(">>> ")
                userIn = userIn if userIn else "no"
                if userIn == "no":
                    return
                elif userIn == "yes":
                    break
                else:
                    print("Wrong input!", end=' ')
    
    def goodbye(self):
        os.system("cls" if os.name == 'nt' else "clear")
        print(self.title)
        input(f"\n{random.choice(self.goodbye_message)}\n\n")

            