#Dariusz Cebula
#Algorytm na początku przygotowuje graf dwudzielny skierowany (z jednej strony pracownicy z drugiej maszyny).
#Dodaje źródło i ujście i nadaje wartości wszystkim krawędziom na 1.
#Korzystając z algorytmu Forda-Fulkersona z użyciem DFS iteracyjnego obliczamy maksymalny przpływ w tym grafie
#Maksymalny przepływ w tym wypadku będzie równy maksymalnemu skojarzeniu co jest odpowiedzią na ten problem
#Szacunkowa złożoność algorytmu O(V^3)

from zad6testy import runtests

from collections import deque                

def DFS_iterative(G,s,t):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    Q = deque()
    Q.append(s)
    visited[s] = True
    while len(Q) != 0:
        u = Q.pop()
        if u == t:
            break
        for v in G[u]:
            if not visited[v[0]] and v[1] > 0:
                visited[v[0]] = True
                parent[v[0]] = u
                Q.append(v[0])
    
    if parent[t] != None:
        return parent
    else:
        return None

def max_flow(G,s,t):
    n = len(G)
    flow = 0
    parent = DFS_iterative(G,s,t)

    while parent != None:
        i = t
        while parent[i] != None:
            G[i].append([parent[i],1])
            G[parent[i]].remove([i,1])
            i = parent[i]
        
        flow += 1
        parent = DFS_iterative(G,s,t)
    
    return flow

def binworker( M ):
    # tu prosze wpisac wlasna implementacje
    n = len(M)
    s = 2*n
    t = 2*n+1
    G = [[] for _ in range(2*n+2)]
    for i in range(n):
        for j in range(len(M[i])):
            G[i].append([M[i][j]+n,1])

        G[s].append([i,1])
        G[i+n].append([t,1])
    
    flow = max_flow(G,s,t)

    return flow

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
