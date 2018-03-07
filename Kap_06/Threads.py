#Grundlegendes:
# Damit die GUI ansprechbar bleibt, obwohl lange Evenst im Hintergrund laufen
# werden Threads verwendet. Diese teilen sich CPU und Arbeitsspeicher. Eine alternative wäre IPC
# Magic happens ab Line 30
# Threads können in Python nicht gestoppt werden
# Es werden Daemons benutzt, die anhalten, wenn der Main-Thread (GUI) in den Hintergrund wechselt
# => Keine Fehler beim Abbruch (Beenden) des Programms

#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
from time    import sleep         

from threading import Thread  #Import für Threads

GLOBAL_CONST = 42

class OOP():
    def __init__(self):       
        self.win = tk.Tk()      
        self.win.title("Python GUI")      
        self.create_widgets()

#=====================================================
##MAGIC:##
    # Ein Thread wird erzeugt
    def create_thread(self):

        self.run_thread = Thread(target=self.method_in_a_thread, args=[8])
        self.run_thread.setDaemon(True) # Abänderung Thread -> Daemon
        self.run_thread.start()
        print(self.run_thread)
        print('createThread():', self.run_thread.isAlive()) #1.)Thread wird geboren

    # Gethreadeter Code, da eine Funktion darüber ein Thread zugewiesen wurde
    def method_in_a_thread(self, num_of_loops=10): 
        print('Hi, how are you?')
        for idx in range(10):         # Langer Code-Teil wird in eigenen Thread ausgelagert!
            sleep(1)                  # !ACHTUNG! Schleife Startet mit jedem Thread neu!
            self.scrol.insert(tk.INSERT, str(idx) + 'n')
        sleep(1)
        print('method_in_a_thread():', self.run_thread.isAlive()) #2.) Thread lebt immer noch


    def click_me(self): #Nicht gethreadeter Code (!Freezed das Fenster!)
        #self.action.configure(text='Hello ' + self.name.get() + ' ' + self.number_chosen.get())
        self.create_thread() # Threadet Code -> kein Freeze

# Bei vorzeitigem Schließen des Fenster wird eine Meldung geworfen, dass
# der Thread nicht im Mainloop liegt -> Umändern von Thread zu Daemon
#=====================================================

    # Exit GUI cleanly
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit() 
                  
    def create_widgets(self):    
        tabControl = ttk.Notebook(self.win)          
        
        tab1 = ttk.Frame(tabControl)            
        tabControl.add(tab1, text='Tab 1')          
        tabControl.pack(expand=1, fill="both")  
  
        mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')
        mighty.grid(column=0, row=0, padx=8, pady=4)
        
        a_label = ttk.Label(mighty, text="Enter a name:")
        a_label.grid(column=0, row=0, sticky='W')
     
        self.name = tk.StringVar()
        self.name_entered = ttk.Entry(mighty, width=24, textvariable=self.name)
        self.name_entered.grid(column=0, row=1, sticky='W')               
        
        self.action = ttk.Button(mighty, text="Click Me!", command=self.click_me)   
        self.action.grid(column=2, row=1)                                
        
        ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)
        number = tk.StringVar()
        self.number_chosen = ttk.Combobox(mighty, width=14, textvariable=number, state='readonly')
        self.number_chosen['values'] = (1, 2, 4, 42, 100)
        self.number_chosen.grid(column=1, row=1)
        self.number_chosen.current(0)
        
        scrol_w = 40; scrol_h = 10                
        self.scrol = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.scrol.grid(column=0, row=3, sticky='WE', columnspan=3)                    
        
        for child in mighty.winfo_children():     
            child.grid_configure(padx=4, pady=2) 
            
        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)
        
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self._quit)
        menu_bar.add_cascade(label="File", menu=file_menu)    
        
        self.name_entered.focus()     
                 
#======================
# Start GUI
#======================
oop = OOP()

oop.win.mainloop()
