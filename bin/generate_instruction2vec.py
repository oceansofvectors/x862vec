#! /usr/bin/env python3

import argparse
from src.model.instruction2vec import Instruction2Vec

parser = argparse.ArgumentParser(description='Build the corpus.')
parser.add_argument('--vector_size', dest='vector_size', default=5,
                    help='Generate the assembly corpus.', type=int, required=False)
parser.add_argument('--window', dest='window', default=128,
                    help='Generate the assembly corpus.', type=int, required=False)
parser.add_argument('--workers', dest='workers', default=4,
                    help='Generate the assembly corpus.', type=int, required=False)
parser.add_argument('--retrain', dest='retrain', default=False,
                    help='Generate the assembly corpus.', type=bool, required=False)

args = parser.parse_args()

if __name__ == "__main__":
    i2vec = Instruction2Vec(vector_size=int(args.vector_size),
                            window=int(args.window),
                            workers=int(args.workers),
                            retrain=bool(args.retrain))
