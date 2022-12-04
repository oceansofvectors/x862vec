from src.preprocess.binary import Binary

def test_binary_data():
    binary = Binary(filepath='/usr/bin/bash')
    data = binary.assembly()
    assert isinstance(data, str)


def test_binary_get_function_data():
    binary = Binary(filepath='/usr/bin/bash')
    data = binary.get_function_assembly(func_name='array_shift')
    print(data)
    assert isinstance(data, str)