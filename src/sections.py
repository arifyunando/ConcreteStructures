# default sections, subclass will be the presets of each sections type i.e. rectangular, circular, and T-shape
class sections():
    def __init__(self):
        self.B = 0
        self.H = 0
        self.x_bar = 0
        self.y_bar = 0
        self.inertia_x = 0
        self.inertia_y = 0

    #below are the configurations method available for applying rebars
    # setting options:
    # 1. All side equal
    #     The program attempts to place equal number of bars on each side of a
    #     rectangular layout then equally space them on each side. For a circular layout, the program
    #     attempts to equally space the bar.
    # 2. Equal Spacing
    #     The program attempts to place the bars equally spaced on all four sides
    #     of a rectangular layout. This command is only applicable for rectangular sections
    # 3. Sides Different
    #     The program will put rebars on each of the top (min. 2), bottom (min. 2), left, and right
    #     Note that corner bars are associated with top and bottom. Hence,the minimum value for each of them are 2 bars
    # 4. Tension Only
    #     The program will put rebars only at the tension part of the beam. User can specify up to 2 layers of rebars
    #     This configuration only available for beam analysis.
    # 4. Irregular Patterns
    #     This configuration allows the user to specify any number of bars to be placed any where within the column section
    #     However, note that as per version 0.0.0, only one cross-sectional area are available for this configuration.
    def allSideEqual(size, nbar, cover):
        pass

    def equalSpacing():
        pass

    def sidesDifferent():
        pass

    def tensionRebar():
        pass

    def irrPatterns():
        pass


class rectangleSection(sections):
    def __init__(self, base, height, cover):
        self.B = base
        self.H = height
        self.x_bar = base/2
        self.y_bar = height/2
        self.cover = cover
        self.inertia_x = (1/12)*base*(height**3)
        self.inertia_y = (1/12)*height*(base**3)

    #This method return the depth of compression area (a) given estimated force and available stress limit
    def compressionArea(self, compressionStress, compressionForce):
        return compressionForce/(compressionStress*self.B)

    #This is the distance between tension point to the furthest compression side given center of mass of the rebar (d)
    def CTdistance(self, rebarCenterOfMass):
        return (self.H - self.cover - rebarCenterOfMass)

class circularSection(sections):
    pass

class TSection(sections):
    pass



