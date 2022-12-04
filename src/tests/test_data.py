from src.data.dataset import AssemblyDataset
import pandas as pd
from torch import Tensor


def test_dataset(w2v_model):
    path = "assets/data"
    df = pd.read_csv("assets/train.csv")
    assembly_files = df["filename"]
    labels = df["label"]
    dataset = AssemblyDataset(
        path=path,
        assembly_function_files=assembly_files,
        labels=labels,
        model=w2v_model,
        vector_size=16,
    )
    assert len(dataset)
    assert len(dataset) > 0
    assert dataset[0]
    print(dataset[0])
    print(dataset[0]['x'].shape)
    assert isinstance(dataset[0]["x"], Tensor)
    assert isinstance(dataset[0]["y"], Tensor)
