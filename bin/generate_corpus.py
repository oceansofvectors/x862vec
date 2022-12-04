#! /usr/bin/env python3

import argparse
from src.model.corpus import Corpus

parser = argparse.ArgumentParser(description='Build the corpus.')
parser.add_argument('--max_binaries', dest='max_binaries', default=5,
                    help='Generate the assembly corpus.', type=int)

args = parser.parse_args()

if __name__ == "__main__":
    c = Corpus(max_binaries=int(args.max_binaries))
    c.build_corpus()
