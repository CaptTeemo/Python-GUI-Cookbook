# Grundlegende Informationen:
# Tkinter benutzt eigene Datentypen, die leicht von den gewohnten Datentypen abweichen.
# Diese sind: StringVar(), IntVar(), DoubleVar()-> entspricht float und BooleanVar()

import tkinter as tk
from tkinter import Spinbox
 
# Erzeugen von Globalen Variablen auf Modul-Ebene
# Module in Python sind inoffizielle Namespaces
# Python kennt eig. keine Konstanten -> keine Warnungen, wenn GlobaleVar verändert werden

GLOBAL_CONST =42  #C-Style


win=tk.Tk()

# Zuweisung
strData = tk.StringVar()
# Setzen der Daten
strData.set('Hello StringVar')
# Umwandlung: stringVar() -> string
varData = strData.get()

print(varData)
# Ausgabe der Defaultwerte (PY_VAR1 usw..)
# Auch die Zuweisung zu einer Python Variablen würde daran nichts ändern
# Erst nach Aufruf der get() Methode wird der Wert zu 0
print(tk.IntVar())
print(tk.DoubleVar())
print(tk.BooleanVar())

#Daten von einem Widget erhalten
#Widget:

spin = Spinbox(win, width=5, bd=8)
spin['values'] = (1, 2, 4, 42, 100)
spin.grid(column=0, row=2)

strData = spin.get()
print("Spinbox value: " + strData)

def usingGlobal():
    global GLOBAL_CONST   # Hinweis, dass die globale Variable verwendet werden soll
    print(GLOBAL_CONST)   # Ansonsten, Fehler, weil Variable nicht im Namespace
    GLOBAL_CONST=777
    print(GLOBAL_CONST)

usingGlobal()

#======================
# Start GUI
#======================
win.mainloop()