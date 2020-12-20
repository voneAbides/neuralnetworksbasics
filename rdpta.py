import numpy as np
cat = 0
num = 0
d = [[]]


def rdpta(y):
    c = 0.1
    w = 0.1 * (-1 + 2 * np.random.rand(cat, 1))
    e = 0
    p = 0
    k = 1

    while k < 100:
        while p < (cat * num):
            for i in range(cat):
                # o[i] = np.sign(np.dot(w[i, :]), y[:, p])
                w[i, :] = w[i, :] + 0.5 * c * (d[i, p] - o[i]) * y[:, p].T  #Where the dot product is calculated?
                e = 0.5 * ((d[i, p] - o[i])**2) + e

            p = p + 1

        if e == 0:
            break
        else:
            e = 0
            p = 1

        k = k + 1


