from src.model.corpus import Corpus


def test_build_corpus():
    corpus = Corpus()
    corpus.build_corpus(max_binaries=5)
