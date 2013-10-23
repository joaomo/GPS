import random as rn
from math import exp
import Puzzle as P
#primeiro fazer o programa e depois torna lo modular.       

class solver:
# Solver tem de ter um puzzle aqui apresentado como board
    def __init__(self):
        pass
    
        # nr is the number of neigbours generated 
        #Tmax not necessary yet
        #Structure with the board
    def algorithm_SA(self,puzzle, Tmax=1000, nr=20):
        goal_heur=100
        T=Tmax;dt=Tmax/100;
        
        if isinstance(puzzle, P.Puzzle):
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
            print("WIN!!!!")
            puzzle.print_b()
            puzzle.board.eval()

    def algorithm_MC(self,puzzle,nr=20):#Funciona com K_Queens
        eligible=[]
        current_best=10000
        count=0
        #pdb.set_trace()
        puzzle.board.eval();
        if isinstance(puzzle, P.Puzzle):
            while puzzle.board.conflicts>0:
    #             current_best=puzzle.board.conflicts
                count+=1
                eligible.clear();
                size=len(puzzle.board.con_nodes)
                i=rn.randint(0,size-1) #choose only if involved in conflicts 
                i=puzzle.board.con_nodes[i]
    #             print("\t",i,puzzle.board.data[i])
                puzzle.gen_board(nr,i);
    #             print(i,puzzle.board.data[i])
                puzzle.board.eval();
                #pdb.set_trace()
                for it in puzzle.list:
                    if(it.conflicts<current_best):
                        print("I am better than you",it.conflicts,current_best)
                        eligible.clear();
                        current_best=it.conflicts;
                        eligible.append(it);
                    elif(it.conflicts==current_best):
                        eligible.append(it);
    #                 else:
    #                     print("You are not better than me!!!");
                #pdb.set_trace()
                if(len(eligible)==1):
                    puzzle.board=eligible.pop();
                elif(len(eligible)>1):
                    i=rn.randint(0,len(eligible)-1);
                    puzzle.board=eligible[i];
    #             puzzle.print_b()
    
            print("WIN!!!!!",count);
            puzzle.print_b();    