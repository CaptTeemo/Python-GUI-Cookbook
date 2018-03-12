
# Mithilfe einer sog. Factory können innerhalb des Codes
# einzelne Elements schneller erstell werden.
# natürlich ist dadurch auch der Overhead größer

# Import
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu

#====MAGIC=================================   
# Button Factory, die die Button-erzeugung regelt
class ButtonFactory():
    def createButton(self, type_):
        return buttonTypes[type_]()

# Standardbutton            
class ButtonBase():     
    relief     ='flat'
    foreground ='white'
    def getButtonConfig(self):
        return self.relief, self.foreground
#============================================   
# Überschreiben der Standardbuttons:

class ButtonRidge(ButtonBase):
    relief     ='ridge'
    foreground ='red'        
    
class ButtonSunken(ButtonBase):
    relief     ='sunken'
    foreground ='blue'        

class ButtonGroove(ButtonBase):
    relief     ='groove'
    foreground ='green'        
#============================================   


#Verschiedene Arten von Buttons in  Array stecken
buttonTypes = [ButtonRidge, ButtonSunken, ButtonGroove] 

class OOP():
    def __init__(self): 
        self.win = tk.Tk()         
        self.win.title("Python GUI")      
        self.createWidgets()

    def createWidgets(self):    
        tabControl = ttk.Notebook(self.win)     
        tab1 = ttk.Frame(tabControl)            
        tabControl.add(tab1, text='Tab 1')    
        tabControl.pack(expand=1, fill="both")        
        self.monty = ttk.LabelFrame(tab1, text=' Monty Python ')
        self.monty.grid(column=0, row=0, padx=8, pady=4)        
        self.createButtons()

    # Erstellung der eigentlichen Buttons:
    def createButtons(self):

        #Objekt erstellen    
        factory = ButtonFactory()

        # Button 1 mit relief 0 und foreground 0
        rel = factory.createButton(0).getButtonConfig()[0]
        fg  = factory.createButton(0).getButtonConfig()[1]
        action = tk.Button(self.monty, text="Button "+str(0+1), relief=rel, foreground=fg)   
        action.grid(column=0, row=1)  

        # Button 2 mit relief 1 und foreground 1
        rel = factory.createButton(1).getButtonConfig()[0]
        fg  = factory.createButton(1).getButtonConfig()[1]
        action = tk.Button(self.monty, text="Button "+str(1+1), relief=rel, foreground=fg)   
        action.grid(column=1, row=1)  
        
        # Button 3 mit relief 2 und foreground 2
        rel = factory.createButton(2).getButtonConfig()[0]
        fg  = factory.createButton(2).getButtonConfig()[1]
        action = tk.Button(self.monty, text="Button "+str(2+1), relief=rel, foreground=fg)   
        action.grid(column=2, row=1)          

#==========================
if __name__ == '__main__':
    oop = OOP()
    oop.win.mainloop()