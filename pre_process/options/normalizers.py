import re
from pre_process.models import Option


class NumericNormalizer(Option):
    def __init__(self, replace='0'):
        super().__init__()
        self.replace = replace

    def process(self, doc_obj):
        for s in doc_obj.sentences:
            for t in s.tokens:
                temp = re.sub(r'[\d]+', self.replace, t.processed_content)
                temp = re.sub(r'0+', self.replace, temp)
                temp = re.sub(r'0.0', self.replace, temp)

                temp = re.sub(r'-', ' ', temp)
                temp = re.sub(r'\s+', ' ', temp)

                t.processed_content = temp
