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

# class Vacias(object):
#     def __init__(self, locx, locy):
#         self.x = locx
#         self.y = locy

# class Llenas(object):
#     def __init__(self, locx, locy):
#         self.x = locx
#         self.y = locy

class Tablero(SearchProblem):
    def __init__(self, ubicacion_inicial, llenas, vacias):
        self.ubicacion_inicial = ubicacion_inicial
        SearchProblem.__init__(self.ubicacion_inicial)
        final = (len(llenas) == 0) 
        self.goal_state = final

    def actions(self, state):
        Ubicacion, llenas, vacias = state #Tengo que hacer esta variable global?
        actions = []
        posibles_movimientos = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
        for dx,dy in posibles_movimientos:
            if (0 <= Ubicacion.x + dx < 4 and 0 <= Ubicacion.y + dy< 4):
                new_x = Ubicacion.setx(dx)
                new_y = Ubicacion.sety(dy)
                actions.append(new_x, new_y)
                for i in range(len(llenas)):
                    if llenas[i] == (new_x, new_y):
                        vacias.append((new_x, new_y))
                        llenas.remove(llenas[i])
                        break
        return actions

    # def result(self, state, action):
    #     Ubicacion, llenas, vacias = state
    
    def is_goal(self, state):
        return state == self.goal_state

    def cost(self):
        return 1
    
    def heuristic(self, vacias):
        return len(vacias)
    
def display(result):
    if result is not None:
        for i, (action, state) in enumerate(result.path()):
            if action == None:
                print('Configuración inicial')
            elif i == len(result.path()) - 1:
                print(i,'- Después de moverse a', 'Ir a '+action)
                print('¡Meta lograda con costo = ', result.cost,'!')
            else:
                print(i,'- Después de moverse a', 'Ir a '+action)

            print('  ', state)
    else:
        print('Mala configuración del problema')
