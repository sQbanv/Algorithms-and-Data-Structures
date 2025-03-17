from egzP3btesty import runtests 
from queue import PriorityQueue

def Find(parent,x):
    if parent[x] != x:
        parent[x] = Find(parent,parent[x])
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


def lufthansa ( G ):
    #tutaj proszę wpisać własną implementację 
    n = len(G)
    parent = [i for i in range(n)]
    rank = [1 for _ in range(n)]
    edges = []
    MST = []
    result = []
    taken = 0

    for u in range(n):
        for v,weight in G[u]:
            edges.append((u,v,weight))
    
    edges = sorted(edges,reverse=True,key=lambda item:item[2])

    for edge in edges:
        if taken == n - 1:
            break
        
        x = Find(parent,edge[0])
        y = Find(parent,edge[1])

        if x != y:
            Union(parent,rank,x,y)
            taken += 1
            MST.append(edge)
    
    for edge in MST:
        edges.remove(edge)
        edges.remove((edge[1],edge[0],edge[2]))

    edges = sorted(edges,reverse=True,key=lambda item:item[2])
    
    result = 0
    for i in range(2,len(edges),2):
        result += edges[i][2]
    
    return result

runtests ( lufthansa, all_tests=True )


# G = [
# [(1, 15), (2, 5), (3, 10) ],
# [(0, 15), (2, 8), (4, 5), (5, 12)],
# [(0, 5), (1, 8), (3, 5), (4, 6) ],
# [(0, 10), (2, 5), (4, 2), (5, 11)],
# [(1, 5), (2, 6), (3, 2), (5, 2) ],
# [(1, 12), (4, 2), (3, 11) ]
# ]
# print(lufthansa(G))