from random import randint, uniform
import numpy as np
import matplotlib.pyplot as plt


x1 = np.random.rand(1)
y1 = np.random.rand(1)

x2 = np.random.rand(1)
y2 = np.random.rand(1)

x3 = np.random.rand(1)
y3 = np.random.rand(1)

x4 = np.random.rand(1)
y4 = np.random.rand(1)

y = np.array([[x1, y1, 1],
            [x2, y2, 1],
            [x3, y3, 1],
            [x4, y4, 1]])   #Dataset indexted in p


# d = [0, 1, 1, 0]
d = np.squeeze(0.1 * (-1 + 2 * np.random.rand(4)))
print(y)


def sdpta(y):
    P = len(y)
    dim = len(y[0][0])  #x1 is same len as x2

    c = 0.1
    w = np.squeeze(0.1 * (-1 + 2 * np.random.rand(3)))  # 3 random numbers in range (-1,2) - initial weights [0.1 * (uniform(-1, 2)) for _ in xrange(3)] np.array(0.1 * (np.random.rand(dim, 1))).T
    print('Weights:\n' + str(w))

    e = 0
    p = 0
    k = 1

    while True:
        while p < P:
            # x, d = D[p]
            o = np.sign(np.dot(w.T, y[p, :]))
            w = w + 0.5 * c * (d[p] - o) * y[p, :]
            e = 0.5 * (d[p] - o)**2 + e
            p += 1

            x0 = [0, 1]

            if w[1] == 0:
                w[1] = w[1] + 0.0001

            y0 = (-w[2] / w[1]) - ((w[0] * x0) / w[1])
            # plt.plot(x1, y1, 'g')

        if e == 0:
            break
        else:
            e = 0
            p = 0

        k = k + 1
        print(k)



sdpta(y)