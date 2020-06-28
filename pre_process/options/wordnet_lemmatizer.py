from nltk import WordNetLemmatizer as WordNet
from pre_process.models import Option


class WordNetLemmatizer(Option):
    def __init__(self):
        super().__init__()
        self.lemmer = WordNet()

    def process(self, doc_obj):
        for s in doc_obj.sentences:
            for t in s.tokens:
                t.processed_content = self.lemmer.lemmatize(t.processed_content)
