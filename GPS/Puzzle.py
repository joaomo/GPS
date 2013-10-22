import random as rn
from math import exp

class Board:
    unit=[0]
    def __init__(self,problem_size=4):
        self.nr_column=problem_size
        self.data=self.unit*self.nr_column
        self.eval=0
    
    def eval(self):
        res=100#result of evaluation
        l=len(self.data)#size of board
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
        self.eval=res
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
                if self.list[self.index_best_heur].eval<aux.eval :
                    self.index_best_heur=k;

                    
    def print_b(self):
        print(self.board.data)
        print (self.board.eval)
        