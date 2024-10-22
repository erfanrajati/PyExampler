import json

def reformat_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        
        print("JSON file has been reformatted successfully!")
    
    except Exception as e:
        print(f"An error occurred: {e}")

reformat_json('python_guide_examples.json')
