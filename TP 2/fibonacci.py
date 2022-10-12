import sys
import time

import numpy as np

sys.setrecursionlimit(1000000)


def fibo(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)


"""t = time.time()
fibo(30)
print(time.time() - t)"""


def fibo_bas_haut(n: int) -> int:
    u, v = 1, 1
    for i in range(n):
        u, v = u + v, u
    return v


"""t = time.time()
fibo_bas_haut(10000)
print(time.time() - t)"""

memo = {0: 1, 1: 1}


def fibo_memo(n: int) -> int:
    if n in memo:
        return memo[n]
    memo[n] = fibo_memo(n - 1) + fibo_memo(n - 2)
    return memo[n]


print(fibo_memo(7000))
