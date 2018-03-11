
# Grundlegendes: In diesem Fall kann nach Aufruf des
# wx-Fensters das tkinter Fenster nicht mehr angeklickt werden
# Nach schließen des Fensters werden alle Aktionen auf einmal ausgeführt
#==================================================================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from threading import Thread

win = tk.Tk()    

# Komplette Erstellung des tkinter Teils     
win.title("Python GUI")
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)    
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number)
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)
scrolW = 30
scrolH =  3
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, sticky='WE', columnspan=3) 

#==================================================================
# Funktion für Aufruf der wxPython-GUI ->
# Letztes Fenster kann erst mit Hauptfenster geschlossen werden
def wxPythonApp():
    import wx
    app = wx.App()
    frame = wx.Frame(None, -1, "wxPython GUI", size=(200,150))
    frame.SetBackgroundColour('white')
    frame.CreateStatusBar()
    menu= wx.Menu()
    menu.Append(wx.ID_ABOUT, "About", "wxPython GUI")
    menuBar = wx.MenuBar()
    menuBar.Append(menu, "File") 
    frame.SetMenuBar(menuBar)     
    frame.Show()
    tryRunInThread()
    

# Damit tkinter-Fenster bedienbar werden
def tryRunInThread():
    runT = Thread(target=app.MainLoop)
    runT.setDaemon(True)
    runT.start()

# Button zum Aufrufen des anderen Fensters    
action = ttk.Button(win, text="Call wxPython GUI", command=wxPythonApp) 
action.grid(column=2, row=1)
    
#======================
# Start GUI
#======================
win.mainloop()