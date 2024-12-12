#!/usr/bin/env python3
"""
Author : Daniel T Lee <daniel.ts.lee@gmail.com>
Date   : 2024-11-08
Purpose: Encode to US telephone
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Encode to US telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        metavar='str',
                        help='A positional argument')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    number = args.input

    # Create encoder dict
    defaultNum = [str(x) for x in list(range(0,10))]
    usEncode = list(map(lambda x : str(x), [5,9,8,7,6,0,4,3,2,1,5]))
    encoder = dict(zip(defaultNum, usEncode))

    # encode number
    number = ''.join(encoder.get(x) if x in encoder else x for x in number)
    print(f'{number}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
