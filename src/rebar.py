import numpy as np

#this module contains rebar spesifications
class rebar():
    def __init__(self, size) -> None:
        self.size = size
        self.area = (np.pi/4)*size*size

    def setPosition(self, x, y):  
        self.coord_x = x
        self.coord_y = y
    
    def centerOfMass(self, *args):
        pass