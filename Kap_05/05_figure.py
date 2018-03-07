
# Imports:
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Erstellen des Figure Objekts
fig = Figure(figsize=(12, 8), facecolor='white')

# Hinzufügen der zu plottenden Graphen
axis = fig.add_subplot(111)  # (param= Reihen mit Plot-Fenstern, Spalten mit Plot-Fenstern , Rangordnung des Plots) 
#axis = fig.add_subplot(211) 
    
#__________________________________________________________________________
# Eigentlicher Code für die Graphen
xValues = [1,2,3,4]
yValues = [5,7,6,8]
yValues1 = [5.5,6.5,50,6] 

#--------------------------------------------------------------
#Dynamische Anpassung der Graphen:
yAll = [yValues, yValues1]
# Kleinstes Y aus allen Listen zurückgeben
minY = min([y for yValues in yAll for y in yValues])

yUpperLimit = 20
# Maximum berechnen, solange dieses unter Ultimatum-Max liegt
maxY = max([y for yValues in yAll for y in yValues if y < yUpperLimit])
#--------------------------------------------------------------

# Plotten der Graphen
t0, = axis.plot(xValues, yValues, color= 'red')    # Legende für diese Linie + Ändern der Farbe
t1, = axis.plot(xValues, yValues1, color= 'blue') 
# Variablenname, muss mit Komma (,) sein, damit auch Tupel übergeben werden können
#__________________________________________________________________________

axis.set_ylim(minY, maxY) # Darstellung in y-Achse beschränken (param= von-bis)
axis.set_xlim( min(xValues), max(xValues))


axis.plot(xValues, yValues)          # Plotten des Graphen
axis.set_xlabel('Horizontal Label')  # Beschr. x-Achse
axis.set_ylabel('Vertical Label')    # Beschr. y-Achse            
axis.grid(linestyle='-')             # Ändern des Linienstyles  

fig.legend((t0, t1), ("Nameof_Line", "Name2"),'upper left')  # (param= Variable, Beschriftung, Ort)
# Bug? zeigt nur den ersten Buchstaben des Namens an bei nur einer Linie

#--------------------------------------------------------------
# Erzeugen des GUI Objekts + Ordnungsgemäßes löschen
def _destroyWindow():
    root.quit()
    root.destroy()

root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindow)

#--------------------------------------------------------------
#Zeichnen der Canvas, auf der der Plot dargestellt wird
canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
#--------------------------------------------------------------
# Starten der GUI
root.update()
root.deiconify()
root.mainloop()