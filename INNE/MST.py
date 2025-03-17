from queue import PriorityQueue
from math import inf

def Find(parent,x):
    if parent[x] != x:
        parent[x] = Find(parent, parent[x])
    return parent[x]

def Union(parent,rank,x,y):
    x = Find(parent,x)
    y = Find(parent,y)
    if x == y:
        return
    
    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

def MST_Kruskal(G):
    n = len(G)
    parent = [i for i in range(n)]
    rank = [1 for _ in range(n)]
    edges = []
    MST = []
    taken = 0

    for u in range(n):
        for v,weight in G[u]:
            edges.append((u,v,weight))
    edges = sorted(edges,key=lambda item:item[2])

    for edge in edges:
        if taken == n - 1:
            return MST
        x = Find(parent,edge[0])
        y = Find(parent,edge[1])

        if x != y:
            Union(parent,rank,x,y)
            taken += 1
            MST.append(edge)



G = [[(1,4),(7,8)],[(0,4),(7,11),(2,8)],[(1,8),(8,2),(3,7),(5,4)],[(2,7),(5,14),(4,9)],[(3,9),(5,10)],[(3,14),(4,10),(2,4),(6,2)],[(5,2),(8,6),(7,1)],[(6,1),(8,7),(0,8),(1,11)],[(7,7),(2,2),(6,6)]]
print(MST_Kruskal(G))


def MST_Prim(G):
    n = len(G)
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    weights = [inf for _ in range(n)]
    Q = PriorityQueue()
    Q.put((0,0))
    
    while not Q.empty():
        _,u = Q.get()
        if visited[u]:
            continue
        visited[u] = True
        for v,weight in G[u]:
            if not visited[v] and weight < weights[v]:
                weights[v] = weight
                parent[v] = u
                Q.put((weight,v))
    
    return parent,weights

def get_MST(G):
    parent,weights = MST_Prim(G)
    n = len(G)
    G2 = [[] for _ in range(n)]
    for u in range(n):
        if parent[u] >= 0:
            G2[parent[u]].append((u,weights[u]))
            G2[u].append((parent[u],weights[u]))
    return G2

G = [[(1,4),(7,8)],[(0,4),(7,11),(2,8)],[(1,8),(8,2),(3,7),(5,4)],[(2,7),(5,14),(4,9)],[(3,9),(5,10)],[(3,14),(4,10),(2,4),(6,2)],[(5,2),(8,6),(7,1)],[(6,1),(8,7),(0,8),(1,11)],[(7,7),(2,2),(6,6)]]
print(get_MST(G))