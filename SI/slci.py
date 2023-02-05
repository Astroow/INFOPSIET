import math
import matplotlib.pyplot as plt

# 1
def s(tw0: float, z: float) -> float:
    if z < 1:
        return 1-((math.exp(-z*tw0)*math.sin(tw0*math.sqrt(1-z**2)+math.asin(math.sqrt(1-z**2))))/math.sqrt(1-z**2))
    elif z == 1:
        return 1-(1+tw0)*math.exp(-tw0)
    return 1+((math.exp(-tw0*(z+math.sqrt(z**2 - 1))))/(2*(z*math.sqrt(z**2 - 1)+z**2 - 1)))-((math.exp(-tw0*(z-math.sqrt(z**2 - 1))))/(2*(z*math.sqrt(z**2 - 1)-z**2 +1)))

# 2 / 3
def trace(tw0_g: float, tw0_d: float, n: int, z_g: float, z_d: float, step: float):
    TW0 = [tw0_g+i*(tw0_d-tw0_g)/n for i in range(n)]
    M = int((z_d-z_g)/step)
    Z = [round(z_g+i*step, 2) for i in range(M+1)]
    for z in Z:
        S = []
        for tw0 in TW0:
            S.append(s(tw0, z))
        plt.plot(TW0, S, label=f"z = {z}")
    plt.legend(loc='upper right')
    plt.show()

# 2 trace(0, 10, 50, 1, 10, 1)
# 3 trace(0, 10, 50, 0.1, 1, 0.1)

# 4
def est_dans_bande(v: float, vf: float) -> bool:
    return vf*0.95 <= v <= vf*1.05

# 5