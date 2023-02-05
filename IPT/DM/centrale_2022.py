import turtle


# 1

def longueur1(c: [str], d: int) -> int:
    L = 0
    for e in c:
        if e == "A":
            L += d
    return L


# 2

# ["A", "A", "D", "A"]
# nbg est le nombre de fois qu'il faut tourner à gauche avant d'avancer pour le prochaine fois

# 3

# représentation_minimale est une fonction qui transforme un circuit donné en entrée en conservant le chemin mais en
# supprimant les doublons tels que des enchainements de D et G qui se compenseraient

# 4

def contient_demi_tour1(c: [str]) -> bool:
    for i in range(len(c)):
        if i < len(c) - 1 and c[i] == c[i + 1] and c[i] != "A":
            return True
    return False


# 5

def est_ferme1(c: [str]) -> bool:
    o = 0
    for e in c:
        if e == "G":
            o = (o - 1) % 4
        elif e == "D":
            o = (o + 1) % 4
    if o == 0:
        return True
    return False


# 6

def circuit_convenable1(c: [str]) -> bool:
    return not contient_demi_tour1(c) and est_ferme1(c)


# 7

def dessine_circuit1(c: [str], d: int) -> None:
    turtle.pendown()
    for e in c:
        if e == "A":
            turtle.forward(d)
        elif e == "D":
            turtle.right(90)
        else:
            turtle.left(90)
    turtle.penup()


# 8

def element_valide2(e) -> bool:
    return (type(e) == int and e > 0) or (type(e) == tuple and type(e[0]) == int and e[0] > 0 and type(e[1]) == int and
                                          -360 < e[1] < 360)


# 9

def dessine_circuit2(c: list, echelle: float) -> None:
    turtle.pendown()
    for e in c:
        if type(e) == int:
            turtle.forward(e * echelle)
        else:
            if e[1] > 0:
                turtle.circle(e[0] * echelle, e[1])
            else:
                turtle.circle(-e[0] * echelle, -e[1])
    turtle.penup()



