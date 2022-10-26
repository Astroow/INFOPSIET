import matplotlib.pyplot as plt
import random

from time import time
from tp_2.monnaie import *
from tp_2.monnaie_dyna import *

def test_opti(Smax: int):
  M = [1, 2, 5, 10, 20, 50, 100, 200, 500]

  X, Yg, Yd = [], [], []
  
  for s in range(Smax):
    X.append(s)
    t = time()
    rendu_glouton(s, M)
    Yg.append(time()-t)
    t = time()
    rendu_dyn_memo(s, M)
    Yd.append(time()-t)

  plt.plot(X, Yg, label="Glouton")
  plt.plot(X, Yd, label="Dynamique")
  plt.legend()

  plt.show()

def test_non_opti(n):
  c = 0
  
  for i in range(n+1):
    M = [1] + [random.randint(1, 100) for j in range(10)]
    M.sort()
    if len(rendu_glouton(200, M)) == rendu_bas_haut(200, M)[0]:
      c += 1
  return c/n*100