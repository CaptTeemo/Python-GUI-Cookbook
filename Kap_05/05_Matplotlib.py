# Grundlegendes:
# Zur Verwendung dieser Dateien müssen wheel und matplotlib installiert sein
# 1.) pip install wheel
# 2.) Richtige! Matplotlib-Version als .whl-Datei herunterladen und mit pip installieren
# 3.) Falls Instalation abbricht: Visual C++ installieren (benötigte Pakete werden mit pip automatisch mitinstalliert)

#Imports:
# import numpy as np
# import matplotlib.pyplot as plt
# from pylab import show

#Mit dieser Schreibweise werden keine Modulangaben (np. , plt.) benötigt
from pylab import show, arange, sin, plot, pi 

#Plot
t = arange(0.0, 2.0, 0.01)  #Numpy Reichweiten Operator
s = sin( 2 * pi * t)
plot(t, s)

show()                     #Plotten des Graphen