from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import scipy as sp


data = load_iris()
print(sp.shape(data))

features = data.data
feature_names = data.feature_names
target = data.target
target_names = data.target_names

for t in range(3):
    if t==0:
        c='r'
        marker='>'
    elif t==1:
        c='g'
        marker='o'
    elif t==2:
        c='b'
        marker='x'
    plt.scatter(features[target==t,0],
                features[target==t,1],
                marker=marker,
                c=c,s=100)
plt.show()

labels = target_names[target]
# print(target)
# print(labels)
print("Features.")

plength = features[:,2]
is_setosa = (labels == 'setosa')
max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()
print('Maximum of setosa: {0}.'.format(max_setosa))
print('Minimum of others: {0}.'.format(min_non_setosa))

