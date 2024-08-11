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
    原始成语：当仁不让。
    谐音成语：铛仁不让。
    主人公：叮铛
    关键字：仁慈
    理解：叮铛非常仁慈，不让于任何人。

    原始成语：'巧取豪夺'
    谐音成语：'桥取豪惰'
    主人公：'心桥'
    关键字：'懒惰'
    心桥非常懒惰，总是喜欢从别人那里轻易地获取好处。
    '''
    在上面，我告知你一些用了谐音技巧的中文成语，请帮助我巧妙地理解这些谐音成语。
    原始成语：'{match.idiom}'
    谐音成语：'{match.homophone}'
    主人公：'{match.human_cn}'
    关键字：'{match.key_word_cn}'
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