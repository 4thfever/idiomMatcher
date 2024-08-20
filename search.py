import random

from idiom_matcher import IdiomMatcher
from utils.parser import get_output, get_explain, merge_explain
from utils.llm import get_prompt
from logger import logger
try:
    from local_llm import call_api
except:
    from llm import call_api

idiom_matcher = IdiomMatcher()

def get_homophone(name, keyword, is_strict):
    logger.info(f"name: {name}, keyword: {keyword}, is_strict: {is_strict}")
    matches = idiom_matcher.match(name, keyword, is_strict)
    logger.info(f"matches: {matches}")
    return matches

def insert_full_name_and_keyword(matches, name, full_name, keyword, full_keyword):
    for match in matches:
        if full_name and full_name != name:
            match.human_cn = full_name
        if full_keyword and full_keyword != keyword:
            match.key_word_cn = full_keyword

def explain(match):
    prompt = get_prompt(match)
    res = call_api(prompt)
    explain = get_explain(res)
    explained_res = merge_explain(match, explain)
    logger.info(f"explained_res: {explained_res}")
    return explained_res

def search(name, full_name, keyword, full_keyword, is_strict):
    matches = get_homophone(name, keyword, is_strict)
    if len(matches) == 0:
        return "无匹配结果", "无匹配结果"
    output = get_output(matches)
    insert_full_name_and_keyword(matches, name, full_name, keyword, full_keyword)
    match = random.choice(matches)
    explained_res = explain(match)
    return output, explained_res

if __name__ == "__main__":
    humans = "志峰"
    key_words = "吃饭"
    print(search(humans, key_words))