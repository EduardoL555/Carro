
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import sys
import random
sys.path.append('..')

from OpMat import OpMat
from Carro import Carro
from CityGraph import graph  
from Mapa import draw_city, draw_graph

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

X_MIN = -1300
X_MAX = 1300
Y_MIN = -850
Y_MAX = 850

def init():
    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("OpenGL - Navegación con Grafos (Movimiento Restringido)")
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(X_MIN, X_MAX, Y_MIN, Y_MAX)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    glClearColor(0, 0, 0, 0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)


def main():
    init()
    
    op = OpMat()
    coches = []
    num_coches = 10
    
    available_nodes = [n for n in graph.keys() if n != 6]
    for i in range(num_coches):
        random_node = random.choice(available_nodes)
        car = Carro(opMat=op, graph=graph, initial_node=random_node, initial_dir='right', user_controlled=False,color=[1.0, 1.0, 1.0])
        coches.append(car)
    
   
    user_car = Carro(opMat=op, graph=graph, initial_node=6, initial_dir='right', user_controlled=True,color=[255.0/255.0, 51.0/255.0, 31.0/255.0])
    coches.insert(0, user_car)
    
    clock = pygame.time.Clock()
    done = False
    while not done:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        keys = pygame.key.get_pressed()
        glClear(GL_COLOR_BUFFER_BIT)
        draw_city()
        #draw_graph(graph)
        
        for i, car in enumerate(coches):
            others = coches[:i]
            if car.user_controlled:
                car.update(dt, others, keys)
            else:
                car.update(dt, others)
            car.render()
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
