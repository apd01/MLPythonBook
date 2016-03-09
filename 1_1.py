import scipy as sp
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



def error(f, x, y):
    return sp.sum((f(x)-y)**2)

fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)
f1 = sp.poly1d(fp1)

f2p = sp.polyfit(x, y, 2)
f2 = sp.poly1d(f2p)
print(error(f2, x, y))

fp10 = sp.polyfit(x, y, 10)
f10 = sp.poly1d(fp10)

fp100 = sp.polyfit(x, y, 100)
f100 = sp.poly1d(fp100)





fx = sp.linspace(0,x[-1], 1000) # generate X-values for plotting
plt.plot(fx, f1(fx), linewidth=2)
plt.plot(fx, f2(fx), linewidth=2)
plt.plot(fx, f10(fx), linewidth=2)
plt.plot(fx, f100(fx), linewidth=2)
plt.legend([ "d=%i" % f1.order,
             "d=%i" % f2.order,
             "d=%i" % f10.order,
             "d=%i" % f100.order,
             ], loc="upper left")

plt.show()