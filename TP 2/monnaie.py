EURO = [1, 2, 5, 10, 20, 50, 100, 200, 500]


def plus_grand(S: int, M: list) -> int:
    n = len(M)
    i = 0
    while i < n and M[i] <= S:
        i += 1
    return M[i - 1]


def rendu_glouton(S: int, M: list) -> dict:
    R = {}
    while S > M[0]:
        s = plus_grand(S, M)
        S -= s
        if s in R:
            R[s] += 1
        else:
            R[s] = 1
    return R


print(rendu_glouton(747, EURO))
