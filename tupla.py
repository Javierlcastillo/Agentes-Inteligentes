from simpleai.search import SearchProblem, depth_first, breadth_first, uniform_cost, greedy, astar
from simpleai.search.viewers import BaseViewer, ConsoleViewer, WebViewer

class Ubicacion:
    def __init__(self, locx, locy):
        self.x = locx
        self.y = locy

    def setx(self, equis):
        self.x += equis
      
    def sety(self, ye):
        self.y += ye

class Tablero(SearchProblem):
    def __init__(self, ubicacion_inicial, llenas):
        self.ubicacion_inicial = ubicacion_inicial
        self.llenas = llenas
        initial_state = (ubicacion_inicial, llenas)
        SearchProblem.__init__(self, initial_state)

    def actions(self, state):
        ubicacion, llenas = state
        actions = []
        posibles_movimientos = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
        for dx, dy in posibles_movimientos:
            new_x = ubicacion.x + dx
            new_y = ubicacion.y + dy
            if 0 <= new_x < 4 and 0 <= new_y < 4:
                actions.append((dx, dy))
        return actions

    def result(self, state, action):
        ubicacion, llenas = state
        dx, dy = action
        new_ubicacion = Ubicacion(ubicacion.x + dx, ubicacion.y + dy)
        new_llenas = llenas.copy()
        if (new_ubicacion.x, new_ubicacion.y) in new_llenas:
            new_llenas.remove((new_ubicacion.x, new_ubicacion.y))
        return (new_ubicacion, new_llenas)

    def is_goal(self, state):
        _, llenas = state
        return len(llenas) == 0 

    def cost(self, state1, action, state2):
        return 1
    
    def heuristic(self, state):
        _, llenas = state
        return len(llenas)
    
def display(result):
    if result is not None:
        for i, (action, state) in enumerate(result.path()):
            if action is None:
                print('Configuración inicial')
            elif i == len(result.path()) - 1:
                print(i, '- Después de moverse a', 'Ir a', action)
                print('¡Meta lograda con costo =', result.cost, '!')
            else:
                print(i, '- Después de moverse a', 'Ir a', action)
            print('  ', state)
    else:
        print('Mala configuración del problema')
        
my_viewer = 0
#my_viewer = BaseViewer()       # Solo estadísticas
#my_viewer = ConsoleViewer()    # Texto en la consola
#my_viewer = WebViewer()

def LlenarTablero(tamano):
    llenas = []
    for i in range(tamano):
        for j in range(tamano):
            llenas.append((i, j))
    llenas.remove(llenas[0])
    return llenas

llenas = LlenarTablero(4)
u_inicial = Ubicacion(3,0)
result = breadth_first(Tablero(u_inicial, llenas), graph_search=False, viewer=my_viewer)

# despliega las estadísticas de búsqueda si no se seleccionó un espectador
if my_viewer != None:
    print('Stats:')
    print(my_viewer.stats)

# despliega el resultado de la búsqueda primero en anchura
print()
print('>> Búsqueda Primero en Anchura <<')
display(result)

# resuelve el problema utilizando búsqueda de grafo con el algoritmo de
# primero en profundidad
result = depth_first(Tablero(u_inicial, llenas), graph_search=True)
print()
print('>> Búsqueda Primero en Profundidad <<')
display(result)
