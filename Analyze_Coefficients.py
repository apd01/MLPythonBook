import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import pickle


with open('./data/reddit/output/fitted_data.p', 'r') as infile:
    coefficients = pickle.load(infile)

with open('./data/reddit/output/submission_data.p', 'r') as infile:
    all_data = pickle.load(infile)
    print(len(coefficients))


coefficients_dict = {}
for idx in range(1, len(coefficients)):
    coefficients_dict[coefficients[idx][0]] = [coefficients[idx][1], coefficients[idx][2], coefficients[idx][3], coefficients[idx][4]]


X = []
y = []
for file in all_data:
    for sample in file:
        if sample[0] in coefficients_dict:
            X.append([sample[1], sample[2] - sample[3], sample[4]])
            y.append(coefficients_dict[sample[0]])
        else:
            continue

print(len(X))
print(len(y))

'''
for idx in range(0, len(X)):
    X[idx] = [float(x) / float(X[idx][0]) for x in X[idx]]


for idx in range(0, len(y)):
    y[idx] = [float(yi) / float(y[idx][0]) for yi in y[idx]]
'''

X_train = X[:-150]
X_test = X[-150:]
y_train = y[:-150]
y_test = y[-150:]

regr = linear_model.LinearRegression(normalize='True')
regr.fit(X_train, y_train)

# The coefficients
print('Coefficients: \n', regr.coef_)

# The mean square error
print("Residual sum of squares: %.2f"
      % np.mean((regr.predict(X_test) - y_test) ** 2))

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(X_test, y_test))

print(regr.predict(X_test[15]))

predictions = [regr.predict(X_test[n]) for n in range(0, len(X_test))]

print(len(X_test[:][0]))
print(len(y_test[:][0]))

plt.scatter(X_test[:20][0][0], y_test[:20][0][0],  color='black')
plt.plot(X_test, regr.predict(X_test), color='blue',
         linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()