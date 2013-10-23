import sys

def conv_str2int(a):
    res=-1
    try:
        res=int(a)
    except ValueError:
        print("Trying to convert non int to int")
        return -1;
    return res;
class Answer:
    def __init__(self):
        self.NV=0
        self.NE=0
        self.vert=[]#this has a board of type[x y [adjacent nodes]]
        self.edge=[]  
        
def readFile( filename) :
    a=Answer();
    if(isinstance(filename,str)):
        f=open(filename,"r");
        
        #read and store first line
        line=f.readline().strip();
        result=line.partition(" ");
        
        if(result[1] is None):
            print("We are royally done for because file does not exist");
        print("Dimensions ",result);
        
        a.NV=conv_str2int(result[0])
        a.NE=conv_str2int(result[2])
        
        a.vert=[[-1,-1,[]]]*a.NV;
        print(a.vert);
        #read lines 2 to NV+1
        for i in range(a.NV):
            line=f.readline().strip()#get line without whitespace padding
            result=line.partition(" ");
            if(result[1] is None): #separate index from coordinates
                print("We are royally done for because file does not exist");
            index=conv_str2int(result[0]);
            result=result[2].partition(" ");
            if(result[1] is None): #separate coordinates into x and y
                print("We are royally done for because file does not exist");
            #store coordinates:
            a.vert[index][0]=conv_str2int(result[0]);
            a.vert[index][1]=conv_str2int(result[2]);
        for i in range(a.NE):#read the next NE lines to get Edges
            line=f.readline().strip();
            result=line.partition(" ");
            if(result[1] is None):
                print("We are royally done for because file does not exist");
            v1=conv_str2int(result[0]);
            v2=conv_str2int(result[2]);
            if(v2 not in a.vert[v1][2] ):
                a.vert[v1][2].append(v2);
                a.edge.append([v1,v2])
        print("size",a.NV," ",a.NE);
        for i in range(len(a.vert)):
            a.vert[i][2].sort();
            print("Vertice",i,"(",a.vert[i][0],",",a.vert[i][1],")\n",a.vert[i][2],"\n\n\n\n");
    return a;
