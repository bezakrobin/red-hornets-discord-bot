import json


def load_data(file_name='../data.json'):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
