from sklearn import datasets
from PIL import Image
import numpy as np

digits = datasets.load_digits()
D0 = digits.data
Y = digits.target


# 1.3

def tableau_gris(D) -> list:
    R = np.empty((D.shape[0], 8, 8))
    for i in range(D.shape[0]):
        R[i] = D[i].reshape(8, 8) * 17
    return R


# 1.4

def affichage(d):
    Image.fromarray(d).show()


# 2.1

def repartition(D, Y):
    donnees = []
    test = []
    presence = [0] * 10
    for i in range(len(D)):
        if presence[Y[i]] < 90:
            donnees.append((D[i], Y[i]))
            presence[Y[i]] += 1
        else:
            test.append((D[i], Y[i]))
    return (donnees, test)


# 2.2

def plus_proches_voisins(donnees, test, i, k):
    def distance(t):
        s = 0
        for a in range(8):
            for b in range(8):
                s += (t[0][a, b] - test[i][0][a, b]) ** 2
        return s ** 0.5

    return sorted(donnees, key=distance)[:k]


(D, Z) = repartition(tableau_gris(D0), Y)

print(plus_proches_voisins(D, Z, 5, 10))

#