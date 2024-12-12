#!/usr/bin/env python3
"""
Author : Daniel T Lee <daniel.ts.lee@gmail.com>
Date   : 2024-11-17
Purpose: Scramble the letters of words
"""

import argparse
import os.path
import random
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble the letters of words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input Text')

    parser.add_argument('-s',
                        '--seed',
                        help='Random Seed',
                        metavar='int',
                        type=int,
                        default=None)

    args =  parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read()

    return args


def scramble(word):
    if len(word) <= 3:
        return word
    
    middle = list(word[1:-1])
    random.shuffle(middle)

    return word[0] + ''.join(middle) + word[-1]


def test_scramble():
    """Test scramble"""

    state = random.getstate()
    random.seed(1)
    assert scramble("a") == "a"
    assert scramble("ab") == "ab"
    assert scramble("abc") == "abc"
    assert scramble("abcd") == "acbd"
    assert scramble("abcde") == "acbde"
    assert scramble("abcdef") == "aecbdf"
    assert scramble("abcde'f") == "abcd'ef"
    random.setstate(state)

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    splitter = re.compile('('                        # start capture group
                              '[a-zA-Z]'             # character class of lower and upper
                              '(?:'                  # start non-capture group
                                  '[a-zA-Z\']*'      # zero or more letters plus '
                                  '[a-zA-Z]'         # character class of letters
                              ')?'                   # optional
                          ')'                        # end capture group
                          )  
    for line in args.text.splitlines():
        print( ''.join(map(scramble, splitter.split(line))) )



# --------------------------------------------------
if __name__ == '__main__':
    main()
