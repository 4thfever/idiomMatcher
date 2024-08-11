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