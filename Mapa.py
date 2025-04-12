import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def draw_city():
    glLineWidth(2.5)
    glColor3f(100/255.0, 100/255.0, 100/255.0)
    glBegin(GL_QUADS)
    glVertex2f(-1300, -850)
    glVertex2f(-1300, 850)
    glVertex2f(1300, 850)
    glVertex2f(1300, -850)
    glEnd()
    
    glLineWidth(2.5)
    glColor3f(81/255.0, 78/255.0, 78/255.0)
    glBegin(GL_QUADS)
    # Cuadra 1
    glVertex2f(-1100, 650)
    glVertex2f(-1100, 350)
    glVertex2f(500, 350)
    glVertex2f(500, 650)
    # Cuadra 2
    glVertex2f(700, 650)
    glVertex2f(700, 350)
    glVertex2f(1100, 350)
    glVertex2f(1100, 650)
    # Cuadra 3
    glVertex2f(-1100, 150)
    glVertex2f(-1100, -150)
    glVertex2f(-900, -150)
    glVertex2f(-900, 150)
    # Cuadra 4
    glVertex2f(-700, 150)
    glVertex2f(-700, -150)
    glVertex2f(700, -150)
    glVertex2f(700, 150)
    # Cuadra 5
    glVertex2f(900, 150)
    glVertex2f(900, -150)
    glVertex2f(1100, -150)
    glVertex2f(1100, 150)
    # Cuadra 6
    glVertex2f(-1100, -350)
    glVertex2f(-1100, -650)
    glVertex2f(-700, -650)
    glVertex2f(-700, -350)
    # Cuadra 7
    glVertex2f(-500, -350)
    glVertex2f(-500, -650)
    glVertex2f(300, -650)
    glVertex2f(300, -350)
    # Cuadra 8
    glVertex2f(500, -350)
    glVertex2f(500, -650)
    glVertex2f(1100, -650)
    glVertex2f(1100, -350)
    glEnd()
    
    glLineWidth(2.5)
    glColor3f(166/255.0, 196/255.0, 153/255.0)
    glBegin(GL_QUADS)
    # Relleno c1
    glVertex2f(-1050, 600)
    glVertex2f(-1050, 400)
    glVertex2f(450, 400)
    glVertex2f(450, 600)
    # Relleno c2
    glVertex2f(750, 600)
    glVertex2f(750, 400)
    glVertex2f(1050, 400)
    glVertex2f(1050, 600)
    # Relleno c3
    glVertex2f(-1050, 100)
    glVertex2f(-1050, -100)
    glVertex2f(-950, -100)
    glVertex2f(-950, 100)
    # Relleno c4
    glVertex2f(-650, 100)
    glVertex2f(-650, -100)
    glVertex2f(650, -100)
    glVertex2f(650, 100)
    # Relleno c5
    glVertex2f(950, 100)
    glVertex2f(950, -100)
    glVertex2f(1050, -100)
    glVertex2f(1050, 100)
    # Relleno c6
    glVertex2f(-1050, -400)
    glVertex2f(-1050, -600)
    glVertex2f(-750, -600)
    glVertex2f(-750, -400)
    # Relleno c7
    glVertex2f(-450, -400)
    glVertex2f(-450, -600)
    glVertex2f(250, -600)
    glVertex2f(250, -400)
    # Relleno c8
    glVertex2f(550, -400)
    glVertex2f(550, -600)
    glVertex2f(1050, -600)
    glVertex2f(1050, -400)
    glEnd()
    
    glLineWidth(2.0)
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    
    # Líneas de la ciudad 1
    glVertex2f(-1200, 750)  
    glVertex2f(-1200, 700) 
    glVertex2f(-1200, 750)  
    glVertex2f(-1150, 750) 

    # Líneas de la ciudad 2
    glVertex2f(550, 750)  
    glVertex2f(650, 750) 
    glVertex2f(600, 750)  
    glVertex2f(600, 700) 
    
    # Líneas de la ciudad 3
    glVertex2f(1150, 750)  
    glVertex2f(1200, 750) 
    glVertex2f(1200, 750)  
    glVertex2f(1200, 700)
    
    # Líneas de la ciudad 4
    glVertex2f(-1200, 200)  
    glVertex2f(-1200, 300)
    glVertex2f(-1150, 250)  
    glVertex2f(-1200, 250) 

    # Líneas de la ciudad 5
    glVertex2f(-750, 250)  
    glVertex2f(-850, 250)
    glVertex2f(-800, 250)  
    glVertex2f(-800, 200) 

    # Líneas de la ciudad 6
    glVertex2f(650, 250)  
    glVertex2f(550, 250)
    glVertex2f(600, 250)  
    glVertex2f(600, 300)

    # Líneas de la ciudad 7
    glVertex2f(750, 250)  
    glVertex2f(800, 250)
    glVertex2f(800, 250)  
    glVertex2f(800, 200) 

    # Líneas de la ciudad 8
    glVertex2f(1200, 300)  
    glVertex2f(1200, 200)
    glVertex2f(1200, 250)  
    glVertex2f(1150, 250)

    # Líneas de la ciudad 9
    glVertex2f(-1200, -250)  
    glVertex2f(-1150, -250)
    glVertex2f(-1200, -300)  
    glVertex2f(-1200, -200)

    # Líneas de la ciudad 10
    glVertex2f(-800, -250)  
    glVertex2f(-800, -200)
    glVertex2f(-800, -250)  
    glVertex2f(-750, -250)

    # Líneas de la ciudad 11
    glVertex2f(-550, -250)  
    glVertex2f(-650, -250)
    glVertex2f(-600, -250)  
    glVertex2f(-600, -300)
    
    # Líneas de la ciudad 12
    glVertex2f(350, -250)  
    glVertex2f(450, -250)
    glVertex2f(400, -250)  
    glVertex2f(400, -300)
    
    # Líneas de la ciudad 13
    glVertex2f(750, -250)  
    glVertex2f(850, -250)
    glVertex2f(800, -250)  
    glVertex2f(800, -200)
    
    # Líneas de la ciudad 14
    glVertex2f(1200, -200)  
    glVertex2f(1200, -300)
    glVertex2f(1200, -250)  
    glVertex2f(1150, -250)
    
    # Líneas de la ciudad 15
    glVertex2f(-1200, -750)  
    glVertex2f(-1200, -700)
    glVertex2f(-1200, -750)  
    glVertex2f(-1150, -750)
    
    # Líneas de la ciudad 16
    glVertex2f(-600, -750)  
    glVertex2f(-600, -700)
    glVertex2f(-600, -750)  
    glVertex2f(-650, -750)
    
    # Líneas de la ciudad 17
    glVertex2f(400, -750)  
    glVertex2f(400, -700)
    glVertex2f(450, -750)  
    glVertex2f(350, -750)
    
    # Líneas de la ciudad 17
    glVertex2f(1200, -750)  
    glVertex2f(1200, -700)
    glVertex2f(1200, -750)  
    glVertex2f(1150, -750)
    
    glEnd()
    
def draw_graph(graph):
    # Dibujar nodos:
    glPointSize(5)
    glBegin(GL_POINTS)
    glColor3f(1, 0, 0)
    for node in graph.values():
        glVertex2f(node["x"], node["y"])
    glEnd()
    
    # Dibujar arcos:
    glColor3f(0, 1, 0)
    glBegin(GL_LINES)
    for node in graph.values():
        x1, y1 = node["x"], node["y"]
        for neighbor_id in node.get("neighbors", {}).values():
            neighbor = graph.get(neighbor_id)
            if neighbor:
                x2, y2 = neighbor["x"], neighbor["y"]
                glVertex2f(x1, y1)
                glVertex2f(x2, y2)
    glEnd()