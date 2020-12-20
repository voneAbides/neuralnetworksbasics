import numpy as np
import matplotlib.pyplot as plt


num = 0
y = []
d = []

def scpta(y):

    n = 0.1
    l = 1
    w = 0.1 * (-1 + 2 * np.random.rand(3, 1))
    emax = 0.1
    e = 0
    p = 0
    k = 1

    while k < 1000:
        while p < 2 * num:
            net = np.dot(w.T, y[:, p])
            o = (2 / (1 + np.exp(-l * net))) - 1
            w = w + 0.5 * n * (d[p] - o) * (1 - o**2) * y[:, p]
            e = 0.5 * (d[p] - o) ** 2 + e
            p = p + 1

        x1 = [0, 1]
        if w[2] == 0:
            w[2] = w[2] + 0.0001

        y1 = (-w[3] / w[2]) - ((w[1] * x1 ) / w[2])
        # plt.plot(x1, y1, 'g')

        if e < emax:
            break
        else:
            e = 0
            p = 1

        k = k + 1

