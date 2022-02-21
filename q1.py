import matplotlib.pyplot as plot
import math, numpy


fourier_transform = lambda omega: 1/(1 - 3/4 * numpy.exp(-1j*omega))

def draw_main_signal():
    x = [i for i in range(22)]
    y = [(0.75) ** i for i in range(22)]

    plot.scatter(x, y)
    plot.xlabel('x')
    plot.ylabel('y')
    plot.title('Main Signal')
    plot.show()


def draw_size():
    x = numpy.arange(-2 * (numpy.pi), 2 * (numpy.pi), 0.1)
    y = [abs(fourier_transform(w)) for w in x]

    plot.plot(x, y)
    plot.xlabel('W (Omega)')
    plot.ylabel('Y')
    plot.title('|X(e**jw)|')
    plot.show()


def draw_phase():  
    # atan((3/4 sin w) / (1 - 3/4 cos w))
    x = numpy.arange(-2 * (numpy.pi), 2 * (numpy.pi), 0.1)
    y = [(3 / 4 * math.sin(w)) / (1 - 3 / 4 * math.cos(w)) for w in x]
    
    plot.plot(x, y)
    plot.xlabel('W (Omega)')
    plot.ylabel('Y')
    plot.title('phase')
    plot.show()

if __name__ == '__main__':
    draw_main_signal()
    draw_size()
    draw_phase()

