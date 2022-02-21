import matplotlib.pyplot as plt
from scipy.integrate import quad
import numpy as np

# calculate omega and period
period = 8
W = 2*np.pi/period

# define f(x) by the pulse train plot
def f(x):
    if (-2 <= x <= 2):
        return 1
    return 0

def fourier_a(n):
    return (2 / period) * quad(lambda x,n: f(x) * np.cos(x*W*n),-4,4,args=(n))[0]

def fourier_b(n):
    return (2 / period) * quad(lambda x,n: f(x) * np.sin(x*W*n),-4,4,args=(n))[0]

def fourier_series(x):
    A0 = (1 / period) * quad(f,-2,2,)[0]
    A = 0
    B = 0

    for n in range(1,11):
        A += fourier_a(n)*np.cos(n*x*W)
        B += fourier_b(n)*np.sin(n*x*W)

    return A0 + A + B

if __name__ == '__main__':
    x = np.arange(-10,10,0.01)
    y = fourier_series(x)
    
    plt.plot(x,y)
    plt.title("Fourier [-10, 10]:")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

