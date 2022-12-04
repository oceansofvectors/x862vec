from src.model.instruction2vec import Instruction2Vec


def test_instruction2vec_model():
    instruction2vec = Instruction2Vec()
    print(instruction2vec.model.wv['push'])