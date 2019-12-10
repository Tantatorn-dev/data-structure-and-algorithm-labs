from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def __str__(self):
        return str(self.graph)

    def BFS(self, s): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph)) 
  
        # Create a queue for BFS 
        queue = [] 
  
        # Mark the source node as  
        # visited and enqueue it 
        queue.append(s) 
        visited[s] = True
  
        while queue: 
  
            # Dequeue a vertex from  
            # queue and print it 
            s = queue.pop(0) 
            print (s, end = " ") 
  
            # Get all adjacent vertices of the 
            # dequeued vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it 
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
        print()

    def DFS(self,s):

        visited = [False]*(len(self.graph))

        stack = []


        stack.append(s)
        visited[s] = True

        while stack:

            s=stack.pop()
            print(s, end=" ")

            for i in self.graph[s]:
                if visited[i] == False:
                    stack.append(i)
                    visited[i] = True
        print()


g = Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(1,4)
g.addEdge(4,1)
g.addEdge(2, 3) 
g.addEdge(3, 2) 
print(g)
g.DFS(2)