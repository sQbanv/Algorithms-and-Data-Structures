from math import inf
from copy import deepcopy

def Floyd_Warshall(G):
    n = len(G)
    distance = deepcopy(G)
    parent = [[ j for _ in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            if distance[i][j] == inf or distance[i][j] == 0:
                parent[i][j] = None


    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    parent[i][j] = parent[k][j]
    
    return distance,parent

def Path(distance,parent,u,v):
    if parent[u][v] == None:
        return None
    
    d = distance[u][v]
    path = []
    while v != u:
        path.append(v)
        v = parent[u][v]
    path.append(u)
    return path[::-1],d

G = [ [0, 5, 4, 8, inf],
    [-4, 0, -2, inf, 5],
    [inf, inf, 0, 5, 2],
    [-1, 2, inf, 0, -1],
    [inf, inf, 4, 2, 0] ]

distance,parent = Floyd_Warshall(G)
for i in range(len(G)):
    print(distance[i])

for i in range(len(G)):
    print(parent[i])

print(Path(distance,parent,0,4))