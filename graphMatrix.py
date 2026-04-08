class Graph:
    def __init__(self, vertex):
        self.mat=[[0]*vertex for x in range(vertex)]
        self.size = vertex

    def add_edge(self,src,dest):
        if 0<=src<self.size and 0<dest<self.size:
            self.mat[src][dest]=1
            self.mat[dest][src]=1
        else:
            print("Invalid value!!")
        

    def remove_edge(self,src,dest):
        if 0<=src<self.size and 0<dest<self.size :
            self.mat[src][dest]=0
            self.mat[dest][src]=0
        else:
            print("Invalid value!!")
            
        
    def printGraph(self):
        for i in self.mat:
            print(' '.join(map(str,i)))
            # print(i,end="\n")
            
        

g=Graph(4)
g.add_edge(0,1)
g.add_edge(1,3)
g.add_edge(2,1) 
g.remove_edge(2,1)
g.printGraph()
