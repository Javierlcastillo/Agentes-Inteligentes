#---------------------------------------------------------------------------------------------------------------
#    Agente Solucionador de Problemas para el Tour de Europa
#    Versión que utiliza condiciones para implementar las funciones
#---------------------------------------------------------------------------------------------------------------

from simpleai.search import SearchProblem, depth_first, breadth_first, uniform_cost, greedy, astar
from simpleai.search.viewers import BaseViewer, ConsoleViewer, WebViewer

#---------------------------------------------------------------------------------------------------------------
#   Definición del problema del Tour de Europa
#---------------------------------------------------------------------------------------------------------------

class TourDeEuropa(SearchProblem):
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

        # Define el estado meta = ciudad de destino.
        self.goal_state = destino

    def actions(self, state):
        """ 
            Este método regresa una lista con las acciones legales que pueden ser ejecutadas de 
            acuerdo con el estado especificado.
            
            state: ciudad actual.
        """
        if state == 'Paris':
            actions = ['Burdeos','Estrasburgo']
        elif state == 'Burdeos':
            actions = ['Paris','San Sebastian','Lyon']
        elif state == 'Estrasburgo':
            actions = ['Paris','Lyon','Ginebra']
        elif state == 'San Sebastian':
            actions = ['Burdeos','Barcelona']
        elif state == 'Lyon':
            actions = ['Burdeos','Estrasburgo','Grenoble']
        elif state == 'Ginebra':
            actions = ['Estrasburgo','Cannes']
        elif state == 'Barcelona':
            actions = ['San Sebastian','Cannes']
        elif state == 'Grenoble':
            actions = ['Lyon','Cannes']
        elif state == 'Cannes':
            actions = ['Barcelona','Grenoble','Ginebra']
        return actions

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
        if state == 'Paris':
            if action == 'Burdeos':
                return 300
            elif action == 'Estrasburgo':
                return 320
        elif state == 'Burdeos':
            if action == 'Paris':
                return 300
            elif action == 'San Sebastian':
                return 250
            elif action == 'Lyon':
                return 350
        elif state == 'Estrasburgo':
            if action == 'Paris':
                return 320
            elif action == 'Lyon':
                return 340
            elif action == 'Ginebra':
                return 510
        elif state == 'San Sebastian':
            if action == 'Burdeos':
                return 250
            elif action == 'Barcelona':
                return 430
        elif state == 'Lyon':
            if action == 'Burdeos':
                return 350
            elif action == 'Estrasburgo':
                return 340
            elif action == 'Grenoble':
                return 125
        elif state == 'Ginebra':
            if action == 'Estrasburgo':
                return 510
            elif action == 'Cannes':
                return 630
        elif state == 'Barcelona':
            if action == 'San Sebastian':
                return 430
            elif action == 'Cannes':
                return 485
        elif state == 'Grenoble':
            if action == 'Lyon':
                return 125
            elif action == 'Cannes':
                return 680
        elif state == 'Cannes':
            if action == 'Barcelona':
                return 485
            elif action == 'Grenoble':
                return 680
            elif action == 'Ginebra':
                return 630
        
    def heuristic(self, state):
        """ 
            Este método regresa un estimado de la distancia desde el estado a la meta.

            state: ciudad del nodo
        """
        if state == 'Paris':
            return 1400
        elif state == 'Burdeos':
            return 1100
        elif state == 'Estrasburgo':
            return 1120
        elif state == 'San Sebastian':
            return 900
        elif state == 'Lyon':
            return 780
        elif state == 'Ginebra':
            return 630
        elif state == 'Barcelona':
            return 480
        elif state == 'Grenoble':
            return 680
        elif state == 'Cannes':
            return 0

# Despliega la secuencia de estados y acciones obtenidas como resultado
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
result = breadth_first(TourDeEuropa('Paris','Cannes'), graph_search=False, viewer=my_viewer)

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
result = depth_first(TourDeEuropa('Paris','Cannes'), graph_search=True)
print()
print('>> Búsqueda Primero en Profundidad <<')
display(result)

# resuelve el problema utilizando búsqueda de grafo con el algoritmo de
# A*.
result = astar(TourDeEuropa('Paris','Cannes'), graph_search=True)
print()
print('>> Búsqueda A* <<')
display(result)


#---------------------------------------------------------------------------------------------------------------
#   Fin del archivo
#---------------------------------------------------------------------------------------------------------------