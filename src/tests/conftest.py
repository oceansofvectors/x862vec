from typing import Any
import pytest
import numpy as np
from torch import rand
from gensim.models import KeyedVectors


@pytest.fixture
def w2v_model():
    model = KeyedVectors.load("assets/x862vec.model", mmap="r")
    yield model
