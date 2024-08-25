from idiom_matcher import IdiomMatcher, Match
from utils.parser import get_explain, merge_explain
from utils.llm import get_prompt
from utils.decorator import log_func_info, retry_when_error
try:
    from local_llm import call_api
except:
    from llm import call_api

idiom_matcher = IdiomMatcher()

def insert_full_name_and_keyword(matches, name, full_name, keyword, full_keyword):
    for match in matches:
        if full_name and full_name != name:
            match.name = full_name
        if full_keyword and full_keyword != keyword:
            match.keyword = full_keyword

@log_func_info  
def get_homophone(name, keyword, is_strict):
    matches = idiom_matcher.match(name, keyword, is_strict)
    return matches

@log_func_info
@retry_when_error
def explain(match):
    prompt = get_prompt(match)
    res = call_api(prompt)
    explain, example = get_explain(res)
    explained_res = merge_explain(match, explain, example)
    return explained_res

def search(name, full_name, keyword, full_keyword, is_strict):
    matches = get_homophone(name, keyword, is_strict)
    insert_full_name_and_keyword(matches, name, full_name, keyword, full_keyword)
    return matches

def explain_homophone(idiom, homophone, name, keyword):
    match = Match(idiom=idiom, homophone=homophone, name=name, keyword=keyword)
    res = explain(match)
    return res
