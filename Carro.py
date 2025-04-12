
from OpenGL.GL import *
import math
import numpy as np

import random
import pygame  

class Carro:
    def __init__(self, opMat, graph, initial_node, initial_dir='right', user_controlled=False, color=None):
        self.opMat = opMat
        self.graph = graph
        self.node = initial_node
        self.pos = np.array([graph[initial_node]["x"], graph[initial_node]["y"]], dtype=float)
        
        self.direction = initial_dir
        self.countDeg = self._dir_to_angle(initial_dir)
        
        if color is None:
            color = [1.0, 1.0, 1.0]
        self.color = color
        self.esc = 12.0
        
        self.points = np.array([

            [-4.0, -2.0, 1.0],
            [-4.0,  2.0, 1.0],
            [ 4.0,  2.0, 1.0],
            [ 4.0, -2.0, 1.0],

            [-4.0,  3.0, 1.0],
            [-2.0,  3.0, 1.0],
            [-2.0,  4.0, 1.0],
            [-4.0,  4.0, 1.0],

            [ 2.0,  3.0, 1.0],
            [ 4.0,  3.0, 1.0],
            [ 4.0,  4.0, 1.0],
            [ 2.0,  4.0, 1.0],

            [-4.0, -3.0, 1.0],
            [-2.0, -3.0, 1.0],
            [-2.0, -4.0, 1.0],
            [-4.0, -4.0, 1.0],

            [ 2.0, -3.0, 1.0],
            [ 4.0, -3.0, 1.0],
            [ 4.0, -4.0, 1.0],
            [ 2.0, -4.0, 1.0]
        ], dtype=float)
        

        self.in_motion = False
        self.start_pos = self.pos.copy()
        self.target_pos = self.pos.copy()
        self.total_distance = 0.0
        self.velocity = 800.0  
        self.next_node = self.node
        self.radius = (8.0 * self.esc) / 2
        self.user_controlled = user_controlled

    def _dir_to_angle(self, d):
        if d == 'up':
            return 90
        elif d == 'down':
            return 270
        elif d == 'left':
            return 180
        return 0 

    def process_command_auto(self):
        if self.in_motion:
            return
        current_node = self.graph[self.node]
        neighbors = current_node.get("neighbors", {})
        if not neighbors:
            return
        next_direction = random.choice(list(neighbors.keys()))
        next_node = neighbors[next_direction]
        
        self.start_pos = self.pos.copy()
        self.target_pos = np.array([self.graph[next_node]["x"], self.graph[next_node]["y"]], dtype=float)
        self.total_distance = np.linalg.norm(self.target_pos - self.start_pos)
        self.in_motion = True
        self.next_node = next_node
        self.direction = next_direction
        self.countDeg = self._dir_to_angle(next_direction)

    def process_command_user(self, keys):
        if self.in_motion:
            return
        current_node = self.graph[self.node]
        allowed = current_node.get("neighbors", {})
        new_direction = None
        if keys[pygame.K_UP] and 'up' in allowed:
            new_direction = 'up'
        elif keys[pygame.K_DOWN] and 'down' in allowed:
            new_direction = 'down'
        elif keys[pygame.K_LEFT] and 'left' in allowed:
            new_direction = 'left'
        elif keys[pygame.K_RIGHT] and 'right' in allowed:
            new_direction = 'right'
        
        if new_direction is None:
            return
        
        next_node = allowed[new_direction]
        self.start_pos = self.pos.copy()
        self.target_pos = np.array([self.graph[next_node]["x"], self.graph[next_node]["y"]], dtype=float)
        self.total_distance = np.linalg.norm(self.target_pos - self.start_pos)
        self.in_motion = True
        self.next_node = next_node
        self.direction = new_direction
        self.countDeg = self._dir_to_angle(new_direction)

    def update(self, dt, others, keys=None):
        dt_s = dt / 1000.0
        
        if self.user_controlled:
            if not self.in_motion:
                self.process_command_user(keys)
        else:
            if not self.in_motion:
                self.process_command_auto()
                
        if self.in_motion:
            direction_vector = self.target_pos - self.start_pos
            if self.total_distance == 0:
                self.pos = self.target_pos.copy()
                self.node = self.next_node
                self.in_motion = False
                return
            
            direction_unit = direction_vector / self.total_distance
            displacement = self.velocity * dt_s
            proposed_pos = self.pos + direction_unit * displacement
            
            collision = False
            for other in others:
                if np.linalg.norm(proposed_pos - other.pos) < (self.radius + other.radius):
                    collision = True
                    break
            if collision:
                return
            
            traveled = np.linalg.norm(proposed_pos - self.start_pos)
            if traveled >= self.total_distance:
                self.pos = self.target_pos.copy()
                self.node = self.next_node
                self.in_motion = False
            else:
                self.pos = proposed_pos

    def render(self):
        self.opMat.push()
        self.opMat.loadId()
        self.opMat.translate(self.pos[0], self.pos[1])
        self.opMat.rotate(self.countDeg)
        self.opMat.scale(self.esc, self.esc)
        
        pointsR = self.points.copy()
        self.opMat.mult_Points(pointsR)
        
        glColor3f(*self.color)
        glBegin(GL_QUADS)
        for i in range(0, len(pointsR), 4):
            for j in range(4):
                glVertex2f(pointsR[i+j][0], pointsR[i+j][1])
        glEnd()
        
        self.opMat.pop()
