import numpy as np


class Encoder:
    def __init__(self, model, vector_size):
        self.model = model
        self.vector_size = vector_size

    def encode(self, data):
        # data = normalize_assembly(data)
        vectors = list()
        sentence_vectors = list()
        for sentence in data:
            words = sentence.strip().split(" ")
            size = len(words)
            padding = self.vector_size - size
            for word in words:
                vector = self.model.wv[word]
                vectors.append(vector)
            for _ in range(padding):
                vectors.append(np.zeros(16))
            sentence_vector = np.concatenate(vectors)
            sentence_vectors.append(sentence_vector)
            vectors = list()
        matrix = np.stack(sentence_vectors)
        return matrix
