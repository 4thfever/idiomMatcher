from utils import split_pinyin
from idiom_matcher import IdiomMatcher

def test_split_pinyin():
    pinyins = split_pinyin("yǐ quán wéi yú")
    assert pinyins == ["yǐ", "quán", "wéi", "yú"]

def test_add_comma():
    # pinyins = ["yǐ", "quán", "móu", "sī"]
    # word = "以权谋私"
    # output = IdiomMatcher.add_comma_to_pinyin(word, pinyins)
    # assert output == ["yǐ", "quán", "móu", "sī"]

    # pinyins = ["bīng", "cáng", "wǔ", "kù", "mǎ", "rù", "huà", "shān"]
    # word = "兵藏武库，马入华山"
    # output = IdiomMatcher.add_comma_to_pinyin(word, pinyins)
    # assert output == ["bīng", "cáng", "wǔ", "kù", "，", "mǎ", "rù", "huà", "shān"]
    pinyins = [
        ["yǐ", "quán", "móu", "sī"],
        ["bīng", "cáng", "wǔ", "kù", "mǎ", "rù", "huà", "shān"]
    ]
    words = ["以权谋私", "兵藏武库，马入华山"]
    outputs = [
        ["yǐ", "quán", "móu", "sī"],
        ["bīng", "cáng", "wǔ", "kù", "，", "mǎ", "rù", "huà", "shān"]
    ]
    for pinyin, word, output in zip(pinyins, words, outputs):
        assert IdiomMatcher.add_comma_to_pinyin(word, pinyin) == output
