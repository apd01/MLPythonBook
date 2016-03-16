from nltk.corpus import PlaintextCorpusReader

corpus_root = r"C:\Users\Alan Dunne\workspace\ML with Python\BuildingMachineLearningSystemsWithPython\CH03\data\reddit"
worldlists = PlaintextCorpusReader(corpus_root, '.*')

