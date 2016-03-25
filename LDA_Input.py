import gzip
import json
from nltk.corpus import stopwords
import gensim
from gensim import corpora
import logging
import pickle

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


#lda = pickle.load(open('lda.p', 'rb'))
lda = gensim.models.LdaModel.load('lda_new.p')

outputDirectory = './ch03/data/output/'
dict = corpora.Dictionary.load(outputDirectory + 'tmp.dict')
# cmt_lda = lda[dict.doc2bow('No Holly to be the baddest chick on the planet and earn Dana\'s respect you need to hide inside your room and eat tubs of ice cream until Ronda beats Tate then text Dana "I guess it\'s time to get back to work"'.lower().split())]
cmt_lda = lda[dict.doc2bow('bjj triangle'.lower().split())]

print(cmt_lda)
# for a in [lda.print_topics(20)]:
#     print(a)
#print(lda.print_topics(2))

# [0][1])
#for idx in range(0, len(cmt_lda)):
#    print(dict[cmt_lda[idx][0]])
#    print((cmt_lda[idx][1]))


for topic, weight in cmt_lda:
    if weight > .08:
        print(weight)
        print(lda.print_topic(topic))