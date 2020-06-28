from gensim.models import Word2Vec
import numpy as np

model = Word2Vec.load('w2v_retrain.bin')
words = list(model.wv.vocab)
embeddings = np.zeros([len(words), 300])
i = 0
for word in sorted(words, key=str.lower):
    embeddings[i] = model[word]
    i += 1
np.savez_compressed('w2v_retrain.npz', embeddings=embeddings)
