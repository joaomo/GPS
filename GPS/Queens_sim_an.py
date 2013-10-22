import random as rn
from math import exp

class Board:
    def __init__(self,size_matrix=4):
        self.nr_column=size_matrix
        self.data=[0]*self.nr_column
        self.heur=0
        self.conflicts=0
    
    def eval(self):
        res=100
        l=len(self.data)
        count=0
        diag=0
        conflicts=0
        a=set()
        print(self.data)
        #for i in self.data:#iteration on column
        for j in range(l):
            i=self.data[j]
            if (j!=0 and i!=0 and self.data[j-1]==i-1):#diagonal back
                diag+=1
                print("back","i",i,"j",j,self.data[j-1],i-1)
            if (j!=0 and i!=l and self.data[j-1]==i+1):
                diag+=1
                print("front","i",i,"j",j,self.data[j-1],i+1)
            if self.data[j] in a:
                count+=1
            a.add(self.data[j])
        if ((count > 0) | (diag >0)):
            res-=(4**count+diag)
            conflicts+=count+diag
            print(diag,count)
#             else:
#                 print(count,diag)
        self.heur=res
        print(res)
        self.conflicts=conflicts
        
class Puzzle:
    
    def __init__(self,size=4):
        self.board = Board(size)
        self.list=[]
        self.index_best_heur=0
      
      
    def gen_board(self,nr):
        aux1=self.board
        l=len(self.board.data)-1
        self.list.clear()
        if(len==0):#case where the board is initially empty
            for i in range(len):
                j=rn.randint(0,l)
                self.board.data[i]=j
                self.board.eval()
        else:#case where variants of the existing board are needed
            for k in range(nr):
                i=rn.randint(0,l)
                j=rn.randint(0,l)
                aux=aux1
                aux.data[i]=j
                aux.eval()
                self.list.insert(k,aux)
                if self.list[self.index_best_heur].heur<aux.heur :
                    self.index_best_heur=k;

                    
    def print_b(self):
        print(self.board.data)
        print (self.board.heur)
        
                    
def algorithm_SA(puzzle, Tmax, nr=20):
    goal_heur=100
    T=Tmax;dt=Tmax/100;
    
    if isinstance(puzzle, Puzzle):
        while puzzle.board.heur < goal_heur :
            #puzzle.print_b()
            puzzle.gen_board(nr)
            q=(puzzle.list[puzzle.index_best_heur].heur-puzzle.board.heur)/(puzzle.board.heur)
            p=exp(-q/T)
            p=min(1,p)
            x=rn.random()
            if  x > p :
                puzzle.board=puzzle.list[puzzle.index_best_heur]
            else:
                x=rn.randint(0,len(puzzle.list)-1)
                puzzle.board=puzzle.list[x]
            if(T>10):
                T=T-dt;
        puzzle.print_b()
        puzzle.board.eval()
        
def algorithm_MC():
    pass

puzzle=Puzzle(10)
#puzzle.board.data=[1,3,0,2]
#puzzle.board.eval()
algorithm_SA(puzzle,1000)