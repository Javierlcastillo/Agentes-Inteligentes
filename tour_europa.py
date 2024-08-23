#---------------------------------------------------------------------------------------------------------------
#    Agente Solucionador de Problemas para el Tour de Europa
#    Versión que utiliza diccionarios externos para describir los datos de problema
#---------------------------------------------------------------------------------------------------------------

from simpleai.search import SearchProblem, depth_first, breadth_first, uniform_cost, greedy, astar
from simpleai.search.viewers import BaseViewer, ConsoleViewer, WebViewer

#---------------------------------------------------------------------------------------------------------------
#   Definición del problema del Tour de Europa
#---------------------------------------------------------------------------------------------------------------

class Tour(SearchProblem):
    """ 
        Clase utilizada para describir el problema del Tour de Europa. Los estados son representados 
        por medio del nombre de de las ciudades europeas.
    """

    def __init__(self, origen, destino):
        """ Constructor de la clase para el problema del Tour de Europa. 
            Inicializa el problema de acuerdo a la ciudad de origen.
       
            origen: ciudad donde inicia el tour
            destino: ciudad donde termina el tour
        """
        
        # Llama al constructor de su superclase SearchProblem (estado inicial = ciudad de inicio).
        SearchProblem.__init__(self, origen)

        # Define el estado meta = ciudad destino.
        self.goal_state = destino

    def actions(self, state):
        """ 
            Este método regresa una lista con las acciones legales que pueden ser ejecutadas de 
            acuerdo con el estado especificado.
            
            state: ciudad actual.
        """

        # Cada acción es una ciudad vecina (con su distancia) de la ciudad origen.

        return list(ciudades_vecinas[state])

    def result(self, state, action):
        """ 
            Este método regresa la ciudad vecina en la que terminaría el agente si se usa la acción. 

            state: Una ciudad actual.
            action: Acción de traslado especificada como (ciudad vecina, distancia).
        """
        return action

    def is_goal(self, state):
        """ 
            Este método evalua si un estado es meta.

            state: estado a ser evaluado
        """
        return state == self.goal_state
        
    def cost(self, state, action, state2):
        """ 
            Regresa el costo de aplicar la acción para trasladarse de state a state2.

            state: Una ciudad origen.
            action: trasladarse a una ciudad vecina, especificada como (ciudad vecina, distancia)
            state2: Una ciudad vecina de la ciudad origen
        """
        return ciudades_vecinas[state][state2]
        
    def heuristic(self, state):
        """ 
            Este método regresa un estimado de la distancia desde el estado a la meta.
			Utiliza una tabla de distancias en línea recta entre las ciudades.

            state: Ciudad actual.
        """

        return distancia_a_cannes[state]

# Despliega la secuencia de estados y acciones obtenidas como resultado
def display(result):
    if result is not None:
        for i, (action, state) in enumerate(result.path()):
            if action == None:
                print('Configuración inicial')
            elif i == len(result.path()) - 1:
                print(i,'- Después de moverse a', action)
                print('¡Meta lograda con costo =', result.cost,'!')
            else:
                print(i,'- Después de moverse a', action)

            print('  ', state)
    else:
        print('Mala configuración del problema')

#---------------------------------------------------------------------------------------------------------------
#   Programa
#---------------------------------------------------------------------------------------------------------------

# Ciudades con las que conecta cada ciudad del Tour de Europa y su distancia
ciudades_vecinas = {
    'Paris' : {'Burdeos': 300, 'Estrasburgo': 320},
    'Burdeos' : {'Paris': 300, 'SanSebastian': 250, 'Lyon': 350},
    'Estrasburgo' : {'Paris': 320, 'Lyon': 340, 'Ginebra': 510},
    'SanSebastian' : {'Burdeos': 250, 'Barcelona': 430},
    'Lyon' : {'Burdeos': 350, 'Estrasburgo': 340, 'Grenoble': 125},
    'Ginebra' : {'Estrasburgo': 510, 'Cannes': 630},
    'Barcelona' : {'SanSebastian': 250, 'Cannes': 485},
    'Grenoble' : {'Lyon': 125, 'Cannes': 680},
    'Cannes' : {'Barcelona': 485, 'Grenoble': 680, 'Ginebra': 630}
}

# Distancia de cada ciudad a Cannes (la meta)
distancia_a_cannes = {
    'Paris' : 1400,
    'Burdeos' : 1100,
    'Estrasburgo' : 1120,
    'SanSebastian' : 900,
    'Lyon' : 780,
    'Ginebra' : 630,
    'Barcelona' : 480,
    'Grenoble' : 680,
    'Cannes' : 0
}

#---------------------------------------------------------------------------------------------------------------
#   Solución del problema con diferentes métodos
#---------------------------------------------------------------------------------------------------------------

# posibles expectadores para las búsquedas
my_viewer = None
#my_viewer = BaseViewer()       # Solo estadísticas
#my_viewer = ConsoleViewer()    # Texto en la consola
#my_viewer = WebViewer()        # Abrir en un browser en la liga http://localhost:8000

# Crea un PSA y lo resuelve mediante una búsqueda de árbol con el algoritmo
# primero en anchura
result = breadth_first(Tour('Paris', 'Cannes'), graph_search=False, viewer=my_viewer)

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
result = depth_first(Tour('Paris', 'Cannes'), graph_search=True)
print()
print('>> Búsqueda Primero en Profundidad <<')
display(result)

# resuelve el problema utilizando búsqueda de grafo con el algoritmo de
# A*. 
result = astar(Tour('Paris', 'Cannes'), graph_search=True)
print()
print('>> Búsqueda A* <<')
display(result)


#---------------------------------------------------------------------------------------------------------------
#   Fin del archivo
#---------------------------------------------------------------------------------------------------------------