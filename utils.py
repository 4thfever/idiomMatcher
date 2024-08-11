import re
from unidecode import unidecode
from collections.abc import MutableSequence

from pypinyin import lazy_pinyin, Style


def chinese_to_pinyin(chinese_word, style=None):
    """
    将中文字符转换为拼音表示。
    """
    if style == "tone":
        return lazy_pinyin(chinese_word, style=Style.TONE)

    return lazy_pinyin(chinese_word)

def remove_accents(pinyin_with_accents):
    """
    使用 unidecode 去掉拼音中的音调。
    """
    if isinstance(pinyin_with_accents, MutableSequence):
        return [unidecode(pinyin) for pinyin in pinyin_with_accents]
    return unidecode(pinyin_with_accents)

def split_pinyin(s):
    """
    拆分拼音字符串。空格或者中英文逗号分隔。
    """
    parts = re.split(r"[,，\s]", s)
    parts = [part.strip() for part in parts if part.strip()]
    return parts

def replace_char_in_string(s, index, new_char):
    """
    替换字符串中指定索引位置的字符。
    """
    return s[:index] + new_char + s[index + 1:]

def get_prompt(match):
    return f"""
    '''
    主人公：叮铛
    关键字：仁慈
    原始成语：当仁不让。
    谐音成语：铛仁不让。
    理解：叮铛非常仁慈，不让于任何人。

    主人公：桥
    关键字：懒惰
    原始成语：巧取豪夺
    谐音成语：桥取豪惰
    理解：桥非常懒惰，总是喜欢从别人那里轻易地获取好处。

    主人公：牛马
    关键字：题目
    原始成语：马失前蹄
    谐音成语：马失前题
    理解：牛马在做题目时，前面的题目做错了。

    主人公：谭警官
    关键字：诈唬
    原始成语：谈虎色变
    谐音成语：谭唬色变
    理解：谭警官在面对诈唬时，神情发生了变化。
    '''
    在上面，我告知你一些用了谐音技巧的中文成语，请帮助我巧妙地理解这些谐音成语。注意：整个理解必须合乎逻辑且有意义。
    主人公：{match.human_cn}
    关键字：{match.key_word_cn}
    原始成语：{match.idiom}
    谐音成语：{match.homophone}
    理解：
    """

def get_output(matches):
    matches = [_get_output(match) for match in matches]
    output = "\n\n".join(matches)
    return output

def _get_output(match):
    idiom = match.idiom
    homophone = match.homophone
    return f"原始成语：{idiom}\n谐音成语：{homophone}"

def get_explain(match, understanding):
    return f"""
    原始成语：{match.idiom}
    谐音成语：{match.homophone}
    主人公：{match.human_cn}
    关键字：{match.key_word_cn}
    理解：{understanding}
    """