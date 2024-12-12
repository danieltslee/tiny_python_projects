#!/usr/bin/env python3
"""
Author : Daniel T Lee <daniel.ts.lee@gmail.com>
Date   : 2024-11-16
Purpose: Make rhyming "words"
"""

import argparse
import string
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='str',
                        help='A positional argument')

    args = parser.parse_args()

    return args


def stemmer(word):
    """Breaking word into consonants and the rest"""
    vowels = 'aeiou'
    consonants = ''.join([c for c in string.ascii_lowercase if c not in vowels])
    pattern = (
              '([' + consonants + ']+)?'    # capture leading consonants
              '('                           # start capture
              '[' + vowels + ']'            # at least one vowel
              '.*'                          # zero or more of anything else
              ')?'                          # end capture
              )                       
    match = re.match(pattern, word.lower())
    return (match.group(1) or '', match.group(2) or '') if match else ('','')

'''
def stemmer(word):
    """Return leading consonants (if any), and 'stem' of word"""

    word = word.lower()
    vowel_pos = list(map(word.index, filter(lambda v: v in word, 'aeiou')))

    if vowel_pos:
        first_vowel = min(vowel_pos)
        return (word[:first_vowel], word[first_vowel:])
    else:
        return (word, '')
'''

def test_stemmer():
    """test the stemmer"""

    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '')
    #assert stemmer('123') == ('123', '')



def vowelLoc(word):
    ind = next((ch for ch in word.lower() if ch in 'aeiou'), '')
    return word.lower().index(ind) if ind else False


def makeRhymed(pref, word):
    suffix = None
    if vowelLoc(word) is not False:
        suffix = word[vowelLoc(word):]
    if (word[:vowelLoc(word)].isupper()):
        pref = pref.upper()
    
    rhymed = f'{pref}{suffix}'

    return rhymed if rhymed != word else None


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    
    args = get_args()

    vowels = 'aeiou'
    consonants = [c for c in string.ascii_lowercase if c not in 'aeiou']
    consonants = list(filter(lambda c: c not in vowels, string.ascii_lowercase))
    prefixes = consonants + (
            'bl br ch cl cr dr fl fr gl gr pl pr sc '
            'sh sk sl sm sn sp st sw th tr tw thw wh wr '
            'sch scr shr sph spl spr squ str thr'.split()
            )
    
    start, rest = stemmer(args.word)

    if rest:
        # words by list comprehension
        words = '\n'.join(sorted([p + rest for p in prefixes if p != start]))
        print(words) 
    else:
        print(f'Cannot rhyme "{args.word}"')

'''
    # Test if has vowel
    if ([ch for ch in args.word if ch in 'aeiouAEIOU']):
        pass
    else:
        print(f'Cannot rhyme "{args.word}"')
        return


    prefix = [s for s in string.ascii_lowercase if s not in 'aeiou']
    consClut = 'bl br ch cl cr dr fl fr gl gr pl pr sc \
            sh sk sl sm sn sp st sw th tr tw thw wh wr \
            sch scr shr sph spl spr squ str thr'.split()
    prefix.extend(consClut)
    prefix.sort()

    for pref in prefix:
        print(makeRhymed(pref, args.word).lower()) if makeRhymed(pref, args.word) else print(end='')
'''


# --------------------------------------------------
if __name__ == '__main__':
    main()
