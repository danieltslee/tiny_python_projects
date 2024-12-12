#!/usr/bin/env python3
"""
Author : Daniel T Lee <daniel.ts.lee@gmail.com>
Date   : 2024-12-10
Purpose: Rock the Casbah
"""

import argparse
import io
import random
import re
import csv

from pprint import pprint
from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed (default: None)',
                        metavar='int',
                        type=int,
                        default=None)
    
    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises (default: 4)',
                        metavar='int',
                        type=int,
                        default=4)

    parser.add_argument('-f',
                        '--file',
                        help='Input file of exercises',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv')

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps (default: False)',
                        action='store_true')

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


def read_csv(fh):
    """Read the CSV input"""
    reader = csv.DictReader(fh, delimiter=',')
    exercises = []
    for rec in reader:
        name, reps = rec.get('exercise'), rec.get('reps')
        if name and reps:
            #low, high = map(int, reps.groups())
            match = re.search(r'(\d+)-(\d+)', reps)
            if match:
                low, high = map(int, match.groups())
                exercises.append((name, low, high))

    return exercises


def test_read_csv():
    """Test read_csv"""

    text = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(text) == [('Burpees', 20, 50), ('Situps', 40, 100)]


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    exercises = read_csv(args.file)
    
    if exercises:
        exercises = random.sample(exercises, k=args.num)
        div = 2 if args.easy else 1
        exercises = [(exercise[0], random.randint(exercise[1], exercise[2]) // div) \
                    for exercise in exercises]

        print(tabulate(exercises, headers=('Exercise', 'Reps')))


# --------------------------------------------------
if __name__ == '__main__':
    main()
