import spacy as sp
from spacy.symbols import ORTH, LEMMA
from utils import Timer


class Spacy:
    nlp = None

    @staticmethod
    def load_spacy():
        t = Timer()
        t.start('Load SpaCy', verbal=True)
        Spacy.nlp = sp.load('en_core_web_lg')
        t.stop()
        Spacy.nlp.tokenizer.add_special_case(u'+/-', [{ORTH: u'+/-', LEMMA: u'+/-'}])
        Spacy.nlp.tokenizer.add_special_case("mg.", [{ORTH: "mg.", LEMMA: "mg."}])
        Spacy.nlp.tokenizer.add_special_case("mg/kg", [{ORTH: "mg/kg", LEMMA: "mg/kg"}])
        Spacy.nlp.tokenizer.add_special_case("Gm.", [{ORTH: "Gm.", LEMMA: "Gm."}])
        Spacy.nlp.tokenizer.add_special_case("i.c.", [{ORTH: "i.c.", LEMMA: "i.c."}])
        Spacy.nlp.tokenizer.add_special_case("i.p.", [{ORTH: "i.p.", LEMMA: "i.p."}])
        Spacy.nlp.tokenizer.add_special_case("s.c.", [{ORTH: "s.c.", LEMMA: "s.c."}])
        Spacy.nlp.tokenizer.add_special_case("p.o.", [{ORTH: "p.o.", LEMMA: "p.o."}])
        Spacy.nlp.tokenizer.add_special_case("i.c.v.", [{ORTH: "i.c.v.", LEMMA: "i.c.v."}])
        Spacy.nlp.tokenizer.add_special_case("e.g.", [{ORTH: "e.g.", LEMMA: "e.g."}])
        Spacy.nlp.tokenizer.add_special_case("i.v.", [{ORTH: "i.v.", LEMMA: "i.v."}])
        Spacy.nlp.tokenizer.add_special_case("t.d.s.", [{ORTH: "t.d.s.", LEMMA: "t.d.s."}])
        Spacy.nlp.tokenizer.add_special_case("t.i.d.", [{ORTH: "t.i.d.", LEMMA: "t.i.d."}])
        Spacy.nlp.tokenizer.add_special_case("b.i.d.", [{ORTH: "b.i.d.", LEMMA: "b.i.d."}])
        Spacy.nlp.tokenizer.add_special_case("i.m.", [{ORTH: "i.m.", LEMMA: "i.m."}])
        Spacy.nlp.tokenizer.add_special_case("i.e.", [{ORTH: "i.e.", LEMMA: "i.e."}])
        Spacy.nlp.tokenizer.add_special_case("medications.", [{ORTH: "medications.", LEMMA: "medications."}])
        Spacy.nlp.tokenizer.add_special_case("mEq.", [{ORTH: "mEq.", LEMMA: "mEq."}])
        Spacy.nlp.tokenizer.add_special_case("a.m.", [{ORTH: "a.m.", LEMMA: "a.m."}])
        Spacy.nlp.tokenizer.add_special_case("p.m.", [{ORTH: "p.m.", LEMMA: "p.m."}])
        Spacy.nlp.tokenizer.add_special_case("M.S.", [{ORTH: "M.S.", LEMMA: "M.S."}])
        Spacy.nlp.tokenizer.add_special_case("ng.", [{ORTH: "ng.", LEMMA: "ng."}])
        Spacy.nlp.tokenizer.add_special_case("ml.", [{ORTH: "ml.", LEMMA: "ml."}])

    @staticmethod
    def get_spacy_model():
        if Spacy.nlp is None:
            Spacy.load_spacy()

        return Spacy.nlp

    @staticmethod
    def parse(text):
        if Spacy.nlp is None:
            Spacy.load_spacy()

        return Spacy.nlp(text)

    @staticmethod
    def get_heads(text):
        if Spacy.nlp is None:
            Spacy.load_spacy()

        doc = Spacy.nlp(text)
        res = []
        for chunk in doc.noun_chunks:
            res.append(chunk.root.text)
        return res
