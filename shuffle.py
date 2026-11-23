#!/usr/bin/env python
"""Shuffles the lines of a file."""

import argparse
import random


def main(args: argparse.Namespace) -> None:
    data = []
    with open(args.input, "r") as text:
        for line in text:
            data.append(line.rstrip())
    random.seed(args.seed)
    random.shuffle(data)
    with open(args.output, "w") as new:
        for line in data:
            new.write(line + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="shuffles")
    parser.add_argument("input", help="path to input file")
    parser.add_argument("output", help="path to output file")
    parser.add_argument(
        "--seed", type=int, required=True, help="random seed"
    )
    main(parser.parse_args())