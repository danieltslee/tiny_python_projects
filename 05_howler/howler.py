#!/usr/bin/env python3
"""
Author : Daniel T Lee <daniel.ts.lee@gmail.com>
Date   : 2024-11-08
Purpose: Writes in uppercase
"""

import argparse
import os.path

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Writes in uppercase',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='A positional argument')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        default='')

    return parser.parse_args()



# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text_arg = args.text
    str_arg = args.outfile

    # Test if arg is a file
    text_arg = open(text_arg).read().rstrip() if os.path.isfile(text_arg) else text_arg
    text_arg = text_arg.upper()
    """if (os.path.isfile(text_arg)):
        fh = open(text_arg, 'r')
        inputText = fh.read().upper()
        fh.close()
    else:
        inputText = text_arg.upper()"""

    # If output flag is on
    open(str_arg, 'wt').write(text_arg + '\n') if str_arg else print(text_arg)
    """if (str_arg):
        fh = open(str_arg, 'wt')
        fh.write(text_arg)
        fh.close()
    else: # if no output flag
        print(text_arg)"""
   

# --------------------------------------------------
if __name__ == '__main__':
    main()
