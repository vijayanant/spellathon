import os
from flask import Flask, request, Response
import enchant
import itertools
from sets import Set
import json


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


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/words', methods=['GET'])
def possible_words():
    key=request.args.get('key', '')
    chars= request.args.get('letters','')
    words = findPossibleWords(key, chars)
    return json.dumps(words)

if __name__ == '__main__':
	app.debug=True
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
