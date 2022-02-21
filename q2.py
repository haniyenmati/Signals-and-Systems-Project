# stdnum : 9832068 ----> a = 6 & b = 8

import matplotlib.pyplot as plt
import numpy as np


def draw_sin_pi_t():
    x = np.arange(-10,10,0.001)
    y = [np.sin(np.pi * t) / (np.pi * t) for t in x]



    plt.plot(x, y)
    plt.title("sin(pi * t) / (pi * t)")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def draw_sin_pi_6t_8():
    x = np.arange(-10,10,0.001)
    y = [np.sin(np.pi * (6*t + 8)) / (np.pi * (6*t + 8)) for t in x]



    plt.plot(x, y)
    plt.title("sin(pi * (6t + 8) / (pi * (6t + 8))")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


if __name__ == '__main__':
    draw_sin_pi_t()
    draw_sin_pi_6t_8()