import scipy as sp
from sklearn import cross_validation

data = sp.genfromtxt("ch01\data\web_traffic.tsv", delimiter="\t")
print(data.shape)
print(data[:3])
x = data[:,0]
y = data[:,1]



print(sp.sum(sp.isnan(x)))
print(sp.sum(sp.isnan(y)))
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]
print(x.shape)
print(y.shape)

import matplotlib.pyplot as plt
# plot the (x,y) points with dots of size 10
plt.scatter(x, y, s=10)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],
               ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)
# draw a slightly opaque, dashed grid
plt.grid(True, linestyle='-', color='0.75')

inflection = 3.5*7*24
print(inflection)

Xa = x[:inflection]
Ya = y[:inflection]

Xb = x[inflection:]
Yb = y[inflection:]

def error(f, x, y):
    return sp.sum((f(x)-y)**2)

for y in range(0,9):
    Xa_Train, Xa_Test, Ya_Train, Ya_Test = cross_validation.train_test_split(Xa, Ya, test_size=.25, random_state=y)
    Xb_Train, Xb_Test, Yb_Train, Yb_Test = cross_validation.train_test_split(Xb, Yb, test_size=.25, random_state=y)

    l1p = sp.polyfit(Xa_Train, Ya_Train, 1)
    l1 = sp.poly1d(l1p)

    l2p = sp.polyfit(Xb_Train, Yb_Train, 2)
    l2 = sp.poly1d(l2p)

    Ratio1 = (error(l1, Xa_Train, Ya_Train)/3)/error(l1, Xa_Test, Ya_Test)
    Ratio2 = (error(l2, Xb_Train, Yb_Train)/3)/error(l2, Xb_Test, Yb_Test)

    # print("Train Error 1: %f" % error(l1, Xa_Train, Ya_Train)/3)
    # print("Test Error 1: %f" % error(l1, Xa_Test, Ya_Test))
    # print("Train Error 2: %f" % error(l2, Xb_Train, Yb_Train)/3)
    # print("Test Error 2: %f" % error(l2, Xb_Test, Yb_Test))
    print("Error Ratio 1: %f" % Ratio1)
    print("Error Ratio 2: %f" % Ratio2)

    from scipy.optimize import fsolve
    reached_max = fsolve(l2-100000, x0=800)/(7*24)
    print("Will hit 100,000 hits/hour at week %f" % reached_max[0])

fd = sp.shape(x)
fd = fd[0]

fx = sp.linspace(0,x[-1], fd) # generate X-values for plotting
fxa = fx[:inflection]
fxb = fx[inflection-150:]
plt.plot(fx, l1(fx), linewidth=2)
plt.plot(fxb, l2(fxb), linewidth=2)
plt.legend([ "d=%i" % l1.order,
             "d=%i" % l2.order,
             ], loc="upper left")

from scipy.optimize import fsolve
reached_max = fsolve(l2-100000, x0=800)/(7*24)
print("Will hit 100,000 hits/hour at week %f" % reached_max[0])


plt.show()