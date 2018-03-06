
#Nötige Imports
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
from time    import sleep

#Erzeugen eines Fensters
win = tk.Tk()

#Titel des Fensters
win.title("Python GUI")

#Ändern des Default Icons (Bugt rum?)
win.iconbitmap('Anderes/py.ico')

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
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='Tab 3')

tabControl.pack(expand= 1, fill="both") #Sichtbar machen der Tabs

#==================================================
#Container,für Widgets:
mighty= ttk.LabelFrame(tab1, text= ' Mighty Python ')
mighty.grid(column=0, row=0, padx=8, pady=4) 

mighty2= ttk.LabelFrame(tab2, text= ' The Snake ')
mighty2.grid(column=0, row=0, padx=8, pady=4) 

#==================================================
#Klassen:

class ToolTip(object):

    def __init__(self, widget):   #Konstruktor
        self.widget = widget
        self.tip_window = None

    def show_tip(self, tip_text):
        "Display text in a tooltip window"
        if self.tip_window or not tip_text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")      # Größe des Widgets
        x = x + self.widget.winfo_rootx() + 25          # Berechnungen zur Darstelung
        y = y + cy + self.widget.winfo_rooty() + 25     # 
        self.tip_window = tw = tk.Toplevel(self.widget) # Neues Tooltip-Fenster
        tw.wm_overrideredirect(True)                    # Alle Windows-Dekorationen entfernen (auf false setzbar)
        tw.wm_geometry("+%d+%d" % (x, y))               # Fenster der gewünschten Größe erstellen
        label = tk.Label(tw, text=tip_text, justify=tk.LEFT,  #Eigenschaften des Tooltips
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()


#==================================================
#Events:

#Event für Tooltips
def create_ToolTip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.show_tip(text)

    def leave(event):
        toolTip.hide_tip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

#Anzeigen einer Messagebox (Versch. Arten von Messageboxen)
def _msgBox():
    msg.showinfo('Fenstername', 'Fensterinhalt \n \u00A9CaptTeemo')
    #msg.showwarning()
    #msg.showerror()
    #answer = msg.askyesnocancel("Fenstertitel","Inhalt") #Returns 1,0 oder NULL

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

#Event für die Spinbox
def _spin():
    value = spin.get()
    #print(value)
    scr.insert(tk.INSERT, value + '\n')  #(param: welche Funktion benutzt wird, Wert)

#Events für Fortschrittsbalken:
def run_progressbar():
    progress_bar['maximum'] = 100
    for i in range(101):
        sleep(0.05)
        progress_bar['value']= i
        progress_bar.update()
    progress_bar['value'] = 0

def start_progressbar():
    progress_bar.start()

def stop_progressbar():
    progress_bar.stop()

def progressbar_stop_after(wait_ms=1000):
    win.after(wait_ms, progress_bar.stop)  #Sleep funktioniert hier nicht

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
help_menu.add_command(label='About', command=_msgBox)
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

#Spinbox (param= Label od. Fenster, Wertebereich von-bis, Größe der Box, Rahmengröße,, Rahmenstyle Event
#         statt from_ + to kann auch values=(0,50,42,100) benutz werden
#         Arten von Bordern: tk.SUNKEN, tk.RAISED, tk.FLAT, tk.GROOVE, tk.RIDGE
spin = Spinbox(mighty, from_=0, to=10, width=5, bd=8, relief=tk.SUNKEN, command=_spin)
spin.grid(column=0, row=2)

#Scrollbarer Text(Param:Größe der Box + Umbruch per Wort)
scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=6, sticky='WE', columnspan=3)

#Container für Labels (param=text, + Feld in der Tabelle, Padding)
buttons_frame = ttk.LabelFrame(mighty2, text=' Labels in a Frame ')
buttons_frame.grid(column=1, row=7) #oder (column=1,padx=20, pady=40 für Mitte)
                
#Labels in Container setzen
ttk.Button(buttons_frame, text="Run Progressbar"    , command= run_progressbar ).grid(column=0, row=0, sticky=tk.W)
ttk.Button(buttons_frame, text="Start Progressbar"  , command= start_progressbar).grid(column=1, row=0, sticky=tk.W)
ttk.Button(buttons_frame, text="Stop immediatly"    , command= stop_progressbar).grid(column=2, row=0, sticky=tk.W)
ttk.Button(buttons_frame, text="Stop after a Second", command= progressbar_stop_after).grid(column=0, row=3, sticky=tk.W)

#Fortschrittsbalken
progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=286, mode='determinate')
progress_bar.grid(column=0, row=3, pady=2)

#Canvas (Selten benutztes Tool zum malen:
tab3_frame = tk.Frame(tab3, bg='blue')
tab3_frame.pack()
for orange_color in range(2):
    canvas = tk.Canvas(tab3_frame, width=150, height=80,
                        highlightthickness=0, bg='orange')
    canvas.grid(row=orange_color, column=orange_color)

#===============================================================================
#Tooltips hinzufügen:

create_ToolTip(scr, 'This is a scrolled Widget')
create_ToolTip(name_entered, 'Please enter your Name')

#===============================================================================
#Start GUI
win.mainloop()
#===============================================================================
