import simpleai

class Empty(object):
    def __init__(self, locationx, locationy):
        self.x = locationx
        self.y = locationy

class Full(object):
    def __init__(self, locationx, locationy):
        self.x = locationx
        self.y = locationy

class Agent:
    def __init__(self, locationx, locationy):
        self.x = locationx
        self.y = locationy

    def Move(self, destinox, destinoy, movValido): #Puedo incluir una variable que sea 'movValido') 
        if destinox not in (4) or destinoy not in (4):
            movValido = False
        elif ((self.x + 2 or self.x - 2) == destinox) and ((self.y + 1 or self.y - 1) == destinoy):
            movValido = True
        elif ((self.x + 1 or self.x - 1) == destinox) and ((self.y + 2 or self.y - 2) == destinoy):
            movValido = True
        else:
            movValido = False


