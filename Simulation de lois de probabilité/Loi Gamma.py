"""         Ousmane DIA
@authors:   Abdoulaye Bara DIAW
            Ndeye fatou DIAW
Avril_2020
"""

import numpy as np
import matplotlib.pyplot as plt
# Nombre de valeurs à générer
length = 10000
bins=1000

###Données 
data = np.random.gamma(10,5,length)

###Graphe
y, x = np.histogram(data, bins=bins, density=True)
# Milieu de chaque classe
x = (x + np.roll(x, -1))[:-1] / 2.0
plt.figure(figsize=(12,8))
plt.hist(data, bins=1000, density=True)
plt.title("Simulation de la loi Gamma")
plt.show()