import numpy as np


def edition_bas_haut(s1: str, s2: str) -> (int, np.array):
    T = np.zeros((len(s1) + 1, len(s2) + 1), dtype=int)
    for i in range(len(s1) + 1):
        T[i, 0] = i
    for j in range(len(s2) + 1):
        T[0, j] = j
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                T[i, j] = min(1 + T[i - 1, j], 1 + T[i, j - 1], T[i - 1, j - 1])
            else:
                T[i, j] = 1 + min(T[i - 1, j], T[i, j - 1], T[i - 1, j - 1])
    return T[len(s1), len(s2)], T


# print(edition_bas_haut("abc", "adcf"))


def edition_bas_haut_reconst(s1: str, s2: str) -> (int, [int]):
    (N, T) = edition_bas_haut(s1, s2)
    L = [0, 0, 0]  # [Remplacements, suppressions, ajouts]
    print(T)
    i, j = len(s1), len(s2)
    while i != 0 and j != 0:
        if s1[i - 1] == s2[j - 1]:
            i -= 1
            j -= 1
        else:
            if T[i, j] == 1 + T[i - 1, j - 1]:
                L[0] += 1
                i -= 1
                j -= 1
            elif T[i, j] == 1 + T[i - 1, j]:
                L[1] += 1
                i -= 1
            elif T[i, j] == 1 + T[i, j-1]:
                L[2] += 1
                j -= 1
    return N, L


# print(edition_bas_haut_reconst("abc", "adcf"))
print(edition_bas_haut_reconst("polynomial", "polygonal"))
