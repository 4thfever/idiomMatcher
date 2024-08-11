import random

from idiom_matcher import IdiomMatcher
from utils import get_prompt, get_output
from llm import call_api
from local_llm import call_api

idiom_matcher = IdiomMatcher()

def search(humans, key_words, is_strict):
    ress = idiom_matcher.match(humans, key_words, is_strict)

    if len(ress) ==  0:
        return "无匹配结果"
    
    res = random.choice(ress)
    idiom, _, idiom_xieyin, human, key_word = res
    prompt = get_prompt(human, key_word, idiom, idiom_xieyin)
    understanding = call_api(prompt)
    output = get_output(human, key_word, idiom, idiom_xieyin, understanding)
    return output 

if __name__ == "__main__":
    humans = "志峰"
    key_words = "吃饭"
    print(search(humans, key_words))