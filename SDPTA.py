from random import randint, uniform
import numpy as np
import matplotlib.pyplot as plt


P = 35000
x1 = np.random.rand(1, 5)
d1 = np.random.rand(1, 5)

x2 = np.random.rand(1, 5)
d2 = np.random.rand(1, 5)

D = [[x1, d1], [x2, d2]]  #Dataset indexted in p
print(D)


def sdpta(D):
    P = len(D)
    dim = len(D[0][0])  #x1 is same len as x2

    c = 0.1
    w = 0.1 * (-1 + 2 * np.random.rand(3,1))  # 3 random numbers in range (-1,2) - initial weights [0.1 * (uniform(-1, 2)) for _ in xrange(3)] np.array(0.1 * (np.random.rand(dim, 1))).T
    print('Weights:\n' + str(w))

    e = 0
    p = 0
    k = 1

    while True:
        while p <= P:
            x, d = D[p]
            o = np.sign(np.dot(w.T, x))
            w = w + np.dot(0.5 * c * (d - o), x)
            e = 0.5 * (d - o)**2 + e
            p += 1

            x1 = [0, 1]

            if w[2] == 0:
                w[2] = w[2] + 0.0001

            y1 = (-w[3] / w[2]) - ((w[1] * x1 ) / w[2])

            if e == 0:
                break

        k = k + 1


sdpta(D)