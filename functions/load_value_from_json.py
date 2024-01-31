import json


def load_value_from_json(key):
    file_path = 'data.json'
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            return data.get(key)
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except json.JSONDecodeError:
        print(f"The file {file_path} is not a valid JSON file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None
