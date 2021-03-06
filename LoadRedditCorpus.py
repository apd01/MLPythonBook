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

json_comments = {'Submission':'', 'Comments':[]}
reddit_threads = {"Threads":[]}

for currentFile in files:
    with open(inputDirectory + currentFile, 'r') as data_file:
        json_comments = {'Submission':'', 'Comments':[]}

        print("%s" % data_file)
        try:
            data = json.load(data_file)
            submission = data["Submission"]
            comments = data["CommentList"]
            if(len(comments)>0):
                # Structure the comments such that each comment is put into a separate dict entry along with
                # its respective parent comment.
                json_comments['Submission'] = {'Title':submission['title']} # Two different ways of doing the same JSON thing
                json_comments['Submission']['Url'] = [submission['url']] #
                for comment in comments:
                    #outfile.write('"Comment":' + json.dumps(comment["id"], indent=4, ))
                    json_comments['Comments'].append(comment['body'].replace('[','\[').replace(']', '\]'))
                reddit_threads["Threads"].append(json_comments)
        except Exception as e: # If there's an error here, it's probably because there are no comments in the file
            print("Exception")
            print(type(e))



with open(outputDirectory + 'comment_corpus.txt', 'w') as outfile:
    outfile.write(json.dumps(reddit_threads)) # , indent=4 taken out for smaller filesize
    #all_comments += comment["body"] + '\n