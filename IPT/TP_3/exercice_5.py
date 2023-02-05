import time

from exercice_4 import *


# 1. T(i, j) = max(T(i-1, j), T(i, j-1), T(i-1, j-1))
# Si i ou j = 0, T(i, j) = 0

# 2. T(i, j) = max(T(i-1, j), T(i, j-1), T(i-1, j-1)) pour i > 0 et j > 0

# 3.

def maxi_tab(T: np.array) -> (int, int):
    M, Mi, Mj = 0, 0, 0
    (n, m) = np.shape(T)
    for i in range(n):
        for j in range(m):
            if T[i, j] > M:
                M = T[i, j]
                Mi = i
                Mj = j
    return Mi, Mj


# 4.

def carre_blanc_bas_haut(M: np.array) -> (int, (int, int)):
    n = np.shape(M)[0]
    T = np.zeros((n, n), dtype=int)

    for i in range(n):
        T[i, 1] = 1
    for j in range(n):
        T[1, j] = 1

    for i in range(1, n):
        for j in range(1, n):
            if M[i, j] == 255 and min(M[i - 1, j - 1], M[i - 1, j], M[i, j - 1]) == 255:
                T[i, j] = 1 + max(T[i - 1, j], T[i, j - 1], T[i - 1, j - 1])

    Mi, Mj = maxi_tab(T)
    return T, T[Mi, Mj], (Mi, Mj)


M = carre(15, 0.5)
print(carre_blanc_bas_haut(M))
affichage(M)
