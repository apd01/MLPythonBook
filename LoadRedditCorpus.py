# Parse previously scraped reddit comments (json structure)
# and create a wordlist corpus. Save this corpus to disk

from nltk.corpus import PlaintextCorpusReader
import json
from pprint import pprint
from os import listdir
from os.path import isfile, join


'''
corpus_root = 'ch03\\data\\reddit'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
wordlists.fileids()
wordlists.words('connectives')
'''

outputDirectory = './ch03/data/output/'
inputDirectory = './ch03/data/reddit/'
files = listdir(inputDirectory)

for currentFile in files:
    with open(inputDirectory + currentFile) as data_file:
        data = json.load(data_file)
        comments = data["CommentList"]
        all_comments = ''
        for comment in comments:
            all_comments += comment["body"] + '\n'
        with open(outputDirectory + 'comment_corpus.txt', 'a') as outfile:
            outfile.write(all_comments.encode('utf-8'))

