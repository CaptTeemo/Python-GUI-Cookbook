'''
May 2017
@author: Burkhard A. Meier
'''

from tkinter import Tk, Label
from itertools import cycle
from os import listdir, path, chdir

# Neuer Import:
from PIL import ImageTk 


class SlideShow(Tk):
    # Tkinter erweitern
    def __init__(self, msShowTimeBetweenSlides=1500):
        #Superklasse
        Tk.__init__(self)
        
        # Zeit in der ein Bild angezeigt wird
        self.showTime = msShowTimeBetweenSlides
        
        # Suchen nach Bildern im ORdner Resources
        chapter_folder = path.realpath(path.dirname(__file__))
        resources_folder = path.join(chapter_folder, 'Resources')
        listOfSlides = [slide for slide in listdir(resources_folder) if slide.endswith('gif') or slide.endswith('jpg')]

        # In einem Kreis (endlos) Bilder einlesen
        chdir(resources_folder)
        self.iterableCycle = cycle((ImageTk.PhotoImage(file=slide), slide) for slide in listOfSlides)
        
        # Label zum darstelen der Bilder
        self.slidesLabel = Label(self)
        
        # Frame erstellen
        self.slidesLabel.pack()
 
 
    def slidesCallback(self):
        # Nächstes Bild bekommen
        currentInstance, nameOfSlide = next(self.iterableCycle)
        
        # Zum Label zuweisen
        self.slidesLabel.config(image=currentInstance)
        
        # Titel der Fensters passend zum Bildnamen updaten
        self.title(nameOfSlide)
        
        # Rekursiver (Endloser) Aufruf
        self.after(self.showTime, self.slidesCallback)

 
#=================================
# Start GUI
#=================================             
if __name__ == '__main__':
    win = SlideShow()
    win.after(0, win.slidesCallback())
    win.mainloop()
