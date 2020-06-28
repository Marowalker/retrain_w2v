class DataManager:
    def __init__(self):
        pass


class CDRDataManager(DataManager):
    @staticmethod
    def parse_documents(raw_documents):
        titles = {}
        abstracts = {}

        for i in raw_documents:
            if raw_documents[i].get('t'):
                titles[i] = raw_documents[i]['t']
            if raw_documents[i].get('a'):
                abstracts[i] = raw_documents[i]['a']

        return titles, abstracts

    @staticmethod
    def merge_documents(titles, abstracts):
        """
        :param list titles: list of Document objects
        :param list abstracts: list of Document objects
        :return: list of Document objects
        """
        documents = []
        for t_doc in titles:
            for a_doc in abstracts:
                if t_doc.id == a_doc.id:
                    add_amount = len(t_doc.content) + 1
                    # update sentences' offset in document
                    for s in a_doc.sentences:
                        s.doc_offset_add(add_amount)
                        # update tokens' offset in sentence
                        for t in s.tokens:
                            t.doc_offset_add(add_amount)

                    t_doc.content += ' ' + a_doc.content
                    t_doc.sentences += a_doc.sentences

                    abstracts.remove(a_doc)
                    break
            # whatever happens, append t_doc
            documents.append(t_doc)

        # maybe there are abstract documents that do not have corresponding title documents
        documents += abstracts

        return documents
