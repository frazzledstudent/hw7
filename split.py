#!/usr/bin/env python
"""Shuffles and splits a file into training, development, and test sets.
"""

import argparse
import random


def main(args: argparse.Namespace) -> None:
    data = []
    with open(args.input, "r") as text:
        for line in text:
            data.append(line.rstrip())
    random.seed(args.seed)
    random.shuffle(data)
    ten_pct = len(data) // 10
    train_set = ten_pct * 8
    dev_set = ten_pct * 9
    with open(args.train, "w") as new:
        for line in data[:train_set]:
            new.write(line + "\n")
    with open(args.dev, "w") as new:
        for line in data[train_set:dev_set]:
            new.write(line + "\n")
    with open(args.test, "w") as new:
        for line in data[dev_set:]:
            new.write(line + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="path to input file")
    parser.add_argument("train", help="path to training output file")
    parser.add_argument("dev", help="path to development output file")
    parser.add_argument("test", help="path to test output file")
    parser.add_argument("--seed", type=int, required=True, help="random seed")
    main(parser.parse_args())