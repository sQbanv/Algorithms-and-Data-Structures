#Dariusz Cebula
#Algorytm na początku przygotowuje graf dwudzielny skierowany (z jednej strony pracownicy z drugiej maszyny).
#Dodaje źródło i ujście i nadaje wartości wszystkim krawędziom na 1.
#Korzystając z algorytmu Forda-Fulkersona z użyciem DFS iteracyjnego obliczamy maksymalny przpływ w tym grafie
#Maksymalny przepływ w tym wypadku będzie równy maksymalnemu skojarzeniu co jest odpowiedzią na ten problem
#Szacunkowa złożoność algorytmu O(V^3)

from zad6testy import runtests

from collections import deque                

def DFS(G,s,t):
    flag = True
    def DFS_Vistit(G,u):
        nonlocal flag
        visited[u] = True
        if u == t:
            flag = False
        for i in range(len(G[u])):
            if flag and not visited[G[u][i][0]] and G[u][i][1] > 0:
                G[u][i][1] = 0 # ustawianie na 0 jak użyliśmy krawędź
                parent[G[u][i][0]] = u
                DFS_Vistit(G,G[u][i][0])

    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    DFS_Vistit(G,s)

    if not flag:
        return parent
    else:
        return None

def max_flow(G,s,t):
    n = len(G)
    flow = 0
    parent = DFS(G,s,t)

    while parent != None:
        i = t
        while parent[i] != None:
            G[i].append([parent[i],1]) #tworzenie sieci rezydualnej
            i = parent[i]

        flow += 1
        parent = DFS(G,s,t)
    
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
            # G[M[i][j]+n].append((i,0))

        G[s].append([i,1])
        # G[i].append((s,0))

        G[i+n].append([t,1])
        # G[t].append((i+n,0))

    # print(G)

    # print(DFS(G,s,t))
    # print(DFS_2(G,s,t))
    
    flow = max_flow(G,s,t)

    return flow

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
