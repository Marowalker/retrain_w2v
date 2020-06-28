import re

from pre_process.models import Tokenizer


class SimpleTokenizer(Tokenizer):
    def __init__(self):
        super().__init__()

    def tokenize(self, sent):
        # delete '-'
        sent = re.sub(r'-', ' ', sent)

        # space out marks
        marks = ['.', ',', ';', '?', '(', ')', '/', '"', ':']
        for m in marks:
            sent = sent.replace(m, " {} ".format(m))
        sent = re.sub(r'\s+', ' ', sent.strip())

        return sent.split()