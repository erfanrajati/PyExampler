from functions import *
        
if __name__ == "__main__":
    db:dict = read_json_file('python_guide_examples.json')

    python = Language(name="Python", json_dict=db)

    menu = MainMenu(
        language=python, 
        welcome_message= WELCMOE_MESSAGE, 
        goodbye_message=GOODBYE_MESSAGE
    )

    menu.main_loop()
    menu.goodbye()


# I don't know what to do with these! very important though :)
# pyinstaller --onefile --name PyExampler --workpath ./PyExampler_build/build --distpath ./PyExampler_build/dist --specpath ./PyExampler_build myscript.py
# pyinstaller --onefile --name PyExampler --add-data "C:\Users\Erfan\AppData\Local\Programs\Python\Python312\Lib\site-packages\pyfiglet\fonts;pyfiglet/fonts" --workpath ./PyExampler_build/build --distpath ./PyExampler_build/dist --specpath ./PyExampler_build main.py
