#!/usr/bin/env python3
"""
Author : Daniel T Lee <daniel.ts.lee@gmail.com>
Date   : 2024-11-09
Purpose: Telephone
"""

import argparse
import os.path
#import sys
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='float',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    if (args.mutations < 0 or args.mutations > 1):
       parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    args.text = open(args.text, 'rt').read().rstrip() if os.path.isfile(args.text) else args.text

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    text = ''.join([' ' if c == ' ' else \
                    chr(random.randint(33, 126)) if random.random() < args.mutations else c for c in args.text])

    print(f'You said: "{args.text}"')
    print(f'I heard : "{text}"')

    count = 0
    for i in range(len(args.text)):
        if args.text[i] != text[i]:
            count += 1
    print(f'Percent different is {100*count/len(text)}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
