#!/usr/bin/env python3
"""
Author : Daniel T Lee <daniel.ts.lee@gmail.com>
Date   : 2024-12-09
Purpose: Mad Libs
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad Libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt')
                        )
    
    parser.add_argument('-i',
                        '--inputs',
                        help='inputs (for testing)',
                        type=str,
                        metavar='str',
                        nargs='*',
                        default=[])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.file.read().rstrip()
    placeholders = re.findall('(<([^<>]+)>)', text)

    if not placeholders:
        #print(f'"{args.file.name}" has no placeholders.', file=sys.stderr)
        sys.exit(f'"{args.file.name}" has no placeholders.')
    

    if len(args.inputs) < len(placeholders):
        for i, val in enumerate(placeholders):
            if i < len(args.inputs):
                continue
            junc = 'an' if val[1][0] in 'aeiou' else 'an'
            lib = input(f'Give me {junc} {val[1]}: ')
            args.inputs.append(lib)

    args.inputs.reverse()
    for i in range(len(args.inputs)):
        currWord = args.inputs.pop()
        text = re.sub(f'{placeholders[i][0]}?', currWord, text, count=1)
        

    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
