#primeiro fazer o programa e depois torna lo modular.

class Puzzle:
    
    def __init__(self):
        self.heuristic=0

    def gen_puzz(self):
        pass
    
    def eval(self):
        pass
    
class Board_Q(Puzzle):
    
    def __init__(self):
        pass
    
    def gen_puzz(self):
        pass
    
    def eval(self):
        pass
        

class solver:
# Solver tem de ter um puzzle aqui apresentado como board
    def __init__(self):
        self.puzzle= Board_Q()
        pass
    
    def solve(self):
        list_puzzle=self.puzzle.gen_puzz()
        conflicts=self.puzzle.eval;
        while conflicts!=0 :
            for aux in list_puzzle:
                if(aux.eval<conflicts):
                    self.puzzle=aux
                    
                
        
        