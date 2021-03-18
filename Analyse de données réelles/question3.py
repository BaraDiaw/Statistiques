"""         Ousmane DIA
@authors:   Abdoulaye Bara DIAW
            Ndeye fatou DIAW
Avril_2020
"""

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

"""------------------------
   1_ Lecture et structure
------------------------"""
fichier = pd.read_excel("data3.xlsx") # Lecture du fichier excel contenant les données
q3 = pd.DataFrame(fichier)
print("-------La structure (lignes,colonnes) est la suivante: ", q3.shape) # Vérification de la structure lignes, colonnes
# Affectation des variables pour faciliter la mainpulation
age = q3["age"]
enfants = q3["n.enfant"]
fratrie = q3["n.fratrie"]
interv = q3["dur.interv"]
prof = q3["prof"]

"""-----------------------------------------------
   2_ Changement des types de certaines variables
-----------------------------------------------"""
"""print("\nTypes originels")
print("\n", q3.dtypes)
"""
# Reconvertion des données
q3["prof"] = q3["prof"].astype("category")
q3["duree"] = q3["duree"].astype("category")
q3["discip"] = q3["discip"].astype("category")
q3["ecole"] = q3["ecole"].astype("category")
q3["separation"] = q3["separation"].astype("category")
q3["juge.enfant"] = q3["juge.enfant"].astype("category")
q3["place"] = q3["place"].astype("category")
q3["abus"] = q3["abus"].astype("category")
q3["grav.cons"] = q3["grav.cons"].astype("category")
q3["dep.cons"] = q3["dep.cons"].astype("category")
q3["ago.cons"] = q3["ago.cons"].astype("category")
q3["ptsd.cons"] = q3["ptsd.cons"].astype("category")
q3["alc.cons"] = q3["alc.cons"].astype("category")
q3["subst.cons"] = q3["subst.cons"].astype("category")
q3["scz.cons"]= q3["scz.cons"].astype("category")
q3["char"] = q3["char"].astype("category")
q3["rs"] = q3["rs"].astype("category")
q3["ed"] = q3["ed"].astype("category")
q3["dr"] = q3["dr"].astype("category")
q3["suicide.hr"] = q3["suicide.hr"].astype("category")
q3["suicide.past"] = q3["suicide.past"].astype("category")

print("\n-------Nouveaux types de données-------")
print(q3.dtypes)

"""-----------------------------------------------------------------------------
   3_ Moyenne, Variance, Ecart-type et 3 premiers quantiles de la variables age
-----------------------------------------------------------------------------"""
# Variable age
print("\n------------Agrégats de la variable age------------")
print("  Moyenne = ", age.mean())
print("  Variance = ", age.var())
print("  Ecart-type = ", age.std())
# Variable n.enfant
print("\n------------Agrégats de la variable n.enfant------------")
print("  Moyenne = ", enfants.mean())
print("  Variance = ", enfants.var())
print("  Ecart-type = ", enfants.std())
# Variable n.fratrie
print("\n------------Agrégats de la variable n.fratrie------------")
print("  Moyenne = ", fratrie.mean())
print("  Variance = ", fratrie.var())
print("  Ecart-type = ", fratrie.std())
# Variable n.interv
print("\n------------Agrégats de la variable n.interv------------")
print("  Moyenne = ", interv.mean())
print("  Variance = ", interv.var())
print("  Ecart-type = ", interv.std())

# Trois premiers quantiles de la variable age
print("\n----Trois premiers quantiles de la variable age----")
print("\n DESCRIPTION") 
print(age.describe())
print("\nEn voyant la description ci-dessus nous pouvons déduire que les premier, deuxième et troisième quantiles de la variable age sont respectivement: 28, 37 et 48")

"""
Q1 = age.quantile([0.25])# Le premier quantile  Q1
Q2 = age.quantile([0.50])# Le deuxième quantile  Q2
Q3 = age.quantile([0.75])# le troisième quartile Q3
print("Le premier quantile de la variable age est: ", Q1)
print("Le premier quantile de la variable age est: ", Q2)
print("Le premier quantile de la variable age est: ", Q3)
"""

"""----------------------------------------------
    4_ Boxplot de la variable age et conclusions
----------------------------------------------"""
# Boxplot
age.plot.box(vert = False, grid = True, figsize = (10,5))
plt.title("Boxplot de la variable age", c= "blue")
plt.show()
# Conclusions
print("\nD'après le boxplot ci-dessus nous pouvons conclure :")
print("- Les prisonniers de cette étude ont entre 19 et 83 ans")
print("- 25% des prisonniers sont âgés entre 19-28ans")
print("- 25% des prisonniers sont âgés entre 28-37ans")
print("- 25% des prisonniers sont âgés entre 37-48ans")
print("- 25% des prisonniers sont au moins âgés de 48ans")
print("- Les données sont beaucoup plus dispersées dans le dernier quart(au moins âgés de 48ans) que dans les autres")

"""------------------------------------------------------------------------
    5_ Aﬃchage des données pour les agriculteurs qui ont plus de 2 enfants
------------------------------------------------------------------------"""
print("\n-----Le tableau ci-dessous présente les informations des agriculteurs qui ont plus de 2 enfants-----")
d5 = q3[(enfants > 2 ) & (prof == "agriculteur")]
print(d5)

"""-----------------------------------------------------------------------------------------------------
    6_ Calcule des fréquences des modalités de la variable prof et détermination de la catégorie modale
-----------------------------------------------------------------------------------------------------"""
valeurProf = prof.values
eff = prof.value_counts()#On inclut pas les valeurs 'NaN'
total = eff.sum()
freq = (eff/total)*100 # calcul de la fréquence (en %)
print("\n-------Fréquences des modalités de la variables prof-------")
print(freq)
print("Le tableau ci-dessous montre que la catégorie modale de cette variable est 'ouvrier' avec 28.62% des prisonniers ")
print("Cela peut être réconforter par le diagramme ci-dessous")
mod = {"Fonctions": ["ouvrier", "sans emploi", "employe", "artisan", "prof.intermediaire", "autre", "cadre", "agriculteur"],
       "Nombres": [227, 222, 135, 90, 58, 31, 24, 6]
       }
modal = pd.DataFrame(mod)
px.bar(modal, x = 'Fonctions', y = 'Nombres')

"""---------------------------------------------
    7_ Diagramme circulaire de la variable prof
---------------------------------------------"""
print("\n-------Diagramme circulaire de la variable prof-------")
fonction = ["Ouvrier", "Sans emploi", "Employé", "Artisan", "Prof.intermediaire", "Autre", "Cadre", "Agriculteur"]
nombre = [227, 222, 135, 90, 58, 31, 24, 6]
couleurs = ["#FF00FF", "#FF0000", "#1E88E5", "#FFFF00", "#00FFFF", "#FF8000", "#7BFF00", "#0000FF"]
fig, ax = plt.subplots(figsize=(10,5))
plt.pie(nombre, labels = None, shadow = True, colors = couleurs, autopct="%1.1f%%")
plt.title("Les professions des prisonniers de cette étude")
plt.axis("equal")
plt.legend(fonction,loc='upper right') 
plt.show()

"""-----------------------------------------
    8_ Les moyennes des âges par profession
-----------------------------------------"""
# Supprimer les colonnes dont on a pas besoin
newq3 = q3.drop(["duree", "discip", "ecole", "separation", 
              "juge.enfant", "place", "abus", "grav.cons", 
              "dep.cons", "ago.cons", "ptsd.cons", "alc.cons", 
              "subst.cons", "scz.cons", "char", "rs", "ed", "dr", 
              "suicide.hr", "suicide.past", "n.enfant", "n.fratrie", 
              "dur.interv", "suicide.s"], axis = 1)

print("\n-------Les moyennes d'âges des prisonniers selon leur fonction-------")
#Utilisation de la fonction "groupby" pour regrouper les différents éléments de la variable prof
print(newq3.groupby(["prof"]).mean())

"""---------------------------------------------------------------------
    9_ La table des eﬀectifs pour la variable prof incluant les "NaN"
---------------------------------------------------------------------"""
print("\n-----Table des eﬀectifs pour la variable prof incluant les 'NaN'-----")
print("\n", prof.value_counts(dropna = False))

"""---------------------------------------------
    10_ Le nombre de "Nan" pour chaque variable
---------------------------------------------"""
print("\n-------Le nombre de 'Nan' pour chaque variable-------")
print(q3.isnull().sum())

"""-------------------------------------------------------
    11_ Suppression toutes les lignes contenant des "Nan"
-------------------------------------------------------"""
print("\n-----Table de données ne contenant pas les données manquantes 'Nan' -----")
cleaned = q3.dropna( axis = 0)
print(cleaned)

"""----------------------------------------------------------------------
    12_ L'histogramme et la densité de la variable age sur la même ﬁgure
----------------------------------------------------------------------"""
p = sns.distplot(cleaned["age"], bins = 20, color = "blue", kde_kws = {"color": "orange", "lw": 2})# Utilisation de seaborn
plt.xlabel("Âges des prisonniers", color = "red")
plt.title("Représentation et densité de la variable age", color = "red")
fig = plt.gcf()#Taille de la figure
fig.set_size_inches(14, 4)
plt.legend()
plt.show()

"""------------------------------------
    13_ Discrétisation la variable age
------------------------------------"""
minAge = 19
maxAge = 83
Q1 = 28  
Q2 = 37
Q3 = 48
q3["age_classe"] = pd.cut(q3.age, bins = [19, 28, 37, 48, 83], labels = ["19-28", "28-37","37-48" ,"48-83"])
print("\n-------Nouvelle table de données contenant la variable 'age_classe' ------")
print("\n", q3)
"""---------------------------------------------------------------------
    14_ Les fréquences des modalités de la nouvelle variable age_classe
---------------------------------------------------------------------"""
print("\n-------Les fréquences des modalités de la nouvelle variable age_classe-------")
ageCl = q3["age_classe"] 
print(ageCl.value_counts())