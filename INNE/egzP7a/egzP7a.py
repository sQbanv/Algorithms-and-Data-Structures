from egzP7atesty import runtests 

def dfs(G,s,t,parent):
    def dfs_visit(G,visited,parent,u):
        visited[u] = True
        for v in range(len(G)):
            if not visited[v] and G[u][v] != 0:
                parent[v] = u
                dfs_visit(G,visited,parent,v)

    n = len(G)
    visited = [False for _ in range(n)]
    dfs_visit(G,visited,parent,s)
    return visited[t]

def Ford_Fulkerson_Matrix(G,s,t):
    n = len(G)
    parent = [None for _ in range(n)]
    max_flow = 0
    while dfs(G,s,t,parent):
        curr_flow = float('inf')
        curr = t
        while curr != s:
            curr_flow = min(curr_flow, G[parent[curr]][curr])
            curr = parent[curr]
        max_flow += curr_flow
        v = t
        while v != s:
            u = parent[v]
            G[u][v] -= curr_flow
            G[v][u] += curr_flow
            v = parent[v]
    return max_flow


def akademik( T ):
    #Tutaj proszę wpisać własną implementację
    s = len(T)*2
    t = s + 1
    n = t + 1
    n1 = len(T)

    G2 = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n1):
        for j in range(len(T[i])):
            if T[i][j] != None:
                G2[i][T[i][j]+n1] = 1
    for i in range(n1):
        G2[s][i] = 1
        G2[i+n1][t] = 1

    counter = 0
    for i in range(n1):
        if T[i] == (None,None,None):
            counter += 1

    max_flow = Ford_Fulkerson_Matrix(G2,s,t)

    return n1 - max_flow - counter

runtests ( akademik )
