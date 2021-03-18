"""         Ousmane DIA
@authors:   Abdoulaye Bara DIAW
            Ndeye fatou DIAW
Avril_2020
"""

from scipy import random
import numpy as np
import matplotlib.pyplot as plt
a=0
b=1
N=10000
"""Définition de la fonction"""
def func(x):
     return np.sqrt(1-(x)**2)
"""Calcule de l'aire"""
areas = []
for i in range (N):
    xrand=np.zeros(N)
    for i in range(len(xrand)):
        xrand[i] = random.uniform(a,b)
        integral =0.0
    for i in range(N):
        integral += func(xrand[i])
        answer = (b-a)/float(N)*integral
        areas.append(answer)
plt.title("Distribution d'aire avec MonteCarlo sous python")
plt.hist(areas, bin=30, ec="black")
plt.xlabel("Areas")


