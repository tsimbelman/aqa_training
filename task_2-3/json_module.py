import json
import pprint

FILE_PATH = 'abonents.json'

def read_json(path):
    with open(path, mode='r') as json_file:
        data = json.load(json_file)
        json_file.close()
        return data


def data_base():
    data = read_json(FILE_PATH)
    return data

def pretty_print():
    pretty = pprint.pprint(data_base())


def main():
    data_base()
    pretty_print()


if __name__=='main':
    main()
