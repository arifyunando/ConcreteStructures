import numpy as np
import materials

#this module contains rebar spesifications
class rebar():
    #initialazion only consist of defining the size of the rebar. Each rebar locations can be added
    #using the setPosition method after instanciating the class. Hence, if a section use more than
    #one size of rebar, multiple instanciation will be needed.
    def __init__(self, size):
        self.size  = size
        self.area  = (np.pi/4)*size*size
        self.coord_x = []
        self.coord_y = []

    def setMaterial(self, material):
        self.material = material if isinstance(material, materials.steel) else print("Set Material Failed")
    
    def setPosition(self, x, y):  
        self.coord_x.append(x)
        self.coord_y.append(y)

    @property
    def centerOfMass(self):
        self.x_bar = np.average(self.coord_x)
        self.y_bar = np.average(self.coord_y)
        return (self.x_bar, self.y_bar)

class ties():
    pass

class spirals():
    pass