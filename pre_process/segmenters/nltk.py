from nltk.tokenize import sent_tokenize
from pre_process.models import Segmenter


class NltkSegmenter(Segmenter):
    def __init__(self):
        super().__init__()

    def segment(self, text):
        """
        :param string text: document that needs to be segmented
        :return: list of string
        """
        return sent_tokenize(text)
