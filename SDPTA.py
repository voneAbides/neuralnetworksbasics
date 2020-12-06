from random import randint, uniform
import numpy as np

from pip._vendor.msgpack.fallback import xrange

P = 35000
c = 0.1
W = np.array([0.1 * (uniform(-1, 2)) for _ in xrange(3)]).T  # 3 random numbers in range (-1,2) - initial weights
E = 0
p = 1
k = 1
y = np.array([1, 1, 1])
print(W)

while True:
    while p <= p:
        o = np.sign(np.dot(W, y))

