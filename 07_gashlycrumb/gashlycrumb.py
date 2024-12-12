#!/usr/bin/env python3
"""
Author : Daniel T Lee <daniel.ts.lee@gmail.com>
Date   : 2024-11-08
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letters',
                        metavar='letters',
                        nargs='+',
                        help='Starting Letter')

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    table = {line[0].lower() : line.rstrip() for line in args.file}

    for letter in args.letters:
        """if letter.lower() not in table.keys():
            print(f'I do not know "{letter}".')
            continue
        print(table.get(letter.lower(), letter))"""

        #print(table.get(letter.lower(), letter)) if letter.lower() in table.keys() else print(f'I do not know "{letter}".')

        print(table.get(letter.lower(), f'I do not know "{letter}".'))
    
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
