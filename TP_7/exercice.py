import numpy as np

JEU_TEST = np.array(
    [[0, 1, 1, 0, 1, 0, 0],
     [1, 0, 0, 0, 0, 0, 1],
     [1, 0, 1, 0, 0, 0, 0],
     [1, 0, 2, 1, 2, 0, 1],
     [1, 1, 2, 2, 1, 0, 1],
     [2, 1, 0, 1, 1, 2, 1]]
)

HEURISTIQUE = np.array([
    [3, 4, 5, 7, 5, 4, 3],
    [4, 6, 8, 10, 8, 6, 4],
    [5, 8, 11, 13, 11, 8, 5],
    [5, 8, 11, 13, 11, 8, 5],
    [4, 6, 8, 10, 8, 6, 4],
    [3, 4, 5, 7, 5, 4, 3]
])


# 1
def est_gagnant(A: np.array, joueur: int) -> bool:
    c = 0
    (x, y) = np.shape(A)
    x -= 1
    y -= 1
    for i in range(x + 1):
        for j in range(y):
            if A[i, j] == joueur:
                c += 1
            else:
                c = 0
            if c == 4:
                return True
    for i in range(x + 2):
        for j in range(y):
            if A[j, i] == joueur:
                c += 1
            else:
                c = 0
            if c == 4:
                return True
    for i in range(3, x + 1):
        for j in range(y - 2):
            if A[i, j] == joueur and A[i, j] == A[i - 1, j + 1] and A[i, j] == A[i - 2, j + 2] and A[i, j] == \
                    A[i - 3, j + 3]:
                return True
    return False


# 2.

def colonnes_vides(A: np.array) -> [int]:
    return [j for j in range(7) if A[0, j] == 0]


# 3.

def jouer_coup(A: np.array, joueur: int, colonne: int) -> np.array:
    assert colonne in colonnes_vides(A)
    i = 5
    while A[i, colonne] != 0:
        i -= 1
    A[i, colonne] = joueur

    return A


# 4.

def invite_coup(A: np.array, joueur: int) -> np.array:
    print(A)
    coup = int(input("Veuillez rentrer le coup à jouer (entre 0 et 6)"))
    while coup not in colonnes_vides(A):
        print("Erreur: La colonne est pleine")
        coup = int(input("Veuillez rentrer le coup à jouer (entre 0 et 6)"))
    return jouer_coup(A, 1, coup)


# 5.

def heuristique(A: np.array) -> float:
    if est_gagnant(A, 1):
        return np.inf
    if est_gagnant(A, 2):
        return -np.inf
    c = 0
    for i in range(6):
        for j in range(6):
            if A[i, j] != 0:
                c += ((-1) ** (A[i, j] + 1)) * HEURISTIQUE[i, j]
    return c


# 6.

def successeurs(A: np.array, joueur: int) -> [np.array]:
    P = colonnes_vides(A)
    R = []
    for i in range(7):
        if i in P:
            B = A.copy()
            T = jouer_coup(B, joueur, i)
            R.append(T)
    return R


# 7.

def minimax(A: np.array, n: int):
    if n == 0 or successeurs(A, 2) == []:
        return heuristique(A)
    mini = np.inf
    for p in successeurs(A, 2):
        s = maximin(p, n - 1)
        if s < mini:
            mini = s
    return mini


def maximin(A: np.array, n: int):
    if n == 0 or successeurs(A, 1) == []:
        return heuristique(A)
    maxi = -np.inf
    for p in successeurs(A, 1):
        s = minimax(p, n - 1)
        if s > maxi:
            maxi = s
    return maxi


# 8

def puissance4(n):
    JEU = np.zeros((6, 7), dtype=int)
    print("Bienvenue dans ce super jeu de puissance 4 où vous allez vous amuser pendant 1h")
    gagnant = 0
    while colonnes_vides(JEU):
        JEU = invite_coup(JEU, 1)
        if est_gagnant(JEU, 1):
            gagnant = 1
            break
        mini = np.inf
        coup = None
        for p in successeurs(JEU, 2):
            s = maximin(p, n)
            if s < mini:
                coup = p
                mini = s
        JEU = coup
        if est_gagnant(JEU, 2):
            gagnant = 2
            break
    if gagnant == 0:
        print("Match nul ...")
    elif gagnant == 1:
        print("Victore de 1 !!!!")
    else:
        print("2 à gagné ...")


puissance4(3)
