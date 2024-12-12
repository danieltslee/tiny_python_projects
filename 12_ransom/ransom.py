#!/usr/bin/env python3
"""
Author : Daniel T Lee <daniel.ts.lee@gmail.com>
Date   : 2024-11-12
Purpose: Ransom Note
"""

import argparse
import os.path
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='A positional argument')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='str',
                        type=str,
                        default=None)
    
    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text, 'rt').read().rstrip()

    return args

# --------------------------------------------------
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    # Method 6: map
    ransom = map(choose, args.text)
    print(''.join(ransom))


# --------------------------------------------------
def choose(char):
    """Randomly choose an upper or lowercase letter to return"""

    return char.upper() if random.choice([0, 1]) else char.lower()


# --------------------------------------------------
def test_choose():
    """Test choose"""

    state = random.getstate()
    random.seed(1)
    assert choose('a') == 'a'
    assert choose('b') == 'b'
    assert choose('c') == 'C'
    assert choose('d') == 'd'
    random.setstate(state)

# --------------------------------------------------
if __name__ == '__main__':
    main()
