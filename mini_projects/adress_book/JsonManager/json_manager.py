import json

def convert_json_to_dict(txt_json):
    return json.loads(txt_json)

def read_from_json_convert_to_dict(file_path):
    try:
        with open(file_path, 'r') as file_reader:
            dict_json = json.load(file_reader)
        return dict_json
    
    except Exception as e:
        print(f'Dogodila se pograška: {e}')

def dump_json_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file_writer:
            json.dump(content, file_writer, indent = 4)

    except Exception as e:
        print(f'Dogodila se pogreška {e}')