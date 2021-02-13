# default sections, subclass will be the presets of each sections type i.e. rectangular, circular, and T-shape
class sections():
    def __init__(self):
        self.H = 0
        self.x_bar = 0
        self.y_bar = 0
        self.inertia_x = 0
        self.inertia_y = 0

class rectangleSection(sections):
    def __init__(self, base, height, cover):
        self.b = base
        self.H = height
        self.x_bar = base/2
        self.y_bar = height/2
        self.cover = cover
        self.inertia_x = (1/12)*base*(height**3)
        self.inertia_y = (1/12)*height*(base**3)

    #This compression area grows as a get deeper
    def compressionArea(self, a):
        return self.b*a

    #This is the distance between tension point to the furthest compression side given center of mass of the rebar (d)
    def CTdistance(self, rebarCenterOfMass):
        return (self.H - self.cover - rebarCenterOfMass)

     