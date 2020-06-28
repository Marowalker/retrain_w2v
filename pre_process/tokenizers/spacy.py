import re
from module.spacy import Spacy
from pre_process.models import Tokenizer


class SpacyTokenizer(Tokenizer):
    def __init__(self):
        super().__init__()

    def tokenize(self, sent):
        tokens = SpacyTokenizer.parse(sent)
        return [(t.string.strip(), t.tag_) for t in tokens]

    @staticmethod
    def parse(sent):
        # sent = re.sub(r'/', ' / ', sent)
        # sent = re.sub(r']', '] ', sent)
        sent = re.sub(r'\s{2,}', ' ', sent)

        tokens = Spacy.parse(sent)
        return tokens
