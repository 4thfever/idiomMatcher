import ast



def get_output(matches):
    matches = [_get_output(match) for match in matches]
    output = "\n".join(matches)
    return output

def _get_output(match):
    idiom = match.idiom
    homophone = match.homophone
    return f"{idiom}   ==>   {homophone}"

def get_explain(res):
    res = ast.literal_eval(res)
    understanding = res["理解"]
    return understanding

def merge_explain(match, understanding):
    return f"""
    原始成语：{match.idiom}
    谐音成语：{match.homophone}
    主人公：{match.human_cn}
    关键字：{match.key_word_cn}
    理解：{understanding}
    """