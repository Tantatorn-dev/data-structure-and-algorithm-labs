from collections import defaultdict

adj = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


def matrixToList(matrix):
    graph = defaultdict(list)
    for i in range(len(matrix)):
        graph[i] = []
        for n in range(len(matrix[i])):
            if matrix[i][n] == 1:
                graph[i].append(n)
    return graph


visited = [False]*len(adj)


def addEdge(adj,start, stop):
    adj[start][stop] = 1
    adj[stop][start] = 1


def DFS(adjList, start,stop, visited,ans=[]):

    if start == stop:
        return ans+[stop]

    visited[start] = True
    ans.append(start)

    for i in adjList[start]:
        if visited[i] == False:
            return DFS(adjList, i,stop, visited)


def BFS(adjList, start, stop, visited, ans=[]):

    queue = []

    queue.append(start)
    visited[start] = True

    while queue:

        s = queue.pop(0)
        ans.append(s)

        for i in adjList[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

    return ans


addEdge(adj,0, 1)
addEdge(adj,1, 2)
adjList = matrixToList(adj)

print(DFS(adjList, 0, 2, visited))
