import re
from module.spacy import Spacy
from pre_process.models import Segmenter


class SpacySegmenter(Segmenter):
    def __init__(self):
        super().__init__()

    @staticmethod
    def __fix_segmentation(raw_sentences):
        new_sentences = []
        cur_sent = raw_sentences[0]
        i = 1
        while i < len(raw_sentences):
            if cur_sent[-1] == '.':
                new_sentences.append(cur_sent)
                cur_sent = raw_sentences[i]
            else:
                cur_sent += " " + raw_sentences[i]
            i += 1
        new_sentences.append(cur_sent)
        return new_sentences

    def segment(self, text):
        """
        :param string text: document that needs to be segmented
        :return: list of string
        """
        # remove (ABSTRACT TRUNCATED AT 250 WORDS)
        text = re.sub('\(ABSTRACT TRUNCATED AT 250 WORDS\)', '', text)
        # parsed = Spacy.parse(text)
        # return self.__fix_segmentation([str(sent) for sent in parsed.sents])

        ret = [text]
        while True:
            count = len(ret)
            new_ret = []
            for t in ret:
                parsed = Spacy.parse(t)
                new_ret.extend([str(sent) for sent in parsed.sents])
            new_count = len(new_ret)

            if count == new_count:
                break

            ret = new_ret

        return ret
