import json 

def format_json(file):
    with open(file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    # save into file with indent
    with open('formatted.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)

def main():
    format_json('idiom.json')

if __name__ == "__main__":
    main()