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
    explain = res["理解"]
    example = res["例句"]
    return explain, example

def merge_explain(match, explain, example):
    return f"""
    原始成语：{match.idiom}
    谐音成语：{match.homophone}
    主人公：{match.name}
    关键字：{match.keyword}
    理解：{explain}
    例句：{example}
    """