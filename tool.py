import json 

def format_json(file):
    with open(file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    with open('formatted.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)

def remove_abbreviations(file):
    with open(file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    for idiom in json_data:
        del idiom['abbreviation']
    with open('idiom.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)

def main():
    # format_json('idiom.json')
    remove_abbreviations('idiom.json')

if __name__ == "__main__":
    main()