import os
import re
from collections import defaultdict
import constants
import pre_process
from pre_process import opt as pre_opt

input_path = 'data/pmc_data/'

parts = ['==== Body\n', '==== Refs\n']

print('Start')

pre_config = {
    pre_opt.SEGMENTER_KEY: pre_opt.SimpleSegmenter(),
    pre_opt.TOKENIZER_KEY: pre_opt.SimpleTokenizer()
}


def get_sent_dict():
    pmc_dict = defaultdict()
    idx = 0
    dirs = os.listdir(input_path)
    for d in dirs:
        print("Processing folder: " + d)
        for folder in os.listdir(os.path.join(input_path, d)):
            for filename in os.listdir(os.path.join(os.path.join(input_path, d), folder)):
                # print(idx)
                file = open(os.path.join(os.path.join(os.path.join(input_path, d), folder), filename),
                            encoding='latin1')
                lines = file.readlines()
                if parts[0] not in lines or parts[1] not in lines:
                    file.close()
                else:
                    body = [l.strip() for l in lines[lines.index(parts[0]) + 1: lines.index(parts[1]) - 1]]
                    pmc_sents = []
                    for line in body:
                        sent = re.sub(r'Fig\..*\. ', '', line)
                        match = re.match(r'.*\.$', sent)
                        if match:
                            # print(match.group())
                            pmc_sents.append(match.group())
                    pmc_dict[idx] = ' '.join(pmc_sents)
                    idx += 1
    return pmc_dict


def get_sents():
    sents = get_sent_dict()
    all_sents = []
    documents = pre_process.process(sents, pre_config, constants.SENTENCE_TYPE_ABSTRACT)
    for doc in documents:
        for sentence in doc.sentences:
            token_list = [t.content for t in sentence.tokens]
            all_sents.append(token_list)
    return all_sents
