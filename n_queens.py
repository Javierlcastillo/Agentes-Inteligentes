#------------------------------------------------------------------------------------------------------------------
#   Hill Climbing solver for the n-queen problem
#   Modified by Dr. Santiago Enrique Conant Pablos
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------------------------
import time
import random
import math

#------------------------------------------------------------------------------------------------------------------
#   Class definitions
#------------------------------------------------------------------------------------------------------------------

class Board(object):
    """ 
        Class that represents n-queens placed on a chess board. Each queen is located in a 
        different column. The board is represented by a list of n rows. 
    """
    
    def __init__(self, n, randomize = True):        
        """ 
            This constructor initializes the board with n queens. 

            n: The number of rows and columns of the chess.
            randomize: True indicates that the initial queen rows are choosen randomly.
                       False indicates that the queens are placed on the first row.
        """
        self.n = n
        self.queens = []
        
        for col in range(n):
            if randomize:
                row = random.choice(range(n))
            else: # Place the queens on the first row
                row = 0
            self.queens.append(row)

    def show(self):        
        """ This method prints the current board. """               
        for row in range(self.n):
            for col in range(self.n):
                if self.queens[col] == row:
                    print (' Q ', end = '')
                else:
                    print (' - ', end = '')
            print('')
        print('')
    
    def cost(self):
        """ This method calculates the cost of this solution (the number of queens that are not safe). """
        c = 0
        for queen in range(self.n-1):
            for other_queen in range(queen+1,self.n):
                if (self.queens[queen] == self.queens[other_queen]):
                    # The queens are on the same row
                    c += 1
                elif (other_queen - queen) == abs(self.queens[queen] - self.queens[other_queen]):
                    # The queens are on the same diagonal
                    c += 1
        return c

    def best_neighbor(self):
        """ This method returns a board instance like this one but with the best move made. """        
        
        # Copy current board
        new_board = Board(self.n, False)
        new_board.queens = self.queens.copy()
             
        # Check all the non-occupied positions
        best_queen = best_row = best_cost = None
        for queen in range(self.n):
            for row in range(self.n):
                if self.queens[queen] != row:
                    # Copy current board
                    new_board = Board(self.n, False)
                    new_board.queens = self.queens.copy()
                    new_board.queens[queen] = row
                    #new_board.show()
                    new_cost = new_board.cost()
                    if best_cost == None or best_cost > new_cost:
                        best_board = new_board
                        best_cost = new_cost
        
        return best_board
                       
#------------------------------------------------------------------------------------------------------------------
#   Hill Climbing algorithm
#------------------------------------------------------------------------------------------------------------------
random.seed(time.time()*1000)

board = Board(8, True)      # Initialize board
board.show()    

def hill_climbing(current):
    print("-------- Initial state -----------")
    current.show()
    cost = current.cost()   # Initial cost  
    print("Initial Cost: ", cost)

    step = 0                # Step count
    while True:
        step += 1
        
        # Get best neighbor
        neighbor = current.best_neighbor()
        new_cost = neighbor.cost()

        # Test neighbor
        if new_cost < cost:
            current = neighbor
            cost = new_cost
        else:
            break

        print("Iteration: ", step, "    Cost: ", cost)

    print("--------Solution-----------")
    current.show()
    print("Final Cost: ", cost)
    return current
      

#------------------------------------------------------------------------------------------------------------------
#   Program
#------------------------------------------------------------------------------------------------------------------
random.seed(time.time()*1000)
initial_board = Board(8, True)      # Initialize board
solution = hill_climbing(initial_board)

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------
