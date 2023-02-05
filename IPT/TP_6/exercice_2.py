# 1.

dico_jeu = {
    (0, 1): [(1, 2), (2, 2)],
    (1, 2): [(3, 1), (4, 1)],
    (2, 2): [(3, 1), (5, 1)],
    (3, 1): [(6, 2)],
    (4, 1): [(6, 2), (7, 2)],
    (5, 1): [],
    (6, 2): [],
    (7, 2): [(5, 1)]
}


# 2.

def bibarti(dico: dict) -> bool:
    for so in dico:
        for su in dico[so]:
            if so[1] == su[1]:
                return False
    return True


# 3.

def inverse(dico: dict) -> dict:
    assert bibarti(dico)
    inv = {}
    for so in dico:
        inv[so] = []
    for so in dico:
        for su in dico[so]:
            inv[su].append(so)
    return inv


# 4.

def etat_final(dico: dict, joueur: int) -> [(int, int)]:
    gagnants = []
    for so in dico:
        if so[1] != joueur and dico[so] == []:
            gagnants.append(so)
    return gagnants


# 5.

def attracteur(dico: dict, joueur: int) -> [(int, int)]:
    attracteurs = [s for s in etat_final(dico_jeu, joueur)]
    dico_inv = inverse(dico)
    flag = True
    while flag:
        flag = False
        for a in attracteurs:
            for s in dico_inv[a]:
                if s not in attracteurs:
                    if s[1] == joueur:
                        attracteurs.append(s)
                        flag = True
                    else:
                        drap = True
                        for su in dico[s]:
                            if su not in attracteurs:
                                drap = False
                        if drap:
                            attracteurs.append(s)
                            flag = True
    return attracteurs


# 6.

def strategie_gagnante(dico: dict, joueur: int) -> {(int, int): [(int, int)]}:
    strategie = {}
    attracteurs = attracteur(dico, joueur)
    for s in dico:
        if s[1] == joueur:
            if s in attracteurs:
                strategie[s] = [su for su in dico[s] if su in attracteurs]
            else:
                strategie[s] = []
    return strategie


print(attracteur(dico_jeu, 2))