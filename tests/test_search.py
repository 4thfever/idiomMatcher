from pytest import fixture

from idiom_matcher import IdiomMatcher

@fixture
def idiom_matcher():
    return IdiomMatcher()

def test_match(idiom_matcher):
    humans = ["王"]
    keywords = ["洋"]
    stricts = [True]
    outputs = ["亡羊补牢"]
    for human, keyword, strict, output in zip(humans, keywords, stricts, outputs):
        matches = idiom_matcher.match(human, keyword, strict)
        assert any(match.idiom == output for match in matches)