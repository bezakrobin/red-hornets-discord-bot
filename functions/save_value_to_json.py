import json


def save_value_to_json(key, value):
    file_path = 'data.json'
    data = {}
    try:
        try:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            print(f"No existing file found. A new file will be created at {file_path}.")
        except json.JSONDecodeError:
            print(f"The file {file_path} is not a valid JSON file and will be overwritten.")
        data[key] = value
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    except Exception as e:
        print(f"An error occurred while writing to the JSON file: {e}")
