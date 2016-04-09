import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import pickle

def sigmoid(p,x):
    x0,y0,c,k=p
    y = c / (1 + np.exp(-k*(x-x0))) + y0
    return y

def residuals(p,x,y):
    return y - sigmoid(p,x)

def resize(arr,lower=0.0,upper=1.0):
    arr=arr.copy()
    if lower>upper: lower,upper=upper,lower
    arr -= arr.min()
    arr *= (upper-lower)/arr.max()
    arr += lower
    return arr




# raw data
# x = np.array([821,576,473,377,326],dtype='float')
# y = np.array([255,235,208,166,157],dtype='float')
with open('./data/reddit/output/submission_data.p', 'r') as infile:
    all_data = pickle.load(infile)

x = []
y = []

#for row in all_data:
#    if row[0][0] == '4cwar0': #4cwdhk
#        x.append(row[0])

    #x = [row for row in all_data[0, :] if row[0] == '4cwdhk']
    #y = [y for y in all_data[1, :] - all_data[2, :]]


# y0: y at small x
# y0 + c: y at large x
# k: Rise rate (bigger = faster)
# x0: Y = (base+max)/2

#x = [row for row in all_data if row[0][0] == '4d2qq3']
x = all_data[33]
y = []

for idx in range(0, len(x)):
    y.append(float(x[idx][2]))
    x[idx] = float(x[idx][1])


x.insert(0, 0)
y.insert(0, 0)

x = np.asarray(x)
y = np.asarray(y)

x_max = x.max()
y_max = y.max()
x=resize(x,lower=0.0)
y=resize(y,lower=0.0)



p_guess=(np.median(x),np.median(y),1.0,1.0)
p, cov, infodict, mesg, ier = scipy.optimize.leastsq(
    residuals,p_guess,args=(x,y),full_output=1)

x0,y0,c,k=p
print('''\
x0 = {x0}
y0 = {y0}
c = {c}
k = {k}
'''.format(x0=x0,y0=y0,c=c,k=k))

xp = np.linspace(0, 1.1, 1500)

#Edited 'p' to plot a manual sigmoid, taken from Analyze_Coefficients -> predict
p = [ -0.16016791, -34.12028477 , 35.09745778 , 20.49026726]
print(xp)
print(1788/86400.0)
num_upvotes_predicted = 13/sigmoid(p, 1788/86400.0)
print(num_upvotes_predicted)
pxp=sigmoid(p,xp)


xp *= 86561
pxp *= num_upvotes_predicted

x *= x_max
y *= y_max


# Plot the results
plt.plot(x, y, '.', xp, pxp, '-')
plt.xlabel('x')
plt.ylabel('y',rotation='horizontal')
plt.grid(True)
plt.ylim([-.1, y_max])
plt.xlim([-.1, x_max])
plt.show()

