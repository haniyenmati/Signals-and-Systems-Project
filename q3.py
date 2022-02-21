#Y(jw) = H(jw)*X(jw)

import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
from scipy.integrate import quad
import math
import numpy as np

def h(t):
    # h(t) = e ^ -t . u(t) --> u(t) = 1 for t>=0 otherwise u(t) = 0
    if t>=0:
        return math.exp(-t)
    else:
        return 0

def x(t):
    if t <= math.pi/2 and t>= -math.pi/2:
        return 1
    else:
        return 0

def conv_func(tau,t):

    return x(tau)*h(t - tau)

def H():
    t = np.arange(-2 * (np.pi), 2 * (np.pi), 0.1)
    hlist = []
    for number in t:
        hlist.append(h(number))

    H = fft(hlist)
    return H

def X():
    t = np.arange(-2 * (np.pi), 2 * (np.pi), 0.1)
    xlist = []
    for number in t:
        xlist.append(x(number))

    X = fft(xlist)
    return X

def conv_jw():
    t = np.arange(-2 * (np.pi), 2 * (np.pi), 0.1)
    Xjw = X()
    Hjw = H()
    Yjw = [Xjw[i] * Hjw[i] for i in range(len(Hjw))]

    y = ifft(Yjw)
    yt = [abs(y[j]) for j in range(len(y))]
    plt.plot(t, yt)
    plt.title('y(t) using inverse fft')
    plt.show()

def conv():
    t = np.arange(-2 * (np.pi), 2 * (np.pi), 0.1)
    xlist=[x(number) for number in t]
    hlist=[h(number) for number in t]

    M = len(hlist)
    K = len(xlist)

    ylist = [0 for _ in range(M + K + 1)]

    
    q = 0
    for i in range(M + K + 1):
        conv_add = 0
        if i < K:
            for j in range(i+1):
                conv_add = conv_add + xlist[j]*hlist[i - j]
        else:
            while q < M+1:
                new_var = 0
                conv_add = conv_add + xlist[(i - M + new_var)-1]*hlist[(M - new_var)-1]
                q = q + 1
                new_var = new_var + 1
            q = q + 1
        ylist[i] = 1/8*conv_add

    plt.plot(ylist)
    plt.title('y(t) using conv formula')
    plt.show()

t = np.arange(-2 * (np.pi), 2 * (np.pi), 0.1)
def conv_integral():
    ylist = [(quad(conv_func,-np.inf,np.inf,args=(number)))[0] for number in t]

    plt.plot(t,ylist)
    plt.title('y(t) using integral')
    plt.show()

if __name__ == '__main__':
    conv_jw() # using Y(jw) = X(jw)H(jw)
    conv()  #using conv formula
    conv_integral() #using integral

