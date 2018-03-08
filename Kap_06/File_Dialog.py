#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
from time import  sleep         
#import Kap_04.ToolTip as tt

from threading import Thread
from queue import Queue

import Queues as bq

from tkinter import filedialog as fd  #Neue Imports
from os import path, makedirs

# Module level GLOBALS
GLOBAL_CONST = 42
fDir   = path.dirname(__file__)     #Standardpfad
netDir = fDir + '\\Backup' 
if not path.exists(netDir):
    makedirs(netDir, exist_ok = True) 

#=====================================================
class OOP():
    def __init__(self):       
        self.win = tk.Tk()          
        self.win.title("Python GUI")  
        
        self.gui_queue = Queue() 
            
        self.create_widgets()
        
        self.defaultFileEntries()

    def defaultFileEntries(self):         #Alternative zum setzen von Globalen Variablen
        self.fileEntry.delete(0, tk.END) 
        self.fileEntry.insert(0, fDir)  
        if len(fDir) > self.entryLen:  
            self.fileEntry.config(width=35)                 # Limitieren der GUI Länge
            self.fileEntry.config(state='readonly') 
     
        self.netwEntry.delete(0, tk.END) 
        self.netwEntry.insert(0, netDir)  
        if len(netDir) > self.entryLen: 
#             self.netwEntry.config(width=len(netDir) + 3)
            self.netwEntry.config(width=35)                 # limit width to adjust GUI
        
        
    def use_queues(self, loops=5):
        while True: 
            print(self.gui_queue.get())        
                            
    def method_in_a_thread(self, num_of_loops=10):
        for idx in range(num_of_loops):
            sleep(1)
            self.scrol.insert(tk.INSERT, str(idx) + '\n')  

    def create_thread(self, num=1):
        self.run_thread = Thread(target=self.method_in_a_thread, args=[num]) 
        self.run_thread.setDaemon(True) 
        self.run_thread.start()

        # start queue in its own thread
        write_thread = Thread(target=self.use_queues, args=[num], daemon=True)
        write_thread.start()   
                        
    # Button callback
    def click_me(self): 
        self.action.configure(text='Hello ' + self.name.get())
        print(self)
        # self.create_thread()                # now called from imported module
        bq.write_to_scrol(self)    
            
            
    def _spin(self):
        value = self.spin.get()
        self.scrol.insert(tk.INSERT, value + '\n')
        
    def radCall(self):
        radSel = self.radVar.get()
        if   radSel == 0: self.mighty2.configure(text='Blue')
        elif radSel == 1: self.mighty2.configure(text='Gold')
        elif radSel == 2: self.mighty2.configure(text='Red')          
        
    def run_progressbar(self):
        self.progress_bar["maximum"] = 100
        for i in range(101):
            sleep(0.05)
            self.progress_bar["value"] = i 
            self.progress_bar.update()      
        self.progress_bar["value"] = 0       
    
    def start_progressbar(self):
        self.progress_bar.start()
        
    def stop_progressbar(self):
        self.progress_bar.stop()
     
    def progressbar_stop_after(self, wait_ms=1000):    
        self.win.after(wait_ms, self.progress_bar.stop)        

    def usingGlobal(self):
        global GLOBAL_CONST
        GLOBAL_CONST = 777
        
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit() 
                  
    #####################################################################################       
    def create_widgets(self):    
        tabControl = ttk.Notebook(self.win)     
        
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text='Tab 1')
        tab2 = ttk.Frame(tabControl)           
        tabControl.add(tab2, text='Tab 2')      
        
        tabControl.pack(expand=1, fill="both")  
        
        mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')
        mighty.grid(column=0, row=0, padx=8, pady=4)
        
        a_label = ttk.Label(mighty, text="Enter a name:")
        a_label.grid(column=0, row=0, sticky='W')
     
        # Setzen eines eigenen Namens
        self.name = tk.StringVar()
        self.name_entered = ttk.Entry(mighty, width=24, textvariable=self.name)
        self.name_entered.grid(column=0, row=1, sticky='W')               
        self.name_entered.delete(0, tk.END)
        self.name_entered.insert(0, '< default name >') 
                
        self.action = ttk.Button(mighty, text="Click Me!", command=self.click_me)   
        self.action.grid(column=2, row=1)                                
        
        ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)
        number = tk.StringVar()
        self.number_chosen = ttk.Combobox(mighty, width=14, textvariable=number, state='readonly')
        self.number_chosen['values'] = (1, 2, 4, 42, 100)
        self.number_chosen.grid(column=1, row=1)
        self.number_chosen.current(0)
        
        self.spin = Spinbox(mighty, values=(1, 2, 4, 42, 100), width=5, bd=9, command=self._spin) # using range
        self.spin.grid(column=0, row=2, sticky='W') # align left
        
        scrol_w = 40; scrol_h = 10                  # increase sizes
        self.scrol = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.scrol.grid(column=0, row=3, sticky='WE', columnspan=3)                    
        
        for child in mighty.winfo_children():       # add spacing to align widgets within tabs
            child.grid_configure(padx=4, pady=2) 
         
        #=====================================================================================
        self.mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')
        self.mighty2.grid(column=0, row=0, padx=8, pady=4)
        
        chVarDis = tk.IntVar()
        check1 = tk.Checkbutton(self.mighty2, text="Disabled", variable=chVarDis, state='disabled')
        check1.select()
        check1.grid(column=0, row=0, sticky=tk.W)                   
        
        chVarUn = tk.IntVar()
        check2 = tk.Checkbutton(self.mighty2, text="UnChecked", variable=chVarUn)
        check2.deselect()
        check2.grid(column=1, row=0, sticky=tk.W)                   
        
        chVarEn = tk.IntVar()
        check3 = tk.Checkbutton(self.mighty2, text="Enabled", variable=chVarEn)
        check3.deselect()
        check3.grid(column=2, row=0, sticky=tk.W)                     
        
        
        colors = ["Blue", "Gold", "Red"]    
        self.radVar = tk.IntVar()
        self.radVar.set(99)                                 
         
        for col in range(3):                             
            curRad = tk.Radiobutton(self.mighty2, text=colors[col], variable=self.radVar, 
                                    value=col, command=self.radCall)          
            curRad.grid(column=col, row=1, sticky=tk.W)             
                
        self.progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=342, mode='determinate')
        self.progress_bar.grid(column=0, row=3, pady=2)         
             
        buttons_frame = ttk.LabelFrame(self.mighty2, text=' ProgressBar ')
        buttons_frame.grid(column=0, row=2, sticky='W', columnspan=2)        
        
        ttk.Button(buttons_frame, text=" Run Progressbar   ", command=self.run_progressbar).grid(column=0, row=0, sticky='W')  
        ttk.Button(buttons_frame, text=" Start Progressbar  ", command=self.start_progressbar).grid(column=0, row=1, sticky='W')  
        ttk.Button(buttons_frame, text=" Stop immediately ", command=self.stop_progressbar).grid(column=1, row=0, sticky='W')  
        ttk.Button(buttons_frame, text=" Stop after second ", command=self.progressbar_stop_after).grid(column=1, row=1, sticky='W')  
         
        for child in buttons_frame.winfo_children():  
            child.grid_configure(padx=2, pady=2) 
         
        for child in self.mighty2.winfo_children():  
            child.grid_configure(padx=8, pady=2) 

#========MAGIC=========================================================================

        # Frame für die Dateiauswahl ------------------------------------------------
        mngFilesFrame = ttk.LabelFrame(tab2, text=' Manage Files: ')
        mngFilesFrame.grid(column=0, row=1, sticky='WE', padx=10, pady=5)

        # Button Callback  
        def getFileName():                 #Kein Hardgecodeter Dateipfad mehr
            print('hello from getFileName')
            fDir  = path.dirname(__file__)
            fName = fd.askopenfilename(parent=self.win, initialdir=fDir) #File Select Dialog
            print(fName)
            self.fileEntry.config(state='enabled')
            self.fileEntry.delete(0, tk.END)
            self.fileEntry.insert(0, fName)
            
            if len(fName) > self.entryLen:
                self.fileEntry.config(width=len(fName) + 3)
                        
        # Add Widgets to Manage Files Frame
        lb = ttk.Button(mngFilesFrame, text="Browse to File...", command=getFileName)     
        lb.grid(column=0, row=0, sticky=tk.W) 
        
        #-----------------------------------------------------        
        file = tk.StringVar()
        self.entryLen = scrol_w - 4
        self.fileEntry = ttk.Entry(mngFilesFrame, width=self.entryLen, textvariable=file)
        self.fileEntry.grid(column=1, row=0, sticky=tk.W)
              
        #-----------------------------------------------------
        logDir = tk.StringVar()
        self.netwEntry = ttk.Entry(mngFilesFrame, width=self.entryLen, textvariable=logDir)
        self.netwEntry.grid(column=1, row=1, sticky=tk.W) 

        
        def copyFile():            # Kopiervorgang mit Try, except
            import shutil          # Import innerhalb einer Funktion (Shel-utility)
            src = self.fileEntry.get()
            file = src.split('/')[-1]  
            dst = self.netwEntry.get() + '\\'+ file
            try:
                shutil.copy(src, dst)   
                msg.showinfo('Copy File to Network', 'Succes: File copied.') 
            # Verschiedene Arten von Fehlern    
            except FileNotFoundError as err:
                msg.showerror('Copy File to Network', '*** Failed to copy file! ***\n\n' + str(err))
            except Exception as ex:
                msg.showerror('Copy File to Network', '*** Failed to copy file! ***\n\n' + str(ex))   
        
        cb = ttk.Button(mngFilesFrame, text="Copy File To :   ", command=copyFile)     
        cb.grid(column=0, row=1, sticky=tk.E) 
                
        # Add some space around each label
        for child in mngFilesFrame.winfo_children(): 
            child.grid_configure(padx=6, pady=6)
                    
#==========MAGIC ENDE============================================================================================================

        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)
        
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self._quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        
        def _msgBox():
            msg.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2017.')  
            
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=_msgBox)   # display messagebox when clicked
        menu_bar.add_cascade(label="Help", menu=help_menu)
        
        # call function
        self.usingGlobal()
         
        # Auswahl von Tab2 beim Start 
        tabControl.select(1)  
                 
#======================
# Start GUI
#======================
oop = OOP()
oop.win.mainloop()
