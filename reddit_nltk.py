import nltk
import json
import gzip
import math
from nltk.text import FreqDist
from nltk import word_tokenize
from nltk.corpus import stopwords

outputDirectory = './ch03/data/output/'
with gzip.GzipFile(outputDirectory + 'comment_corpus.txt', 'r') as infile:
    #full_comments = infile.read().decode('utf-8')
    #full_comments = full_comments.split()
    #for word in full_comments:
    #    word.replace('\n', '')
    # full_comments = nltk.Text(full_comments)
    #full_comments.collocations(num=50, window_size=4)
    #full_comments.common_contexts(['Nick', 'Nate', 'Conor'], num=5)
    #full_comments.concordance('Nate')

    # A Lemmatizer is a stemmer that tries to preserve word context
    lem = nltk.WordNetLemmatizer()
    processed_tokens = []

    #print(full_comments[3])
    comments = json.loads(infile.read(), encoding='utf-8')
    print(comments["Length"])
    print(comments["Comments"][12])


'''
    com_dict = comments["Comments"]
    counter = 0.1
    full_comments = ''
    for idx, comment in enumerate(com_dict):
        full_comments += comment
        if((float(idx)/float(len(com_dict))) > counter):
           counter += 0.1
           print("%f percent of the way through" % (100 * float(idx)/float(len(com_dict))))
    full_comments = full_comments.split()
'''

# Process the words in comments (no further sentiment analysis can be done after this step)
# It's basically creating an mma wordlist
'''
stopwords = nltk.corpus.stopwords.words('english')
print("00 of the way through")
for t, idx in full_comments:
    t = t.lower()
    t = t.replace('.', '').replace(',', '').replace('?','')
    t = lem.lemmatize(t)
    if t not in stopwords:
        processed_tokens.append(t)
    print("\r %f of the way through" % (idx/comments["Length"]))

fdist = FreqDist(processed_tokens)
for x in sorted(w for w in set(processed_tokens) if fdist[w] > 2000):
    print(x.encode('utf-8'))
'''



















