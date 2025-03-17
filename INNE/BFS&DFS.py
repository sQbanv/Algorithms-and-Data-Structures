from queue import Queue
from collections import deque


#BFS dla listy sąsiedztwa
def BFS_list(G,s):
    n = len(G)
    d = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    Q = Queue()
    Q.put(s)
    visited[s] = True
    d[s] = 0
    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if not visited[v]:
                d[v] = d[u] + 1
                parent[v] = u
                visited[v] = True
                Q.put(v)

    return d,parent,visited


#BFS dla macierzy sąsiedztwa
def BFS_matrix(G,s):
    n = len(G)
    d = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    Q = deque();
    Q.append(s)
    d[s] = 0
    visited[s] = True
    while len(Q) != 0:
        u = Q.popleft()
        for v in range(n):
            if G[u][v] == 1 and not visited[v]:
                d[v] = d[u] + 1
                visited[v] = True
                parent[v] = u
                Q.append(v)

    return d,parent,visited


#DFS dla listy sąsiedztwa
def DFS_list(G):
    def DFS_visit(G,u):
        nonlocal time
        time += 1
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFS_visit(G,v)
        time += 1

    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    time = 0
    for u in range(n):
        if not visited[u]:
            DFS_visit(G,u)
        
    return time,parent,visited


#DFS dla macierzy sąsiedztwa
def DFS_matrix(G):
    def DFS_visit(G,u):
        nonlocal time
        time += 1
        visited[u] = True
        for v in range(n):
            if G[u][v] == 1 and not visited[v]:
                parent[v] = u
                DFS_visit(G,v)
        time += 1

    n = len(G)
    time = 0
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    for u in range(n):
        if not visited[u]:
            DFS_visit(G,u)

    return time,parent,visited


#sortowanie topologiczne dla listy sąsiedztwa
def topological_sort_list(G):
    def DFS_visit(G,u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS_visit(G,v)
        topologic.append(u)

    n = len(G)
    visited = [False for _ in range(n)]
    topologic = []
    for u in range(n):
        if not visited[u]:
            DFS_visit(G,u)

    return topologic[::-1]


#sortowanie topologiczne dla macierzy sąsiedztwa
def topological_sort_matrix(G):
    def DFS_visit(G,u):
        visited[u] = True
        for v in range(n):
            if G[u][v] == 1 and not visited[v]:
                DFS_visit(G,v)
        topologic.append(u)

    n = len(G)
    visited = [False for _ in range(n)]
    topologic = []
    for u in range(n):
        if not visited[u]:
            DFS_visit(G,u)

    return topologic[::-1]


G = [ #lista sąsiedztwa
[1,2], #0
[0,4], #1
[0,3,5], #2
[2,4], #3
[1,3,5], #4
[2,4,6], #5
[5,7], #6
[6] #7
]

G_2 = [ #macierz sąsiedztwa    
[0,1,1,0,0,0,0,0], #0
[1,0,0,0,1,0,0,0], #1
[1,0,0,1,0,1,0,0], #2
[0,0,1,0,1,0,0,0], #3
[0,1,0,1,0,1,0,0], #4
[0,0,1,0,1,0,1,0], #5
[0,0,0,0,0,1,0,1], #6
[0,0,0,0,0,0,1,0]  #7
]

# print(G)
# print(BFS_list(G,0))

# for i in range(len(G_2)):
#     print(G_2[i])
# print(BFS_matrix(G_2,0))

# print(G)
# print(DFS_list(G))

# for i in range(len(G_2)):
#     print(G_2[i])
# print(DFS_matrix(G_2))

G2 = [ #graf skierowany acykliczcny (lista sąsiedztwa)
[1,2],
[2,4],
[],
[],
[3,6],
[4],
[]
]

G2_2 = [ #graf skierowany acykliczny (macierz sąsiedztwa)
[0,1,1,0,0,0,0],
[0,0,1,0,1,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,1,0,0,1],
[0,0,0,0,1,0,0],
[0,0,0,0,0,0,0]
]

# print(G2)
# print(topological_sort_list(G2))

# for i in range(len(G2_2)):
#     print(G2_2[i])
# print(topological_sort_matrix(G2_2))