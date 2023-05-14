from numpy.polynomial import Polynomial

# a.
def prod_scal(p: Polynomial, q: Polynomial):
    pq = p*q
    pq_integ = pq.integ()
    return pq_integ(1)-pq_integ(0)

# b.
MEMO = {0: Polynomial([1])}
def calc_Q(deg: int) -> Polynomial:
    if deg in MEMO:
        return MEMO[deg]
    X = Polynomial([0 for _ in range(deg)] + [1])
    Q = X - sum([prod_scal(X, calc_Q(i))*calc_Q(i) for i in range(deg)])
    MEMO[deg] = Q
    return Q

for i in range(6):
    print(f"Q{i}: {calc_Q(i)}")

"""
Résultats:
Q0: 1.0
Q1: -0.5 + 1.0·x
Q2: -0.29166667 - 0.08333333·x + 1.0·x²
Q3: -0.19001736 - 0.06857639·x - 0.07708333·x² + 1.0·x³
Q4: -0.1337982 - 0.05635346·x - 0.06565879·x² - 0.06455522·x³ + 1.0·x⁴
Q5: -0.09943286 - 0.04697661·x - 0.05629511·x² - 0.05650612·x³ - 0.05426965·x⁴ + 1.0·x⁵
"""
