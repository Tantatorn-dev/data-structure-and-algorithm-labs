# no weight graph
graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

def find_path(graph:dict,start,end,path=[]):

    path = path + [start]
    if start == end: # I am at sen chai 
        return path
    if start not in graph: # no start point
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph,node,end,path)
            if newpath: 
                return newpath
    return None

def find_all_paths(graph:dict,start,end,path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph,node,end,path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def find_shortest_paths(graph:dict,start,end):
    paths = find_all_paths(graph,start,end)
    shortest_paths = []
    path_length = []
    for path in paths:
        path_length.append(len(path))
    shortest_length = min(path_length)
    for path in paths:
        if len(path) == shortest_length:
            shortest_paths.append(path)
    return shortest_paths


print(find_shortest_paths(graph,'A','D'))