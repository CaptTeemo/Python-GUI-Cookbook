
# Grundlegender Aufbau:
# Tkinter baut die GUI nach Columns und Row auf, wie eine Excel-Tabelle
# Die Länge(width) der Spalten ist abhängig vom Größten Element
# Mit (columnspan), kann ein Objekt mehrere Spalten Umfassen)
# Tkinter benutzt automatisch die nächste Reihe, falls keine angegeben ist
# Falls der Parameter (sticky=tk.W, oder sticky='WE' usw.) gesetzt ist wird das Objekt nicht zentriert
# ein Container (LabelFrame) kann als Tabelle in einer weiteren Tabelle angesehen werden
# die Zählung iinnerhalb der Containers beginnt dann wieder bei 0,0.


#Nötige Imports
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu

#Erzeugen eines Fensters
win = tk.Tk()

#Titel des Fensters
win.title("Python GUI")

#Deaktivieren der Veränderbarkeit in Länge + Breite
win.resizable(False, False) 

#Vordefinierte Farben
#Übersicht unter: http://www.tcl.tk/man/tcl8.5/TkCmd/colors.htm
colors = ["Blue", "Gold", "Red"] 
BLUE = "Blue"
GOLD = "Gold"
RED = "Red"

#==================================================
# Tabs:
tabControl = ttk.Notebook(win)         #TabController erstellen
tab1 = ttk.Frame(tabControl)           #Tabs hinzufügen
tabControl.add(tab1, text='Tab 1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')

tabControl.pack(expand= 1, fill="both") #Sichtbar machen der Tabs

#==================================================
#Container,für Widgets:
mighty= ttk.LabelFrame(tab1, text= ' Mighty Python ')
mighty.grid(column=0, row=0, padx=8, pady=4) 

mighty2= ttk.LabelFrame(tab2, text= ' The Snake ')
mighty2.grid(column=0, row=0, padx=8, pady=4) 

#==================================================
#Events:

#Beenden der GUI
def _quit():      #Unterstrich(_) Zeigt private Funktion an
    win.quit()
    win.destroy()
    exit()

def radCall():
    radSel=radVar.get()
    if   radSel == 0: mighty2.configure(text= 'BLUE')
    elif radSel == 1: mighty2.configure(text= 'GOLD')
    elif radSel == 2: mighty2.configure(text= 'RED')

#Event-Funktion für den Button
def click_me():
	action.configure(text="Hello " + name.get() + ' ' + number.get())

#==================================================
#Menüs:

#Menubar erzeugen
menu_bar= Menu(win)
win.config(menu=menu_bar)
#Einträge erzeugen + Untermenüpunkte anlegen
file_menu = Menu(menu_bar, tearoff=0)        #tearoff: entfernt hässlichen Strich (gedacht um ein Menü abzudocken)
file_menu.add_command(label='New')
#file_menu.add_separator()                   #Seperator-Linie
file_menu.add_command(label='Exit', command=_quit)
menu_bar.add_cascade(label='File', menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)      
menu_bar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About')
#==================================================

#Label 
a_label = ttk.Label(mighty, text= "Enter a Name:")
a_label.grid(column =0, row=0)

#2tes Label
ttk.Label(mighty, text="Choose a Number: ").grid(column=1, row=0)
number = tk.StringVar()

#Textbox 
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column= 0, row=1, sticky=tk.W)
name_entered.focus() #Focus auf das Name Feld mit Eingabe

#Button (param: disabled)
action=ttk.Button(mighty,text= "Click Me!", command=click_me)
action.grid(column =2, row =1)
#action.config(state='disabled') #Disablen eines Buttons

#Checkbuttons(1. Nicht Drückbar, 2.Standard, 3.Kreuz bereits drinnen)
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty2, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty2, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty2, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

#Combobox (param:Read-only)
number_chosen= ttk.Combobox(mighty, width=12, textvariable= number, state='readonly')
number_chosen['values'] = (1,2,42,100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

#Radiobuttons
#Erstellen der Radiobuttons + Eventkommando beim drücken
# radVar = tk.IntVar()

# rad1 = tk.Radiobutton(mighty, text=BLUE, variable=radVar, value=1, command=radCall)
# rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)   

# rad2 = tk.Radiobutton(mighty, text=GOLD, variable=radVar, value=2, command=radCall)
# rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)  

# rad3 = tk.Radiobutton(mighty, text=RED, variable=radVar, value=3, command=radCall)
# rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

#Radiobuttons in einer Schleife erstellen
radVar = tk.IntVar() #Eine Variable für 3 Buttons
radVar.set(99)  #Index, der nicht besetzt ist                               
for col in range(3):                             
	curRad = tk.Radiobutton(mighty2, text=colors[col], variable=radVar, value=col, command=radCall)
	curRad.grid(column=col, row=5, sticky=tk.W) 

#Scrollbarer Text(Param:Größe der Box + Umbruch per Wort)
scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=6, sticky='WE', columnspan=3)

#Container für Labels (param=text, + Feld in der Tabelle, Padding)
buttons_frame = ttk.LabelFrame(mighty2, text=' Labels in a Frame ')
buttons_frame.grid(column=1, row=7) #oder (column=1,padx=20, pady=40 für Mitte)
                
#Labels in Container setzen
ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, sticky=tk.W)


#===============================================================================
#Start GUI
win.mainloop()
#===============================================================================
