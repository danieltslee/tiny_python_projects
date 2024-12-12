#!/usr/bin/env python3
"""
Author : Daniel T Lee <daniel.ts.lee@gmail.com>
Date   : 2024-11-07
Purpose: Choose the Article
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Choose the Article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='The thing we see')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    vowel = 'aeiou'
    if (word[0].lower() in vowel):
        itl = 'an'
    else:
        itl = 'a'
    print('Ahoy, Captain, {ITL} {WORD} off the larboard bow!'.format(ITL=itl, WORD=word))


# --------------------------------------------------
if __name__ == '__main__':
    main()
