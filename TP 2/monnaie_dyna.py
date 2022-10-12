import numpy as np

SYS = [1, 3, 4]

TAB = np.array([[0, 0, 0],
                [1, 1, 1],
                [2, 2, 2],
                [3, 1, 1],
                [4, 2, 1],
                [5, 3, 2],
                [6, 2, 2]])


def rendu_bas_haut(S: int, M: list) -> (int, np.array):
    T = np.zeros((S+1, len(M)), dtype=int)
    for i in range(S+1):
        T[i, 0] = i
    for j in range(1, len(M)):
        for i in range(S+1):
            if M[j] <= i:
                T[i, j] = min(1 + T[i - M[j], j], T[i, j - 1])
            else:
                T[i, j] = T[i, j - 1]
    return T[S, len(M)-1], T
