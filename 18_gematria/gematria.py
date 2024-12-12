#!/usr/bin/env python3
"""
Author : Daniel T Lee <daniel.ts.lee@gmail.com>
Date   : 2024-12-10
Purpose: Gematria
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def encode(line):
    sumsL = list(
                map(
                    lambda word: str(sum([ord(ch) for ch in word])),
                    re.split(' ', line)
                    )
                )
    # blank new line exception
    sumsL = [num if num != '0' else '' for num in sumsL]
    return ' '.join(sumsL)       


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    args.text = [re.sub('[^a-zA-Z0-9 \n]', '', line) for line in re.split('\n', args.text)]
    print('\n'.join(list(map(encode, args.text))))

# --------------------------------------------------
if __name__ == '__main__':
    main()
