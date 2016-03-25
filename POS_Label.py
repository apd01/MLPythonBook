# ------------------------------------------------------------------------------------------
#
#
#
#
#
# ------------------------------------------------------------------------------------------


import json
import gzip
import nltk

# This is pickle funny-business to speed up the tagging loop
# Boy, does it work, though
from nltk.tag.perceptron import PerceptronTagger


debug_mode = True

outputDirectory = './ch03/data/output/'
processed_comments = []
tagger = PerceptronTagger()



if debug_mode:
    with file(outputDirectory + 'comment_corpus.txt', 'r') as infile:
        comments = json.loads(infile.read(), encoding='utf-8')
        for comment in comments["Comments"]:
            cmt = nltk.sent_tokenize(comment)
            cmt = [nltk.word_tokenize(sent) for sent in cmt]
            cmt = [nltk.tag._pos_tag(sent, None, tagger) for sent in cmt] # Pickle funny-business. See top
            print(cmt)
            processed_comments.append(cmt)
else:
    with gzip.GzipFile(outputDirectory + 'comment_corpus.txt', 'r') as infile:
        comments = json.loads(infile.read(), encoding='utf-8')
        for comment in comments["Comments"]:
            cmt = nltk.sent_tokenize(comment)
            cmt = [nltk.word_tokenize(sent) for sent in cmt]
            cmt = [nltk.tag._pos_tag(sent, None, tagger) for sent in cmt] # Pickle funny-business. See top
            #print(cmt)
            processed_comments.append(cmt)


with gzip.GzipFile(outputDirectory + 'taggedComments.zip', 'w') as outfile:
    outfile.write(json.dumps(processed_comments))

    # Open list of named entity hashes




    # Todo: how to handle collisions/naming conflicts? e.g. Diaz
    # Open ?file containing sentiments? Or something?
    # For each comment
    #     Parse for sentences
    #     For each sentence for named entities
    #         Determine whether it was positive or negative
    #         Find hash of NE
    #         Increment count of good/bad comments? {"good": 123, "bad": 321}
    #

