#Dariusz Cebula
#Algorytm na początku za pomocą BFS znajduje najkrótszą ścieżkę od s do t.
#Potem w pętli próbujemy usuwać kolejne krawędzie wzdłóż tej ścieżki i dla każdej usuniętej uruchamimy BFS
#aby sprawdzić czy nie wydłużyło to ścieżki.
#Złożoność algorytmu O((V+E)*E)

from zad4testy import runtests
from collections import deque

def BFS(G,s,t):
    n = len(G)
    d = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    Q = deque()
    Q.append(s)
    d[s] = 0
    visited[s] = True
    while len(Q) != 0:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                d[v] = d[u] + 1
                visited[v] = True
                parent[v] = u
                Q.append(v)
    return d[t]

def longer( G, s, t ):
    # tu prosze wpisac wlasna implementacje 
    n = len(G)
    d = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    Q = deque()
    Q.append(s)
    d[s] = 0
    visited[s] = True
    while len(Q) != 0:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                d[v] = d[u] + 1
                visited[v] = True
                parent[v] = u
                Q.append(v)
    
    if d[t] == -1:
        return None
    else:
        length = d[t]

    prev = t
    curr = parent[t]
    while curr is not None:
        e = (curr,prev)
        G[curr].remove(prev)
        curr_length = BFS(G,s,t)
        if curr_length > length or curr_length == -1:
            return e
        G[curr].append(prev)
        prev = curr
        curr = parent[prev]

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )