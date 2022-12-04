from src.preprocess.normalizer import Normalizer
from src.preprocess.binary import Binary

def test_normalize_assembly_file():
    binary = Binary(filepath='/usr/bin/bash')
    normalizer = Normalizer()
    normalized_assembly = normalizer.normalize_assembly(binary.get_function_assembly('array_shift'))
    assert isinstance(normalized_assembly, list)