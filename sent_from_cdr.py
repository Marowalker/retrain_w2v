import os
from readers import BioCreativeReader
from data_managers import CDRDataManager as data_manager
from pre_process import opt as pre_opt
import pre_process
import constants


input_path = "data/cdr_data"

datasets = ['train', 'dev', 'test']

print('Start')

pre_config = {
    pre_opt.SEGMENTER_KEY: pre_opt.SimpleSegmenter(),
    pre_opt.TOKENIZER_KEY: pre_opt.SimpleTokenizer()
}


def get_sents():
    all_sents = []

    # create list of tokens in sentences
    for dataset in datasets:
        print('Process dataset: ' + dataset)
        reader = BioCreativeReader(os.path.join(input_path, "cdr_" + dataset + ".txt"))
        raw_documents = reader.read()

        title_docs, abstract_docs = data_manager.parse_documents(raw_documents)

        title_doc_objs = pre_process.process(title_docs, pre_config, constants.SENTENCE_TYPE_TITLE)
        abs_doc_objs = pre_process.process(abstract_docs, pre_config, constants.SENTENCE_TYPE_ABSTRACT)
        documents = data_manager.merge_documents(title_doc_objs, abs_doc_objs)

        for doc in documents:
            for sentence in doc.sentences:
                token_list = [t.content for t in sentence.tokens]
                all_sents.append(token_list)
    return all_sents
