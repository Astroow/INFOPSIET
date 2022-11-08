import matplotlib.pyplot as plt
import numpy as np

plt.clf()

rho = 7900.0  # kg/m^3
lamda = 25.0  # W/m/K
cp = 450.0  # J/kg/K
L = 0.1  # m
Ti = 0.0  # +273.15 K
T0 = 1000.0  # +273.15 K
TL = 1.0  # +273.15 K
N = 80
tmax = 500.0  # s
idisplay = 80  # Fréquence d'affichage des courbes
D = lamda / (rho * cp)  # diffusivite
print('D[m^2/s]=', D)

# Maillage spatial

x = np.array([i * L / N for i in range(N + 1)])
dx = L / N
print('dx[m]=', dx)

beta = 0.999  # coefficient de sécurité numérique
dtstab = beta * dx ** 2 / (2.0 * D)
print("dtstab[s]=", dtstab)
nbfourier = D * dtstab / dx ** 2  # nombre de fourier adimensionnel
print("nbfourier=", nbfourier)

nbstep = int(tmax / dtstab)

TA = Ti * np.linspace(1, 1, N + 1)
TB = Ti * np.linspace(1, 1, N + 1)

plt.plot(x, TA)

for istep in range(1, nbstep):
    print('Temps=', istep * dtstab)

    for i in range(1, N):
        TB[i] = nbfourier * TA[i - 1] + (1 - 2 * nbfourier) * TA[i] + nbfourier * TA[i + 1]

    TB[0] = T0
    TB[N] = TL

    if istep % idisplay == 0:
        plt.xlabel('x [m]')
        plt.ylabel('T [C]')
        plt.grid(True)
        plt.plot(x, TB, color=plt.get_cmap('jet')(float(istep) / float(nbstep)))
    TA = TB.copy()

plt.show()
