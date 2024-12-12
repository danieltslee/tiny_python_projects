#!/usr/bin/env python3
"""
Author : Daniel T Lee <daniel.ts.lee@gmail.com>
Date   : 2024-11-08
Purpose: Get word count
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Get word count',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        nargs='*',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=[sys.stdin])
                        # default is a list becuase nargs='*' causes a list as return

    return parser.parse_args()


def sortByName(io):
    return io.name


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    
    args = get_args()
    
    sorted(args.file, key=sortByName)

    totalLines = 0
    totalWords = 0
    totalChar = 0
    for fh in args.file:
        numLines = 0
        wordCnt = 0
        charCnt = 0
        for line in fh:
            numLines += 1
            wordCnt += len(line.split())
            charCnt += len(line)
        totalLines += numLines
        totalWords += wordCnt
        totalChar += charCnt

        print(f'{numLines:8}{wordCnt:8}{charCnt:8} {fh.name}')
    if (len(args.file) > 1):
        print(f'{totalLines:8}{totalWords:8}{totalChar:8} total')
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
    