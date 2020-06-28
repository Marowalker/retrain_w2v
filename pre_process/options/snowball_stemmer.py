from nltk.stem.snowball import SnowballStemmer as Snowball
from pre_process.models import Option


class SnowballStemmer(Option):
    def __init__(self):
        super().__init__()
        self.stemmer = Snowball("english")

    def process(self, doc_obj):
        for s in doc_obj.sentences:
            for t in s.tokens:
                t.processed_content = self.stemmer.stem(t.processed_content)
