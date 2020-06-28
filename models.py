import constants
import re


class Token:
    def __init__(self, content=None, doc_offset=None, sent_offset=None, metadata=None):
        """

        :param str content: token string
        :param (int, int) doc_offset: start and end offset of token on the document
        :param (int, int) sent_offset:  start and end offset of token on the sentence
        :param dict metadata: additional data
        """
        self.content = content
        self.doc_offset = doc_offset
        self.sent_offset = sent_offset
        self.processed_content = content
        self.metadata = {} if metadata is None else metadata

    def __str__(self):
        return self.content

    def doc_offset_add(self, amount):
        new_offset = tuple(i + amount for i in self.doc_offset)
        self.doc_offset = new_offset

    def get_node(self):
        """
        return node to use on lib networkx graph (our Dependency Graph)
        :return:
        """
        return self.content, self.doc_offset, self.sent_offset

    def is_pronoun(self):
        if 'pos_tag' in self.metadata and self.metadata['pos_tag'] in constants.PRONOUN_TAGS:
            return True
        else:
            return False

    def is_verb(self):
        if 'pos_tag' in self.metadata and self.metadata['pos_tag'] in constants.VERB_TAGS:
            return True
        else:
            return False

    def is_chemical_mention(self):
        if self.content.lower() in constants.CHEMICAL_MENTIONS:
            return True
        else:
            return False

    def is_disease_mention(self):
        if self.content.lower() in constants.DISEASE_MENTIONS:
            return True
        else:
            return False

    def is_stop_word(self):
        if self.content.lower() in constants.STOP_WORD:
            return True
        else:
            return False

    def is_symbol(self):
        if re.match(r'\W+', self.content, re.IGNORECASE):
            return True
        else:
            return False

    def is_number(self):
        if re.match(r'\d+([.,]\d+)?', self.content, re.IGNORECASE):
            return True
        else:
            return False


class Sentence:
    """
    :type type: int
    """
    def __init__(self, type=constants.SENTENCE_TYPE_GENERAL, content=None, doc_offset=None, tokens=None, metadata=None):
        """
        :param str type: SENTENCE_TYPE_GENERAL = 0 SENTENCE_TYPE_TITLE = 1 SENTENCE_TYPE_ABSTRACT = 2
        :param str content:
        :param (int, int) doc_offset: offset of sentence in the document
        :param list of Token tokens: list of Token contained in this sentence
        :param dict metadata:
        """
        self.type = type
        self.content = content
        self.doc_offset = doc_offset
        self.tokens = tokens
        self.metadata = {} if metadata is None else metadata

    def doc_offset_add(self, amount):
        """
        shift the sentence offset
        :param amount:
        :return:
        """
        new_offset = tuple(i + amount for i in self.doc_offset)
        self.doc_offset = new_offset

    def get_pronoun(self):
        """

        :return list of Token:
        """
        pronouns = []
        for tok in self.tokens:
            if tok.is_pronoun():
                pronouns.append(tok)

        return pronouns

    def get_chemical_mention(self):
        """

        :return list of Token:
        """
        chemicals = []

        for tok in self.tokens:
            if tok.is_chemical_mention():
                chemicals.append(tok)

        return chemicals

    def get_disease_mention(self):
        """

        :return list of Token:
        """
        diseases = []

        for tok in self.tokens:
            if tok.is_disease_mention():
                diseases.append(tok)

        return diseases


class Document:
    def __init__(self, id=None, content=None, sentences=None, metadata=None):
        """

        :param str id:
        :param str content:
        :param list of Sentence sentences:
        :param dict metadata:
        """
        self.id = id
        self.content = content
        self.sentences = sentences
        self.metadata = {} if metadata is None else metadata


class Entity:
    """
    :type tokens: list of Token.__name__
    """
    def __init__(self, type=constants.ENTITY_TYPE_GENERAL, tokens=None):
        """

        :param type:
        :param list of Token tokens:
        """
        self.type = type
        self.tokens = tokens
        self.content = self._make_content()

    def _make_content(self):
        if not self.tokens:
            return None

        content = ''
        cur_offset = self.tokens[0].sent_offset[0]
        for t in self.tokens:
            if t.sent_offset[0] != cur_offset:
                num_space = t.sent_offset[0] - cur_offset
                content += ' ' * num_space
                cur_offset += num_space

            content += t.content
            cur_offset += len(t.content)

        return content


class BioEntity(Entity):
    def __init__(self, type=constants.ENTITY_TYPE_GENERAL, tokens=None, ids=None):
        super(BioEntity, self).__init__(type, tokens)
        self.ids = {} if ids is None else ids


class Relation:
    def __init__(self, type=constants.RELATION_TYPE_GENERAL, entity1=None, entity2=None):
        self.type = type
        self.entity1 = entity1
        self.entity2 = entity2
