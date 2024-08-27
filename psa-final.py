from simpleai.search import SearchProblem, iterative_limited_depth_first, limited_depth_first, breadth_first, uniform_cost, greedy, astar
from simpleai.search.viewers import BaseViewer, ConsoleViewer, WebViewer

#---------------------------------------------------------------------------------------------------------------
#   Definición del problema
#---------------------------------------------------------------------------------------------------------------
caballo = {
    1: [10, 7],
    2: [9, 11, 8],
    3: [12, 5, 10],
    4: [6, 11],
    5: [3, 11, 14],
    6: [4, 11, 15, 13],
    7: [1, 9, 14, 16],
    8: [2, 10, 15],
    9: [2, 7, 15],
    10: [8, 16, 1, 3],
    11: [2, 4, 5, 13],
    12: [3, 6, 14],
    13: [6, 11],
    14: [5, 7, 12],
    15: [8, 9, 6],
    16: [7, 10]
}

class Tablero(SearchProblem):
    def __init__(self, inicio, meta):

        # Llama al constructor de su superclase SearchProblem (estado inicial = ciudad de inicio).
        super(Tablero, self).__init__(initial_state= (inicio, ))
        self.meta = set(meta)

    def actions(self, state):
        posicion = state[-1]
        return caballo.get(posicion, [])

    def result(self, state, action):
        return state + (action,)

    def is_goal(self, state):
        return self.meta.issubset(state)
        
    def cost(self, state, action, state2):
        return 1
        
    def heuristic(self, state):
        return len(self.meta - set(state))

def display(result):
    if result is not None:
        for i, (action, state) in enumerate(result.path()):
            if action == None:
                print('Estado inicial')
            elif i == len(result.path()) - 1:
                print(i,'- Despues de moverse a', action)
                print('¡Meta lograda con costo =', result.cost,'!')
            else:
                print(i,'- Despues de moverse a', action)

            print('  ', state)
    else:
        print('Error!')

#---------------------------------------------------------------------------------------------------------------
#   Solución del problema con diferentes métodos
#---------------------------------------------------------------------------------------------------------------

# posibles expectadores para las búsquedas
my_viewer = None
#my_viewer = BaseViewer()       # Solo estadísticas
#my_viewer = ConsoleViewer()    # Texto en la consola
#my_viewer = WebViewer()        # Abrir en un browser en la liga http://localhost:8000

# despliega el resultado de la búsqueda primero en anchura
print()
print('>> Busqueda Primero en Anchura <<')
result = breadth_first(Tablero(inicio=1,meta=[3,2]), graph_search=False, viewer=my_viewer)
display(result)
if my_viewer != None:
    print('Stats:')
    print(my_viewer.stats)

# resuelve el problema utilizando búsqueda de grafo con el algoritmo de
# primero en profundidad
result = iterative_limited_depth_first(Tablero(inicio=1,meta=[3,2]), graph_search=True)
print()
print('>> Busqueda de Profundidad Iterativa limitada <<')
display(result)
if my_viewer != None:
    print('Stats:')
    print(my_viewer.stats)

result = uniform_cost(Tablero(inicio=1, meta=[3, 2]), graph_search=True)
print()
print('>> Busqueda de Costo Uniforme <<')
display(result)
if my_viewer is not None:
    print('Stats:')
    print(my_viewer.stats)

result = limited_depth_first(Tablero(inicio=1, meta=[3, 2]), 4)
print()
print('>> Busqueda con Limite de Profundidad <<')
display(result)
if my_viewer is not None:
    print('Stats:')
    print(my_viewer.stats)




# resuelve el problema utilizando búsqueda de grafo con el algoritmo de
# A*. 
result = astar(Tablero(inicio=1,meta=[3,2]), graph_search=True)
print()
print('>> Busqueda A* <<')
display(result)
if my_viewer != None:
    print('Stats:')
    print(my_viewer.stats)

result = greedy(Tablero(inicio=1, meta=[3, 2]), graph_search=True)
print()
print('>> Busqueda Greedy <<')
display(result)
if my_viewer is not None:
    print('Stats:')
    print(my_viewer.stats)


#---------------------------------------------------------------------------------------------------------------
#   Fin del archivo
#---------------------------------------------------------------------------------------------------------------