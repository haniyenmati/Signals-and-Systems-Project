import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.fftpack import ifft
import math
import numpy as np

# suppose h(t) = e ^ (-2|t|)
h = lambda t: math.exp(-2*abs(t))

# suppose Xs(t) = cos(0.1t)
Xs = lambda t: math.cos(0.1*t)

# suppose Xn(t) = 0.03cos(10t)
Xn = lambda t: 0.3*math.cos(10*t)


# Xtotal(t) = Xs(t) + Xn(t) in a range of numbers (we assume -2pi t0 2pi)
def Xtotal():
    input_range = np.arange(-2 * (np.pi), 2 * (np.pi), 0.1)
    return input_range, [Xn(t) + Xs(t) for t in input_range]


# draw H(jw)
def draw_h_jw():

    input_range = np.arange(-2 * (np.pi), 2 * (np.pi), 0.1)
    output = [h(t) for t in input_range]

    plt.plot(input_range, fft(output))

    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('H(jw)')
    plt.show()


# calculate H(jw)
def H():
    input_range = np.arange(-2 * (np.pi), 2 * (np.pi), 0.1)
    output = [h(t) for t in input_range]

    return fft(output)

def xTotal_draw():
    
    plt.plot(*Xtotal())
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('X total')
    plt.show()


# y(t) is the output of the system
def y():
    t, x_total = Xtotal()

    x = fft(x_total)
    Hjw = H()

    y_input = [x[i] * Hjw[i] for i in range(len(Hjw))] # conv
    y = ifft(y_input)
    y_t = [abs(i) for i in y]
    
    plt.plot(t,y_t)
    plt.title('y(t)')
    plt.show()

if __name__ == '__main__':
    draw_h_jw()
    xTotal_draw()
    y()
    xTotal_draw()
