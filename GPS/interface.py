import sys 
import solver as sol
import K_Queens as K
import colorgraphreader as gr
class Simple_interface():
    
    def __init__(self):
        pass
    
    def main(self):
        solver= sol.solver();
        i=0;
        answer=""
        while i!=-1:
            print("Please chose one of the modes");
            print("1.SA-KQ");
            print("2.SA-GC");
            print("3.MC-KQ");
            print("4.MC-GC");
            print("5.Exit");
            answer=input(">>");
            try:
                index=int(answer);
            except ValueError:
                continue;
            if(index==1):
                print("1")
                print("Puzzle size ");
                answer=input(">>");
                nr=gr.conv_str2int(answer)
                puzzle=K.K_Puzzle(nr)
                print("How many neighbours? ");
                answer=input(">>");
                nr=gr.conv_str2int(answer)
                solver.algorithm_SA(puzzle,nr)
            elif(index==2):
                print("2")
            elif(index==3):
                print("3")
                print("Puzzle size ");
                answer=input(">>");
                nr=gr.conv_str2int(answer)
                puzzle=K.K_Puzzle(nr)
                print("How many neighbours? ");
                answer=input(">>");
                nr=gr.conv_str2int(answer)
                solver.algorithm_MC(puzzle,nr)
            elif(index==4):
                print("4")
            elif(index==5):
                print("5")
                i=-1
                
inter=Simple_interface()
inter.main();
    