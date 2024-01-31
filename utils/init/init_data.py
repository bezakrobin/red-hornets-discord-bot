import json
import os


async def init_data():
    if not os.path.exists('data.json'):
        with open('data.json', 'w') as file:
            initial_content = {}
            json.dump(initial_content, file)
            print("data.json created with initial content.")
    else:
        print("data.json already exists.")
