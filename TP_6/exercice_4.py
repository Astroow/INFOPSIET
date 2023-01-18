# 1.

dico_chomp = {
    0: [1, 2, 3, 4, 5],
    1: [4, 5, 6],
    2: [1, 3, 4, 5],
    3: [5, 6, 7, ],
    4: [7, 8],
    5: [8],
    6: [5, 7],
    7: [8],
    8: []
}


# 2.

def sans_nimber(dico_jeu: dict, dico_nimb: dict) -> int:
    for s in dico_jeu:
        if s not in dico_nimb.keys():
            flag = True
            for su in dico_jeu[s]:
                if su not in dico_nimb.keys():
                    flag = False
    return None


# 3.

def chercher_nimber(L: [int]) -> int:
    if (min(L) - 1) >= 0:
        return min(L) - 1
    return max(L) + 1


print(sans_nimber(dico_chomp, {1: 5, 2: 4}))
