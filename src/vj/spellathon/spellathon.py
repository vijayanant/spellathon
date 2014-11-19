'''
Created on Jul 2, 2012

@author: Vijay Ananth
'''
import sys
import argparse
import enchant
import itertools
from sets import Set

def findPossibleWords(keyAlphabet, alphabetList):
    """Lists all the words that are made up of the chars in
    'alphabetList' and must contain 'keyAlphabet'"""
    dict=enchant.Dict("en_UK")

    word_perms = ("".join(j) for k in range(4, len(alphabetList) + 1) for j in itertools.permutations(alphabetList, k))

    possible_words = Set()
    for word in word_perms:
        if dict.check(word) and keyAlphabet in word : # and toolsLib.containsOnlyFrom(word, alphabetList):
            possible_words.add(word)
    return list(possible_words)

def processArgs(args):
    #dict_file=os.path.join(os.path.dirname(__file__),'sampleDictionary.dict')
    parser = argparse.ArgumentParser(description='Find all possible valid words using a list alphabets')
    parser.add_argument('-k', '--key', action="store", dest='key',
                        help='Alphabet that all words must contain')
    parser.add_argument('-l', '--list', action="store", dest="list",
                        help='Alphabets using which words are to be formed including key')
    #parser.add_argument('-d', '--dict', action="store", dest="dict", nargs='?',
    #                   help='Absolute path to a dictionary file', default=dict)
    
    return parser.parse_args(args)
      
if __name__ == '__main__':
    args=processArgs(sys.argv[1:])
    print args

    myWordList=findPossibleWords(args.key,args.list)
    print myWordList