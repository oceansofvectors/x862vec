# Generate a word2vec model
import os

from gensim.models import KeyedVectors
from gensim.models import Word2Vec
from gensim.models.word2vec import PathLineSentences


class Instruction2Vec:
    def __init__(self, vector_size=5, window=128, workers=4, retrain=False):
        self.vector_size = vector_size
        self.window = window
        self.workers = workers
        self.retrain = retrain
        if not os.path.exists('assets/x862vec.model') or retrain:
            print("Training model...")
            self.model = Word2Vec(sentences=PathLineSentences('assets/corpus'), vector_size=self.vector_size,
                                  window=self.window, min_count=1,
                                  workers=self.workers)
            self.model.save("assets/x862vec.model")
        else:
            self.model = KeyedVectors.load("assets/x862vec.model", mmap="r")
