import random

from idiom_matcher import IdiomMatcher
from utils.parser import get_output, get_explain, get_understanding
from utils.llm import get_prompt
try:
    from local_llm import call_api
except:
    from llm import call_api

idiom_matcher = IdiomMatcher()

def search(humans, key_words, is_strict):
    matches = idiom_matcher.match(humans, key_words, is_strict)

    if len(matches) ==  0:
        return "无匹配结果", "无匹配结果"
    output = get_output(matches)
    match = random.choice(matches)
    prompt = get_prompt(match)
    res = call_api(prompt)
    understanding = get_understanding(res)
    explain = get_explain(match, understanding)
    return output, explain

if __name__ == "__main__":
    humans = "志峰"
    key_words = "吃饭"
    print(search(humans, key_words))