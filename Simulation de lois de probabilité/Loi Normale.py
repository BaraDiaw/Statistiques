"""         Ousmane DIA
@authors:   Abdoulaye Bara DIAW
            Ndeye fatou DIAW
Avril_2020
"""

import numpy as np
import matplotlib.pyplot as plt

mu = 3
sigma = 4

data = np.random.randn(10000) * sigma + mu

hx, hy, _ = plt.hist(data, bins=50, normed=0,color="green")

plt.ylim(0.0,max(hx)+0.05)
plt.title('Generer des valeurs aléatoires depuis depuis une loi normale avec python')
plt.grid()

plt.savefig("numpy_random_numbers_normal_distribution.png", bbox_inches='tight')
plt.show()
