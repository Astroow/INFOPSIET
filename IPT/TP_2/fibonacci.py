def fibo(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)


def fibo_bas_haut(n: int) -> int:
    u, v = 1, 1
    for i in range(n):
        u, v = u + v, u
    return v


MEMO = {0: 1, 1: 1}


def fibo_memo(n: int) -> int:
    if n in MEMO:
        return MEMO[n]
    MEMO[n] = fibo_memo(n - 1) + fibo_memo(n - 2)
    return MEMO[n]
