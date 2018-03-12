from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Anfangsposition + Größe
x = GLfloat(0.0).value
y = GLfloat(0.0).value
rect_size = GLfloat(25.0).value

# Schnelligkeit
xstep = GLfloat(3.0).value
ystep = GLfloat(3.0).value

# Größe des Fensters
windowWidth  = GLfloat(133).value       # 800/600 = 1.33
windowHeight = GLfloat(100).value


def RenderScene():                      # display callback function
    glClear(GL_COLOR_BUFFER_BIT)        # clear window with color defined in SetupRC
                                        # Farbe = Rot
    glColor3f(1.0, 0.0, 0.0)            # Funktion erwartet 3 Floats (RGB)
    glRectf(x, y, x + rect_size, y - rect_size) # Zeichnen des Vierecks + obige Farbe
    
    glutSwapBuffers()                   # Doppelten Buffer swappen


def TimerFunction(value):
    global x, xstep, y, ystep
    
    # Kollisionshandling
    if ((x > windowWidth - rect_size) or (x < -windowWidth)):
        xstep = -xstep
        
    if ((y > windowHeight) or (y < -windowHeight + rect_size)):
        ystep = -ystep
            
    x += xstep
    y += ystep
     
    if (x > (windowWidth - rect_size + xstep)):
        x = windowWidth - rect_size - 1
    elif (x < -(windowWidth + xstep)):
        x = -windowWidth - 1
        
    if (y > (windowHeight + ystep)):
        y = windowHeight - 1
    elif (y < -(windowHeight - rect_size + ystep)):
        y = -windowHeight + rect_size - 1
        
    # Fenster neu zeichnen
    glutPostRedisplay()
    glutTimerFunc(33, TimerFunction, 1)     # Rekursiver-Aufruf
        
        
def SetupRC():                          # Hintergrund zeichnen
    glClearColor(0.0, 0.0, 1.0, 1.0)    
  
  
def ChangeSize(w, h):                   
    if h == 0: h =1                     # /0 verhindern
        
    glViewport(0, 0, w, h)              # Viewport anpassen
    
    glMatrixMode(GL_PROJECTION)         # Projektions-modus
    glLoadIdentity()                    # Koordinatensystem zurücksetzen
    
    aspectRatio = GLfloat(w).value / GLfloat(h).value   # Größe anpassen
                                                            
    if w <= h:
        windowWidth = 100
        windowHeight = 100 / aspectRatio
        glOrtho(-100.0, 100.0, -windowHeight, windowHeight, 1.0, -1.0)      
    else:
        windowWidth = 100 * aspectRatio
        windowHeight = 100
        glOrtho(-windowWidth, windowWidth, -100.0, 100.0, 1.0, -1.0)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)     # Doppelter Buffer modus
    glutInitWindowSize(800, 600)                    # Größe des Fensters
    glutCreateWindow(b"Bouncing Red Square")        # b -> verwandelt den String in Bytes
    glutDisplayFunc(RenderScene)  
    glutReshapeFunc(ChangeSize)  
    
    glutTimerFunc(33, TimerFunction, 1)
    
    SetupRC()
    
    glutMainLoop()
    
#=================
if __name__ == '__main__':
    main()
    