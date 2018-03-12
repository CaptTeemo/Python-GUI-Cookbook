# Ich bin dumb: Dateien dürfen natürlich nicht so heißen wie Bibliotheken

#==========
# Imports
#==========
import pyglet
from pyglet.gl import *
from pyglet.window import key
from OpenGL.GLUT import *

# Globale Variablen
WINDOW = 400
INCREMENT = 5

class Window(pyglet.window.Window):

    # Variablen zur Rotation
    xRotation = yRotation = 30    

    def __init__(self, width, height, title=''):
        super(Window, self).__init__(width, height, title)
        glClearColor(0, 0, 0, 1)
        glEnable(GL_DEPTH_TEST)    

    #==============================
    # Methoden von pyglet.window.Window()
    # werden überschriebe
    #==============================
    def on_draw(self):
        # Altes Bild wegschmeißen
        self.clear()
        
        # Neue Matrix auf stack schmeißen
        glPushMatrix()

        glRotatef(self.xRotation, 1, 0, 0)
        glRotatef(self.yRotation, 0, 1, 0)

        #Würfel Zeichen mit KONSTANTE v. pyglet
        glBegin(GL_QUADS)
        
        #====================
        # Farben bestimmen
        #====================
        # Vorderseite:

        # Weiß
        glColor3ub(255, 255, 255)
        glVertex3f(50, 50, 50)

        # Gelb
        glColor3ub(255, 255, 0)
        glVertex3f(50, -50, 50)

        # Rot
        glColor3ub(255, 0, 0)
        glVertex3f(-50, -50, 50)

        # Magenta
        glColor3ub(255, 0, 255)
        glVertex3f(-50, 50, 50)


        #====================
        # Es werden der Reihe nach die anderen Seiten
        # des Würfels gezeichnet, daher ommen Funktionen
        # öfters vor

        # Cyan
        glColor3f(0, 1, 1)
        glVertex3f(50, 50, -50)

        # Grün
        glColor3f(0, 1, 0)
        glVertex3f(50, -50, -50)
        
        # Schwarz
        glColor3f(0, 0, 0)
        glVertex3f(-50, -50, -50)

        # Blau
        glColor3f(0, 0, 1)
        glVertex3f(-50, 50, -50)
    
        # Cyan
        glColor3f(0, 1, 1)
        glVertex3f(50, 50, -50)

        # Weiß
        glColor3f(1, 1, 1)
        glVertex3f(50, 50, 50)

        # Magenta
        glColor3f(1, 0, 1)
        glVertex3f(-50, 50, 50)

        # Blau
        glColor3f(0, 0, 1)
        glVertex3f(-50, 50, -50)

        # Grünn
        glColor3f(0, 1, 0)
        glVertex3f(50, -50, -50)

        # Gelb
        glColor3f(1, 1, 0)
        glVertex3f(50, -50, 50)

        # Rot
        glColor3f(1, 0, 0)
        glVertex3f(-50, -50, 50)

        # Schwarz
        glColor3f(0, 0, 0)
        glVertex3f(-50, -50, -50)

        # Weiß
        glColor3f(1, 1, 1)
        glVertex3f(50, 50, 50)

        # Cyan
        glColor3f(0, 1, 1)
        glVertex3f(50, 50, -50)

        # Grün
        glColor3f(0, 1, 0)
        glVertex3f(50, -50, -50)

        # Gelb
        glColor3f(1, 1, 0)
        glVertex3f(50, -50, 50)
    
        # Magenta
        glColor3f(1, 0, 1)
        glVertex3f(-50, 50, 50)

        # Blau
        glColor3f(0, 0, 1)
        glVertex3f(-50, 50, -50)

        # Schwarz
        glColor3f(0, 0, 0)
        glVertex3f(-50, -50, -50)

        # Rot
        glColor3f(1, 0, 0)
        glVertex3f(-50, -50, 50)

        glEnd()

        # Matrix vom Stack schubsen
        glPopMatrix()

    def on_resize(self, width, height):
        # Viewport setzen
        glViewport(0, 0, width, height)

        # Projektions modus
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        aspectRatio = width / height
        gluPerspective(35, aspectRatio, 1, 1000)
         
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0, 0, -400)
    

    def on_text_motion(self, motion): 
        if motion == key.UP:
            self.xRotation -= INCREMENT  #KONSTANTEN von pyglet
        elif motion == key.DOWN:
            self.xRotation += INCREMENT
        elif motion == key.LEFT:
            self.yRotation -= INCREMENT
        elif motion == key.RIGHT:
            self.yRotation += INCREMENT
            
#==========
# Test-aufruf
#==========
if __name__ == '__main__':
    Window(WINDOW, WINDOW, 'Pyglet Colored Cube')
    pyglet.app.run()