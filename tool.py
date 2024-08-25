import json 

from funcs import search, explain

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

def loop_example():
    from tqdm import tqdm
    from pathlib import Path
    from video.examples import EXAMPLES

    output_path = Path('video/example_output')
    LIMIT = 25
    for example in tqdm(EXAMPLES):
        outputs = []
        file_name = output_path / f"{example.name} + {example.keyword}.txt"
        ress = search(example.name, example.full_name, example.keyword, example.full_keyword, True)
        if len(ress) < LIMIT:
            new_ress = search(example.name, example.full_name, example.keyword, example.full_keyword, False)
            ress.extend(new_ress)
        ress = ress[:LIMIT]
        for res in ress:
            outputs.append(explain(res))
        # save as json
        string = "\n\n".join(outputs)
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(string)
        
def main():
    # format_json('idiom.json')
    # remove_abbreviations('idiom.json')
    loop_example()

if __name__ == "__main__":
    main()