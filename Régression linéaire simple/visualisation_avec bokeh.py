"""         Ousmane DIA
@authors:   Abdoulaye Bara DIAW
            Ndeye fatou DIAW
Avril_2020
"""

import numpy as np
from sklearn import linear_model 
from bokeh.plotting import figure
from bokeh.models import Toggle
from bokeh.layouts import layout

#Tableaux de données
xi = [18, 7, 14, 31, 21, 5, 11, 16, 26, 29]
yi = [55, 17, 36, 85, 62, 18, 33, 41, 63, 87]
#Redimensionnement des tableaux
Xi = np.array(xi).reshape(-1, 1)
Yi = np.array(yi).reshape(-1, 1)

# Création du model de regression linéaire
regression = linear_model.LinearRegression()

#Entrainement du model sur les données Xi et Yi
regression.fit(Xi,Yi)

#Utilisation du model pour une prédiction sur les données Xi
pred = regression.predict(Xi)

#Nuage de points et droite de regression linéaire
nuage = figure(plot_width = 500, plot_height = 300, title = "Droite de regression linéaire et corrélation entre Xi et Yi")
nuage.xaxis.axis_label = "Xi"
nuage.yaxis.axis_label = "Yi"
nuage.scatter(xi, yi, size = 10, color = "blue")
droite = nuage.line(xi, pred.flatten(), line_color = "#FC0A05")

#Bouton 
bouton = Toggle(label = "Masquer / Afficher  la droite de regression linéaire", button_type = "success", active = True)
bouton.js_link("active", droite, "visible")

show(layout([nuage], [bouton]))
