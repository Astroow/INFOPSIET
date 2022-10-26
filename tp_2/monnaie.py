EURO = [1, 2, 5, 10, 20, 50, 100, 200, 500]


def plus_grand(S: int, M: list) -> int:
    n = len(M)
    i = 0
    while i < n and M[i] <= S:
        i += 1
    return M[i - 1]


def rendu_glouton(S: int, M: list) -> list:
    R = []
    while S >= M[0]:
        s = plus_grand(S, M)
        S -= s
        R.append(s)
    return R

def rendu_glouton_rec(S: int, M: list) -> list:
  if S < M[0]:
    return []
  s = plus_grand(S, M)
  return [s] + rendu_glouton_rec(S-s, M)
