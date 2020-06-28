import re
from pre_process.models import Segmenter


class SimpleSegmenter(Segmenter):
    def __init__(self):
        super().__init__()

    def segment(self, text):
        if text == "":
            return []
        sents = re.split(r'[.?]+\s', text.strip('.'))
        return sents
