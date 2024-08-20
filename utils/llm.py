def get_prompt(match):
    return f"""
    '''
    主人公：叮铛
    关键字：仁慈
    原始成语：当仁不让。
    谐音成语：铛仁不让。
    分析：可以这么理解，成语里面以铛为主体，之后的内容说明了他的仁慈程度。
    理解：叮铛非常仁慈，不让于任何人。

    主人公：桥
    关键字：懒惰
    原始成语：巧取豪夺
    谐音成语：桥取豪惰
    分析：桥是整个成语的主体，取和夺是动作，说明了桥的行为。
    理解：桥非常懒惰，总是喜欢从别人那里轻易地获取好处。

    主人公：牛马
    关键字：题目
    原始成语：马失前蹄
    谐音成语：马失前题
    分析：牛马是整个成语的主体，失是动作，前题是目标。
    理解：牛马在做题目时，前面的题目做错了。

    主人公：谭警官
    关键字：诈唬
    原始成语：谈虎色变
    谐音成语：谭唬色变
    分析：谭警官是一个警察，他或许经常会遇到欺骗。在遭遇到了诈唬的时候，他的神情发生了变化。
    理解：谭警官在面对诈唬时，神情发生了变化。
    '''
    在上面，我告知你一些用了谐音技巧的中文成语，请帮助我巧妙地理解这些谐音成语。
    注意：
    1. 整个理解必须合乎逻辑且有意义。‘理解’中的主角必须为‘主人公’。
    2. 必须合理的结合原始成语的意义，以及原始成语的文本，不能忽略。
    主人公：{match.human_cn}
    关键字：{match.key_word_cn}
    原始成语：{match.idiom}
    谐音成语：{match.homophone}
    
    Return in json format:
    {{
        "分析": "",
        "理解": ""
    }}
    """