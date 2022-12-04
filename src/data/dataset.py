import os

import numpy as np
import pandas as pd
import pytorch_lightning as pl
import torch
from sklearn.model_selection import train_test_split
from torch.utils.data import Dataset, DataLoader

from src.preprocess.encoder import Encoder


class AssemblyLightDataset(pl.LightningDataModule):
    def __init__(self, w2v_model, vector_size, path, matrix_size, batch_size=64):
        super().__init__()
        self.batch_size = batch_size
        self.matrix_size = matrix_size
        self.path = path
        self.w2v_model = w2v_model
        self.vector_size = vector_size

    def setup(self, stage=None):
        df = pd.read_csv("assets/train.csv")
        xtrain, xval, ytrain, yval = train_test_split(
            df["filename"].values, df.label.values, test_size=0.1
        )
        self.train_dataset = AssemblyDataset(self.path, xtrain, ytrain, self.w2v_model, self.vector_size)
        self.validation_dataset = AssemblyDataset(
            self.path, xval, yval, self.w2v_model, self.vector_size
        )

    def train_dataloader(self):
        train_loader = DataLoader(
            self.train_dataset, batch_size=self.batch_size, shuffle=True
        )
        return train_loader

    def val_dataloader(self):
        valid_loader = DataLoader(
            self.validation_dataset, batch_size=self.batch_size, shuffle=False
        )
        return valid_loader


class AssemblyDataset(Dataset):
    def __init__(self, path, assembly_function_files, labels, model, vector_size):
        self.assembly_function_files = assembly_function_files
        self.labels = labels
        self.path = path
        self.encoder = Encoder(model, vector_size)

    def __len__(self):
        return len(self.assembly_function_files)

    def __getitem__(self, item):
        assembly_function_data = open(
            os.path.join(self.path, self.assembly_function_files[item]), "r"
        ).readlines()

        labels = self.labels[item]
        matrix = self.encoder.encode(assembly_function_data)
        matrix = matrix.astype(np.float64)

        return {
            "x": torch.tensor(matrix, dtype=torch.float),
            "y": torch.tensor(labels, dtype=torch.long),
        }
