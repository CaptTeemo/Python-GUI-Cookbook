# Projekte sind in einzelne Ordner und wiederum Unterordner aufgeteilt
# Im Code müssen bei den Imports diese ganzen Ordner angegeben werden
# Über die Umgebungsvariable PYTHONPATH könnte dies verhindert werden

# Eine andere Möglichkeit ist die __init__.py Funktion:

print('hi from GUI init\n')

# Benötigte Imports
from sys import path
from pprint import pprint
from site import addsitedir
from os import getcwd, chdir, pardir
#======================================================================
# Required setup for the PYTONPATH in order to find all package folders
#======================================================================

while True:
    curFull = getcwd()
    curDir = curFull.split('\\')[-1]  # OS-übergreifendes Arbeiten
    if 'NameOfDirectory' == curDir:
        addsitedir(curFull)           # Arbeitsverzeichnis
        addsitedir(curFull + 'Folder1\Folder2\Folder3') # Unterordner des Arbeitsverzeichni
        break
    chdir(pardir)
pprint(path)

# __init__ MUSS EXPLIZIT EINGEBUNDEN WERDEN!!!
# HIER KANN DANN AUCH EIN LANGER PFAD STEHEN
