import nltk
from nltk.text import FreqDist
from nltk import word_tokenize
from nltk.corpus import stopwords

outputDirectory = './ch03/data/output/'
with open(outputDirectory + 'comment_corpus.txt', 'r') as infile:
    full_comments = infile.read().decode('utf-8')
    full_comments = full_comments.split()
    #for word in full_comments:
    #    word.replace('\n', '')
    # full_comments = nltk.Text(full_comments)
    #full_comments.collocations(num=50, window_size=4)
    #full_comments.common_contexts(['Nick', 'Nate', 'Conor'], num=5)
    #full_comments.concordance('Nate')

    # A Lemmatizer is a stemmer that tries to preserve word context
    lem = nltk.WordNetLemmatizer()
    processed_tokens = []

    # Process the words in comments (no further sentiment analysis can be done after this step)
    # It's basically creating an mma wordlist
    stopwords = nltk.corpus.stopwords.words('english')
    for t in full_comments:
        t = t.lower()
        t = t.replace('.', '').replace(',', '').replace('?','')
        t = lem.lemmatize(t)
        if t not in stopwords:
            processed_tokens.append(t)


    fdist = FreqDist(processed_tokens)
    for x in sorted(w for w in set(processed_tokens) if fdist[w] > 1000):
        print(x.encode('utf-8'))
