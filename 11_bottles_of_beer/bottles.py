#!/usr/bin/env python3
"""
Author : Daniel T Lee <daniel.ts.lee@gmail.com>
Date   : 2024-11-09
Purpose: Bottles of beer song
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='int',
                        type=int,
                        default=10)

    args =  parser.parse_args()

    if (args.num <= 0):
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


def beerSong(num):
    song = """\
{NUM} bottle{BNUM} of beer on the wall,
{NUM} bottle{BNUM} of beer,
Take one down, pass it around,\n""".format(NUM=num,
                                                NUMM1=num-1,
                                                BNUM='s' if num != 1 else '')
    if (num > 1):
        tag = "{NUM} bottle{BNUM} of beer on the wall!\n".format(NUM=num-1,
                                                    BNUM='' if num-1 == 1 else 's')
    else:
        tag = "No more bottles of beer on the wall!"
        print(song + tag)
        return
    print(song + tag)
    beerSong(num - 1)

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    beerSong(args.num)


# --------------------------------------------------
if __name__ == '__main__':
    main()
