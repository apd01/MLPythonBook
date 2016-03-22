# Parse previously scraped reddit comments (json structure)
# and create a wordlist corpus. Save this corpus to disk

from nltk.corpus import PlaintextCorpusReader
import json
import gzip
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


# Replace this with
'''
for currentFile in files:
    with open(inputDirectory + currentFile, 'r') as data_file:
        data = json.load(data_file)
        comments = data["CommentList"]
        all_comments = ''
        for comment in comments:
            all_comments += comment["body"] + '\n'
        with open(outputDirectory + 'comment_corpus.txt', 'a') as outfile:
            outfile.write(all_comments.encode('utf-8'))
'''

# with open(outputDirectory + 'comment_corpus.txt', 'a') as outfile:
    # json.dump('{\n"Comments":\n', outfile)

json_comments = {"Length":'',"Comments":[]}

for currentFile in files:
    with open(inputDirectory + currentFile, 'r') as data_file:
        print("%s" % data_file)
        data = json.load(data_file)
        # Error here if there's no "CommentList" key. Consider rewriting redditJson to append
        # comments as json objects like in _nltk.py
        try:
            comments = data["CommentList"]
            for comment in comments:
                #outfile.write('"Comment":' + json.dumps(comment["id"], indent=4, ))
                json_comments["Comments"].append(comment["body"])
        except Exception as e: # If there's an error here, it's probably because there are no comments in the file
            print("Exception")
            print(e)

with gzip.GzipFile(outputDirectory + 'comment_corpus.txt', 'w') as outfile:
    json_comments["Length"] = (len(json_comments["Comments"]))
    outfile.write(json.dumps(json_comments)) # , indent=4 taken out for smaller filesize
            #all_comments += comment["body"] + '\n'