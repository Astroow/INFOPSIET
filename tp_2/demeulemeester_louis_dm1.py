import numpy as np

# Exercice 2 : Résolution par programmation gloutonne

# 1.

def plus_grand(S: int, M: list) -> int:
    n = len(M)
    i = 0
    while i < n and M[i] <= S:
        i += 1
    return M[i - 1]

# 2.

def rendu_glouton(S: int, M: list) -> list:
    R = []
    while S >= M[0]:
        s = plus_grand(S, M)
        S -= s
        R.append(s)
    return R

# 3. M[0] est un entier positif. La suite (S) est une suite récurrente: S(n+1) = S(n) - plus_grand(S(n), M) où plus_grand(S(n), M) renvoie un entier positif strictement, donc la suite est décroissante. Donc il existe un rang n0 (i.e. un tour de boucle) tel que S(n0) <= M[0] ce qui prouve la terminaison de la fonction.

# 4.

def rendu_glouton_rec(S: int, M: list) -> list:
  if S < M[0]:
    return []
  s = plus_grand(S, M)
  return [s] + rendu_glouton_rec(S-s, M)

# 5. On peut prendre M = [1, 6, 8] et S = 12. L'algorithme glouton donne [8, 1, 1, 1, 1] alors que la solution optimale est [6, 6].


# Exercice 3 : Résolution par programmation dynamique

# 1. L'algorithme glouton donne: [4, 1, 1] alors que la solution optimale est [3, 3].

# 2. Pour le système de monnaie [1, 3, 4], on a le tableau suivant:
# \|1 3 4
# 0|0 0 0
# 1|1 1 1
# 2|2 2 2
# 3|3 1 1
# 4|4 2 1
# 5|5 3 2
# 6|6 2 2
# La solution optimale donnée par la programmation dynamique est [3, 3].

# 3.

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

# 4.

def rendu_bas_haut_reconst(S: int, M: list) -> list:
  R = []
  _, T = rendu_bas_haut(S, M)
  i, j = np.shape(T)[0]-1, np.shape(T)[1]-1
  while T[i, j] != 0:
    if j != 0 and T[i, j] == T[i, j-1]:
      j -= 1
    else:
      R.append(M[j])
      i -= M[j]
  return R

# 5.

def rendu_rec(S: int, M: list) -> int:
  i = S
  if len(M) == 1:
    return i
  j = M[len(M)-1]
  if j <= i:
    return min(1 + rendu_rec(i-j, M), rendu_rec(i, M[:len(M)-1]))
  return rendu_rec(i, M[:len(M)-1])

# 6.

MEMO = {}

def rendu_dyn_memo(S: int, M: list) -> int:
  i = S
  if len(M) == 1:
    return i
  j = M[len(M)-1]
  if (i, j) in MEMO:
    return MEMO[(i, j)]
  if j <= i:
    MEMO[(i, j)] = min(1 + rendu_dyn_memo(i-j, M), rendu_dyn_memo(i, M[:len(M)-1]))
    return MEMO[(i, j)]
  MEMO[(i, j)] = rendu_dyn_memo(i, M[:len(M)-1])
  return MEMO[(i, j)]
