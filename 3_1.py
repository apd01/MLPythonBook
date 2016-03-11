from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df=1)

content = ["How to format my hard disk", "Hard disk format problems"]

X = vectorizer.fit_transform(content)
names_list = vectorizer.get_feature_names() #[u'disk', u'format', u'hard', u'how', u'my', u'problems', u'to']

print(X.toarray().transpose()[0, :])

for idx, name in enumerate(names_list):
    #print(X.toarray().transpose()[idx, :], name)
    print(idx)


