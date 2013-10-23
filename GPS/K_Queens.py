import random as rn
from math import exp
import pdb
import Puzzle
import copy

class K_Board(Puzzle.Board):#puzzle specific
    def __init__(self,size_matrix=4):
        self.nr_column=size_matrix
        self.data=[]
        self.heur=0
        self.con_nodes=[[]]
        self.conflicts=0
    
    def eval(self):#for Kqueens
        res=100
        l=len(self.data)
        count=0
        diag=0
        conflicts=0
        a=set();
        self.con_nodes.clear()
        for j in range(l):
            i=self.data[j]
            for k in range(1,j+1):#diagonal back
                if (j>=0 and i-k>=0 and self.data[j-k]==i-k):
                    diag+=1;
                    if(j not in self.con_nodes):
                        self.con_nodes.append(j)
                    if(j-k not in self.con_nodes):
                        self.con_nodes.append(j-k)                    
                if (j-k>=0 and i+k<l and self.data[j-k]==i+k):
                    diag+=1
                    if(j not in self.con_nodes):
                        self.con_nodes.append(j)
                    if((j-k) not in self.con_nodes):
                        self.con_nodes.append(j-k)
                        
            if i in a:
                count+=1
                for k in range(l):
                    if(self.data[k]==i and k not in self.con_nodes):
                        self.con_nodes.append(k)
            a.add(i)
        if ((count > 0) | (diag >0)):
            res-=(4**count+diag)
            conflicts+=count+diag
        self.heur=res
        self.conflicts=conflicts
        
        
class K_Puzzle(Puzzle.Puzzle):#puzzle specific
    
    def __init__(self,size=4):
        self.board = K_Board(size)
        self.list=[]
        self.index_best_heur=0
        self.gen_board()
      
      
    def gen_board(self,nr=20,ind=-1):
        l=len(self.board.data)-1
        self.list.clear()
        self.index_best_heur=0
        if(l<1):#case where the board is initially empty
            self.board.data=[0]*self.board.nr_column
            for i in range(self.board.nr_column):
                j=rn.randint(0,self.board.nr_column-1)
                self.board.data[i]=j
            self.board.eval()
        else:#case where variants of the existing board are needed
            aux1=copy.copy(self.board)
            for k in range(nr):
                if ind!=-1:
                    i=ind
                    j=aux1.data[i];
                    while j==aux1.data[i]:
                        j=rn.randint(0,l)
                else:
                    i=rn.randint(0,l)
                    j=rn.randint(0,l)
                #print(i,j)
                aux=copy.deepcopy(aux1)
                aux.data[i]=j
                aux.eval()
                #print(aux.data)
                self.list.insert(k,aux)
                #print(self.list[k].data,"\n\n\n\n\n\n\n" )
                if (ind==-1 and self.list[self.index_best_heur].heur<aux.heur) :
                    self.index_best_heur=k;
#         for it in self.list:
#             print (it.data);
                    
    def print_b(self):
        print(self.board.data)
        print (self.board.heur)
        
