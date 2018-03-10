# Grundlegendes I18N steht für internationalisierung von Code
# -> Übersetzungen in verschiedene Sprachen
# L10N steht für Lokalisation -> Zeitzonen + Sommerzeit

# Für jede neue Sprache wird eine neue Funktion aufgerufen
# Innerhalb der einzelnen Funktionen werden die Texte, die der Benutzer zu sehen bekommt
# übersetzt. 
# Keine festen Strings für GUI in anderen Dateien
# Umlaute müssen als entsprechendes Unicode-Zeichen eingetragen werden (\u00E4)
# Hierfür gibt es einen in Microsoft integrierten Picker

# Für Zeitzonen Modul pytz

class I18N():
    # Internationalisierung
    def __init__(self, language):  
        # Verfügbare Sprachen    
        if   language == 'en': self.resourceLanguageEnglish()
        elif language == 'de': self.resourceLanguageGerman()
        else: raise NotImplementedError('Unsupported language.')
        
    def resourceLanguageEnglish(self):
        self.title = "Python Graphical User Interface"
        
        self.file  = "File"
        self.new   = "New"
        self.exit  = "Exit"
        self.help  = "Help"
        self.about = "About"
        
        self.WIDGET_LABEL = ' Widgets Frame '
        
        self.disabled  = "Disabled"
        self.unChecked = "UnChecked"
        self.toggle    = "Toggle"
        
        # Radiobutton list
        self.colors   = ["Blue", "Gold", "Red"]
        self.colorsIn = ["in Blue", "in Gold", "in Red"]
        
        self.labelsFrame  = ' Labels within a Frame '
        self.chooseNumber = "Choose a number:"
        self.label2       = "Label 2"
        
        self.timeZones = "All Time Zones"
        self.localZone = "Local Zone"
        self.getTime   = "New York"
        
        self.mgrFiles = ' Manage Files '
        
        self.browseTo = "Browse to File..."
        self.copyTo   = "Copy File To :   "
        
    
    def resourceLanguageGerman(self):      
        self.title = 'Python Grafische Benutzeroberflaeche'                      # w/out umlaut
#         self.title = 'Python Grafische Benutzeroberfl' + "\u00E4" + 'che'       # with umlaut via Unicode
        self.title = 'Python Grafische Benutzeroberfläche'                       # with umlaut UTF-8
        
        self.file  = "Datei"
        self.new   = "Neu"
        self.exit  = "Schliessen"
        self.help  = "Hilfe"
        self.about = "\u00DC" + "ber"
        self.about = "Über"

        self.WIDGET_LABEL = ' Widgets Rahmen '
        
        self.disabled  = "Deaktiviert"
        self.unChecked = "Nicht Markiert"
        self.toggle    = "Markieren"
        
        # Radiobutton list
        self.colors   = ["Blau", "Gold", "Rot"]    
        self.colorsIn = ["in Blau", "in Gold", "in Rot"]  
        
        self.labelsFrame  = ' Etiketten im Rahmen '
        self.chooseNumber = "Waehle eine Nummer:"
        self.label2       = "Etikette 2"
        
        self.timeZones = "Alle Zeitzonen"
        self.localZone = "Lokale Zone"
        self.getTime   = "Zeit"
    
        self.mgrFiles = ' Dateien Organisieren '
        
        self.browseTo = "Waehle eine Datei... "
        self.copyTo   = "Kopiere Datei zu :     "





