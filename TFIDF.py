import gensim
import gzip
import json
from nltk.corpus import stopwords
from gensim import corpora
import string

outputDirectory = './ch03/data/output/'
with gzip.GzipFile(outputDirectory + 'comment_corpus.txt', 'r') as infile:
    comments = json.loads(infile.read(), encoding='utf-8')

    # for comment in comments["Comments"]
    texts = [[word for word in comment.lower().split() if word not in stopwords.words('english')]
             for comment in comments["Comments"]]
    #texts = [word.translate(string.punctuation) for word in texts]
    print('asdf')

    from collections import defaultdict
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1

    # Todo: Maybe make this a frequency percentage?
    # perhaps 1% of comments? That's not ideal either.
    texts = [[token for token in text if frequency[token] > 20] for text in texts]
    # print(sorted(token for token in text if frequency[token] > 3))

    from pprint import pprint
    # pprint([t for t in texts if t], indent=5, width = 250)

    dictionary = corpora.Dictionary(texts)
    dictionary.save(outputDirectory + 'tmp.dict')
    # print(dictionary.token2id)
    # print(sorted(dictionary.token2id, cmp=))


    #print([dictionary.doc2bow(t) for t in texts])
    new_vec = [dictionary.doc2bow(t) for t in texts]
    corpora.MmCorpus.serialize(outputDirectory + 'Reddit_Corpus.mm', new_vec)
    # pprint(new_vec)