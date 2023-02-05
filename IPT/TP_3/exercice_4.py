import time

import matplotlib.pyplot as plt
import numpy as np
import random

from PIL import Image


# 1.

def carre(n: int, p: float) -> np.array:
    return np.array([[0 if random.random() <= p else 255 for j in range(n)] for i in range(n)])


def affichage(M: np.array):
    img = Image.fromarray(M)
    plt.imshow(img)
    plt.show()
