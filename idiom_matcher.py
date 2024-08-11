import re
import json
from copy import deepcopy
from dataclasses import dataclass

from utils import (
    chinese_to_pinyin,
    remove_accents,
    replace_char_in_string,
    split_pinyin
)

@dataclass
class Match:
    idiom: str
    pinyin: str
    homophone: str
    human_cn: str
    key_word_cn: str

class IdiomMatcher:
    def __init__(self, file_path='idiom.json'):
        """
        初始化 IdiomMatcher，并从 JSON 文件中加载成语。
        """
        self.idioms = self.load_idioms(file_path)

    def load_idioms(self, file_path):
        """
        从 JSON 文件中加载成语，并处理其拼音表示。
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            idioms = json.load(file)
        
        for idiom in idioms:
            idiom["pinyin"] = split_pinyin(idiom["pinyin"])
        return idioms


    def find_pinyin_matches(self, idiom_pinyin, human_pinyin, key_word_pinyin):
        """
        查找与成语拼音匹配的人名和关键词拼音及其索引。
        """
        human_match_idx, key_word_match_idx = None, None

        for idx, pinyin in enumerate(idiom_pinyin):
            if pinyin in human_pinyin:
                human_match_idx = (human_pinyin.index(pinyin), idx)
            if pinyin in key_word_pinyin:
                key_word_match_idx = (key_word_pinyin.index(pinyin), idx)
            
            # 如果人名和关键词拼音都有匹配，并且不是同一个位置
            if human_match_idx and key_word_match_idx:
                if human_match_idx[1] != key_word_match_idx[1]:
                    return human_match_idx, key_word_match_idx
        return None, None

    def generate_idiom_with_replacements(self, idiom, human_cn, key_word_cn, human_idx, keyword_idx):
        """
        生成一个新的成语字符串，将字符替换为对应的人名和关键词字符。
        """
        idiom_homophone = deepcopy(idiom["word"])
        idiom_homophone = replace_char_in_string(idiom_homophone, human_idx[1], human_cn[human_idx[0]])
        idiom_homophone = replace_char_in_string(idiom_homophone, keyword_idx[1], key_word_cn[keyword_idx[0]])
        return idiom_homophone

    def match_idioms(self, human_cn, key_word_cn, strict=True):
        """
        根据提供的中文字符及其拼音表示匹配成语。
        """
        matching_idioms = []
        if strict:
            human_pinyin = chinese_to_pinyin(human_cn, style="tone")
            key_word_pinyin = chinese_to_pinyin(key_word_cn, style="tone")
        else:
            human_pinyin = chinese_to_pinyin(human_cn)
            key_word_pinyin = chinese_to_pinyin(key_word_cn)

        for idiom in self.idioms:
            idiom_pinyin = idiom["pinyin"]
            if not strict:
                idiom_pinyin = remove_accents(idiom_pinyin)
            human_match, keyword_match = self.find_pinyin_matches(idiom_pinyin, human_pinyin, key_word_pinyin)

            if human_match and keyword_match:
                idiom_homophone = self.generate_idiom_with_replacements(
                    idiom, human_cn, key_word_cn, human_match, keyword_match
                )
                match = Match(
                    idiom=idiom["word"],
                    pinyin=idiom["pinyin"],
                    homophone=idiom_homophone,
                    human_cn=human_cn,
                    key_word_cn=key_word_cn
                )
                matching_idioms.append(match)
        return matching_idioms

    def match(self, human_cn, key_word_cn, strict=True):
        """
        为每对人名和关键词中文短语匹配成语。
        """
        matching_idioms = self.match_idioms(human_cn, key_word_cn, strict)
        return matching_idioms
