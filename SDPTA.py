from random import randint, uniform
import numpy as np

from pip._vendor.msgpack.fallback import xrange

c = 0.1
W = [0.1 * (uniform(-1, 2)) for _ in xrange(3)]  # 3 random numbers in range (-1,2) - initial weights
E = 0
p = 1
k = 1

print(W)
while True:
    while p <= p:
        o = np.sign(W * y)
