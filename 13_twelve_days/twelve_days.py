#!/usr/bin/env python3
"""
Author : Daniel T Lee <daniel.ts.lee@gmail.com>
Date   : 2024-11-13
Purpose: Twelve Days of Christmas
"""

import argparse
import sys
import os
import io

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve Days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='days',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()

    if (args.num < 1 or args.num > 12):
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


def verse(day):
    gifts = [
        'A partridge in a pear tree.',
        'Two turtle doves,',
        'Three French hens,',
        'Four calling birds,',
        'Five gold rings,',
        'Six geese a laying,',
        'Seven swans a swimming,',
        'Eight maids a milking,',
        'Nine ladies dancing,',
        'Ten lords a leaping,',
        'Eleven pipers piping,',
        'Twelve drummers drumming,',
    ]

    ordinal = [
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
        'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'
    ]

    lines = [f'On the {ordinal[day - 1]} day of Christmas,',
             'My true love gave to me,']
    
    lines.extend([gifts[day - 1] for day in range(day, 0, -1)])

    if (day > 1):
        lines[-1] = 'And ' + lines[-1][0].lower() + lines[-1][1:]

    return '\n'.join(lines)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    song = [verse(day) for day in range(1, args.num + 1)]

    text = '\n\n'.join(song)

    """
    gifts = [
        'A partridge in a pear tree.',
        'Two turtle doves,',
        'Three French hens,',
        'Four calling birds,',
        'Five gold rings,',
        'Six geese a laying,',
        'Seven swans a swimming,',
        'Eight maids a milking,',
        'Nine ladies dancing,',
        'Ten lords a leaping,',
        'Eleven pipers piping,',
        'Twelve drummers drumming,',
    ]

    ordinal = [
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
        'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'
    ]

    text = ''
    for idx, dayName in enumerate(ordinal):
        text += f'On the {dayName} day of Christmas,\nMy true love gave to me,\n'
        for ind in range(idx, -1, -1):
            if ind == 0 and idx > 0:
                text += 'And a ' + gifts[0][2:] + '\n'
            else:
                text += gifts[ind] + '\n'
        else:
            text += '\n'
        if idx == args.num-1:
            break
    """

    textIo = io.StringIO(text.strip())
    for line in textIo:
        args.outfile.write(line)
        pass

# --------------------------------------------------
if __name__ == '__main__':
    main()
