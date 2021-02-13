import numpy as np

#this module contains materials that construct a concrete structure
class materials():
    def __init__(self):
        self.yield_stress = 0   #stress state at which materials start to yield
        self.ultimate_stress = 0#stress state at which materails fail
        self.strain_u = 0       #maximum deformation at ultimate stress
        self.modulus = 0        #Young's modulus
        self.strain = 0         #current deformation
        self.stress = 0         #current stress

class concrete(materials):
    def __init__(self, fc):
       self.yield_stress = fc
       self.ultimate_stress = fc
       self.strain_u = 0.003
       self.modulus = 4700*np.sqrt(fc)*1_000_000
        
class steel(materials):
    def __init__(self,fu, fy):
        self.yield_stress = fy
        self.ultimate_stress = fu
        self.strain_u = 0.005
        self.modulus = 200_000_000        