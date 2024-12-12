#!/usr/bin/env python3
"""
Author : Daniel T Lee <daniel.ts.lee@gmail.com>
Date   : 2024-11-08
Purpose: Brings items to a picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Brings items to a picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='items',
                        nargs='+',
                        help='Items for the picnic.')

    parser.add_argument('-s',
                        '--sorted',
                        help='To sort the items or not.',
                        action="store_true")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    # Store arguments
    args = get_args()
    sortedBool = args.sorted
    allItems = args.items

    # Sort if --sorted
    allItems.sort() if sortedBool else allItems
    # Add "and"
    if len(allItems) == 1:
        itemsStr = allItems[0]   
    elif len(allItems) == 2:
        itemsStr = ' and '.join(allItems)
    else:
        allItems[-1] = 'and ' + allItems[-1]
        itemsStr = ', '.join(allItems)
    print(f'You are bringing {itemsStr}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
