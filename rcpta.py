import numpy as np


cat = 2
num = 1

def rcpta(y, d):
    n = 0.1
    l = 1
    w = np.squeeze(-1 + 2 * np.random.rand(cat, 3))
    emax = 0.1
    e = 0
    p = 0
    k = 1

    while k < 1000:
        while p < (cat * num):
            for i in range(cat):
                net = np.dot(w[i, :], y[:, p])
                o = (2 / (1 + np.exp(-l * net))) - 1
                w[i, :] = w[i, :] + (0.5 * n * (d[i, p] -o) * (1 - o**2) * y[:, p].T)
                e = 0.5 * ((d[i, p] - o)**2 ) + e

            p = p + 1

        if e < emax:
            break
        else:
            e = 0
            p = 1

    k = k + 1

