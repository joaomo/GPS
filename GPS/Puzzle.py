import random as rn
from math import exp

class Board:#puzzle specific
    def __init__(self,size_matrix=4):
        self.heur=0
        self.con_nodes=[[]]
        self.conflicts=0
    
    def eval(self):#for Kqueens
        pass
        
        
class Puzzle:#puzzle specific
    
    def __init__(self,size=4):
        self.board = Board(size)
        self.list=[]
        self.index_best_heur=0
        self.gen_board()
      
      
    def gen_board(self,nr=20,ind=-1):
        pass
                    
    def print_b(self):
        print(self.board.data)
        print (self.board.heur)
        