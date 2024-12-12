#!/usr/bin/env python3
"""
Author : Daniel T Lee <daniel.ts.lee@gmail.com>
Date   : 2024-11-08
Purpose: String Translation
"""

import argparse
import os.path

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='String Translation',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        metavar='input',
                        help='input string or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='Vowel to replace',
                        metavar='str',
                        type=str,
                        choices=['a','e','i','o','u'],
                        default='a')
    
    args = parser.parse_args()
    if os.path.isfile(args.input):
        args.input = open(args.input).read().rstrip()
        
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    src = 'aeiouAEIOU'
    tgt = args.vowel.lower()*5 + args.vowel.upper()*5
    table = args.input.maketrans(src, tgt)
    print(args.input.translate(table))


# --------------------------------------------------
if __name__ == '__main__':
    main()
