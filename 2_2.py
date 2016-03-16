import scipy as sp

from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import KFold

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


classifier = KNeighborsClassifier(n_neighbors=1)
classifier = Pipeline([('norm', StandardScaler()), ('knn', classifier)])




data = sp.genfromtxt("seeds_dataset_clean.txt", delimiter="\t", usecols=(0,1,2,3,4,5,6,7))

features = data[:, 0:6]
labels = data[:, 7]


print(labels)

labels = labels[~sp.isnan(features).any(axis=1)]
features = features[~sp.isnan(features).any(axis=1)]

features = features[~sp.isnan(labels)]
labels = labels[~sp.isnan(labels)]


print("Features shape: ", features.shape)
kf = KFold(len(features), n_folds=5, shuffle=True)


#for tra, test in kf:
#    print("Training: ", tra, "Testing: ", test)

# print("Any element NaN?", sp.any(sp.isnan(features)))
# print("Any element NaN?", sp.any(sp.isnan(labels)))
# print("Is finite?", sp.all(sp.isfinite(features)))
# print("Is finite?", sp.all(sp.isfinite(labels)))


means = []
for training, testing in kf:
    print(features[training])
    print(labels[training])
    classifier.fit(features[training], labels[training])
    prediction = classifier.predict(features[testing])

    curmean = sp.mean(prediction == labels[testing])
    means.append(curmean)
print("Mean accuracy: {:.1%}".format(sp.mean(means)))

print("Predict this is a {:}".format(classifier.predict([1, 1.5, 1, 1, 0.5, 0.5])))
