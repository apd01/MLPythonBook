import gzip
import json
from nltk.corpus import stopwords
import gensim
from gensim import corpora
import logging
import pickle

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

outputDirectory = './ch03/data/output/'
id2word = corpora.Dictionary.load(outputDirectory + 'tmp.dict')

mm = corpora.MmCorpus(outputDirectory + 'Reddit_Corpus.mm')

lda = gensim.models.LdaModel(corpus=mm, num_topics=100, id2word=id2word, chunksize=100)
# lda.print_topics(10)
cmt_lda = lda[id2word.doc2bow('The whole thing fucked, the reason RDA Vs Conor isn\'t a thing is because Nate beat Conor and now Nate Vs RDA makes more sense. However, if they\'re just going to rematch Nate and Conor, then they might aswell rescheduled RDA Vs Conor, i don\'t fucking know anymore i\'m done.'.lower().split())]
print(cmt_lda)
cmt_lda = lda

# Looks like lda.save does the same thing
# pickle.dump(lda, open('lda.p', 'wb'))

lda.save('lda_new.p')

# cmt_hdp = gensim.models.LdaMulticore