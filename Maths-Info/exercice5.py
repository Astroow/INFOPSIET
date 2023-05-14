from numpy.polynomial import Polynomial

# a.
def prod_scal(p: Polynomial, q: Polynomial):
    pq = p*q
    pq_integ = pq.integ()
    return pq_integ(1)-pq_integ(0)

# c.
MEMO = {0: Polynomial([1])}
def calc_Q(deg: int) -> Polynomial:
    if deg in MEMO:
        return MEMO[deg]
    X = Polynomial([0 for _ in range(deg)] + [1])
    Q = X - sum([prod_scal(X, calc_Q(i))*calc_Q(i)/prod_scal(calc_Q(i), calc_Q(i)) for i in range(deg)])
    MEMO[deg] = Q
    return Q

B = [calc_Q(i) for i in range(6)]

"""
Résultats:
Q0: 1.0
Q1: -0.5 + 1.0·x
Q2: 0.16666667 - 1.0·x + 1.0·x²
Q3: -0.05 + 0.6·x - 1.5·x² + 1.0·x³
Q4: 0.01428571 - 0.28571429·x + 1.28571429·x² - 2.0·x³ + 1.0·x⁴
Q5: -0.00396825 + 0.11904762·x - 0.83333333·x² + 2.22222222·x³ - 2.5·x⁴ + 1.0·x⁵
"""

# d.

for Q in B:
    racines = Q.roots()
    Qd = Q.deriv()
    for racine in racines:
        if not(0<racine<1 and Qd(racine) != 0):
            print("Vérification ratée", racine, Q)
            break

"""
Racines:
Q0: []
Q1: [0.5]
Q2: [0.21132487 0.78867513]
Q3: [0.11270167 0.5        0.88729833]
Q4: [0.06943184 0.33000948 0.66999052 0.93056816]
Q5: [0.04691008 0.23076534 0.5        0.76923466 0.95308992]
"""

# Conjecture validée

# e.
