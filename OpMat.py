# OpMat.py
import math
import numpy as np

class OpMat:
    def __init__(self):
        self.A = np.identity(3, dtype=float)
        self.stack = []
    
    def loadId(self):
        self.A = np.identity(3, dtype=float)
    
    def push(self):
        self.stack.append(self.A.copy())
    
    def pop(self):
        if self.stack:
            self.A = self.stack.pop()
    
    def translate(self, tx, ty):
        T = np.identity(3, dtype=float)
        T[0, 2] = tx
        T[1, 2] = ty
        self.A = self.A @ T
    
    def rotate(self, deg):
        R = np.identity(3, dtype=float)
        rad = math.radians(deg)
        R[0, 0] = math.cos(rad)
        R[0, 1] = -math.sin(rad)
        R[1, 0] = math.sin(rad)
        R[1, 1] = math.cos(rad)
        self.A = self.A @ R
    
    def scale(self, sx, sy):
        S = np.identity(3, dtype=float)
        S[0, 0] = sx
        S[1, 1] = sy
        self.A = self.A @ S
    
    def mult_Points(self, points):
        transformed = (self.A @ points.T).T
        for i in range(transformed.shape[0]):
            points[i, 0] = int(transformed[i, 0])
            points[i, 1] = int(transformed[i, 1])
