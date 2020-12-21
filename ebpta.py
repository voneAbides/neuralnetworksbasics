import numpy as np

def ebpta():
    i = 3
    j = 3
    k = 1
    y = np.zeros(j, 1)
    y[j, 1] = -1

    n = 0.1
    l = 1
    w = np.squeeze(-1 + 2 * np.random.rand(j, k))
    v = np.squeeze(-1 + 2 * np.random.rand(i, j - 1))
    emax = 0.1
    e = 0
    p = 0
    q = 0

    while  q < 1000:
        while p < (cat * num):
            for h in range(j - 1):
                nety = np.dot(v[:, j].T, z[:, p])
                y[h] = (2 / (1 + np.exp(-l * nety))) - 1

            for ch in range(j - 1):
                neto = np.dot(w[:, ch].T, y)
                o[ch] = (2 / (1 + np.exp(-l * neto))) - 1
                e = 0.5 * ((d[ch, p] - o[ch])**2) + e

                so[ch] = 0.5 * (d[ch, p] - o[ch]) * (1 - o[ch]**2)

            for h in range(j - 1):
                ss = 0
                for ch in range(k):
                    ss = ss + so[h] * w[h, ch]

                sy[ch] = 0.5 * (1 - y[h]**2) * ss

            for h in range(k):
                for ch in range(j):
                    w[j, k] = w[j, k] + n * so[h] * y[ch]

            for ch in range(j - 1):
                for t in range(i):
                    v[t, ch] = v[t, ch] + n * sy(ch) * z[i, p]

            p = p + 1

        if e < emax:
            break
        else:
            e = 0
            p = 1
    q = q + 1