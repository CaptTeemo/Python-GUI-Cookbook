# Gui mit wxPython

import wx

class GUI(wx.Frame):
    def __init__(self, parent, title, size=(200, 100)):
        # Superklasse initialisieren
        wx.Frame.__init__(self, parent, title=title, size=size)
        # Hintergrund weiß machen
        self.SetBackgroundColour('white')

        # Status Bar (Leiste unten) erstellen
        self.CreateStatusBar()

        # Menü erstellen
        menu = wx.Menu()
        # Menüpunkte erstellen
        menu.Append(wx.ID_ABOUT, "About", "wxPython GUI")  # mit Statusbar
        menu.AppendSeparator()
        menu.Append(wx.ID_EXIT, "Exit", " Exit the GUI")
        # Menü-Tab + Name für das Menü
        menuBar = wx.MenuBar()
        menuBar.Append(menu, "File")
        # MenuBar mit dem Fenster verbinden
        self.SetMenuBar(menuBar)

        # Fenster darstellen
        self.Show()


# Instanz der GUI erstellen
app = wx.App()

# Skalieren der Größe des Fensters
GUI(None, "Python GUI using wxPython", (300, 150))
# GUI laufen lassen
app.MainLoop()
