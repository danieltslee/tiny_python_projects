#!/usr/bin/env python3
"""
Author : Daniel T Lee <daniel.ts.lee@gmail.com>
Date   : 2024-11-17
Purpose: Southern fry text
"""

import argparse
import os.path
import string
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Southern fry text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text of file')

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def fry(word):
    
    you_match = re.match('([yY])ou$', word)
    if you_match:
        return you_match.group(1) + "'all"

    ing_match = re.search('(.*)ing$', word)
    if ing_match:
        first =  ing_match.group(1)
        if re.search('[aeiou]', first, re.IGNORECASE):
            return first  + "in'"
    return word


def test_fry():
    # you to y'all
    assert fry('you') == 'y\'all'
    assert fry('You') == 'Y\'all'
    # -ing to in'
    assert fry('swing') == 'swing'
    assert fry('Swing') == 'Swing'
    assert fry('admiring') == 'admirin\''
    assert fry('Admiring') == 'Admirin\''
    # Punctuation
    assert fry('going') == 'goin\''

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for line in args.text.splitlines():
        print( ''.join(map(fry, re.split(r'(\W+)', line))) )



# def stemmer(word):
#     # Check if word exists
#     if (word == ''):
#         return ''
#     # Remove punctuation 
#     punc = ''
#     if word.lower()[-1] not in list(string.ascii_lowercase):
#         punc += word[-1]
#         word = word[:-1]
#     # Test you case
#     if (word.lower() == 'you' and len(word) == 3):
#         return 'y\'all'+punc if word[0].islower() else 'Y\'all'+punc
#     # Test -ing case
#     elif (word.lower().endswith('ing')):
#         # Count vowel occurance
#         vowels = list(c for c in word.lower() if c in 'aeiou')
#         if (len(vowels) > 1):
#             verb = word[:-3]
#             ing = ''.join([c if c.islower() else c.upper() for c in word[-3:-1]])
#             return verb + ing+'\''+punc
#         else:
#             return word+punc
#     else:
#         return word+punc


# def test_stemmer():
#     assert stemmer('') == ''
#     # you to y'all
#     assert stemmer('you') == 'y\'all'
#     assert stemmer('YOU') == 'Y\'all'
#     # -ing to in'
#     assert stemmer('swing') == 'swing'
#     assert stemmer('SWING') == 'SWING'
#     assert stemmer('admiring') == 'admirin\''
#     assert stemmer('ADMIRING') == 'ADMIRIN\''
#     # Punctuation
#     assert stemmer('going?') == 'goin\'?'

# # --------------------------------------------------
# def main():

#     args = get_args()
#     southernText = ''
#     for line in args.text.splitlines():
#         southernText += ''.join([stemmer(word) for word in re.split(r'(\W+)', line.rstrip())]) + '\n'

#     print(southernText.strip())


# --------------------------------------------------
if __name__ == '__main__':
    main()

    
