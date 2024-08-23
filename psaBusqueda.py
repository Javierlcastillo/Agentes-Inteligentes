from simpleai.search import SearchProblem, depth_first, breadth_first, uniform_cost, greedy, astar

class Ubicacion:
    def __init__(self, locx, locy):
        self.x = locx
        self.y = locy

    def setx(self, equis):
        self.x += equis
      
    def sety(self, ye):
        self.y += ye
"""
    def setNew(self, equis, ye):
        self.x = equis
        self.y = ye
"""
class Tablero(SearchProblem):
    def __init__(self, llenas, vacias):
        super().__init__(llenas)
        self.goal_state = vacias

    def actions(self, Ubicacion):
        actions = []
        posibles_movimientos = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
        for dx,dy in posibles_movimientos:
            if (0 <= Ubicacion.x + dx < 4 and 0 <= Ubicacion.y + dy< 4):
                actions.append[(Ubicacion.setx, Ubicacion.sety)]
        return actions


