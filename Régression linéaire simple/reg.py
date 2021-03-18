"""         Ousmane DIA
@authors:   Abdoulaye Bara DIAW
            Ndeye fatou DIAW
Avril_2020
"""

import matplotlib.pyplot as plt
import pandas as pd

"""-------------------------------------------------------- 
    1_Récupération des données enregistrées au format excel
--------------------------------------------------------"""
tab2 = pd.read_excel("data2.xlsx")
q2 = pd.DataFrame(tab2)
print(q2)
print(q2.describe())

y = q2["Yi"]
x = q2["Xi"]


"""------------------------------------------- 
    2_Représentation des Yi en fonction des Xi
-------------------------------------------"""
plt.scatter(x, y, color = "blue")
plt.title("Degré de dépendance linéaire entre Xi et Yi", color = "orange", size = 14)
plt.xlabel("Xi", color = "black", fontsize = 20)
plt.ylabel("Yi", color = "black", fontsize = 20)
plt.grid()
plt.show()

print("A la vue de cette représentation, nous pouvons soupçonner une liaison linéaire entre les deux variables Xi et Yi")

"""-------------------------------------------------
    3_Coefficients de la droite des moindres carrées
-------------------------------------------------"""
#print(stats.linregress(x,y)) # Voir les stats de la regression
cov = q2.Xi.cov(q2.Yi)
varx = x.var()
a = cov/varx
meanx = x.mean()
meany = y.mean()
b = meany - (a * meanx)
print("\nLes coefficients de la droite des moindres carrées y = ax +b sont: " )
print("a = ", a)
print("b = ", b)
droite = a * x + b

#Représentation de la droite des moindres carrées
plt.plot(x, droite, "orange", x, y, "o", )
plt.title("Droite de regression linéaire et corrélation entre Xi et Yi", color = "blue", size = 14)
plt.xlabel("Xi", color = "black", fontsize = 20)
plt.ylabel("Yi", color = "black", fontsize = 20)
plt.grid()
plt.show()

