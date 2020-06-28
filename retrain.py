from gensim.models import Word2Vec
from sent_from_cdr import get_sents as cdr
from sent_from_pmc import get_sents as pmc
from utils import Timer

# set up params
all_sents = cdr() + pmc()

# train word2vec
timer = Timer()
timer.start("Training word2vec file...")
model = Word2Vec(all_sents, size=300, sg=1)
model.save('w2v_retrained_bc5_and_pmc.bin')
timer.stop()
