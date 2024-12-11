#!/usr/bin/env python3
"""
Author : danieltslee <danieltslee@localhost>
Date   : 2024-11-07
Purpose: Say Hello
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Say Hello",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-n",
        "--name",
        help="Name to greet",
        metavar="name",
        type=str,
        default="World",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Main here """

    args = get_args()
    print("Hello, " + args.name + "!")


# --------------------------------------------------
if __name__ == "__main__":
    main()
