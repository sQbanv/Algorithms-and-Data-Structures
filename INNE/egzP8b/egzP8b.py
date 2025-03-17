from egzP8btesty import runtests

def Floyd_Warshall(G):
    n = len(G)
    for i in range(n):
        for j in range(n):
            if G[i][j] == 0:
                G[i][j] = float('inf')

    for k in range(n):
        for i in range(n):
            for j in range(n):
                G[i][j] = min(G[i][j],G[i][k] + G[k][j])

    return G


def robot( G, P ):
    #Tutaj proszę wpisać własną implementację
    n = len(G)
    G2 = [[0 for _ in range(n)] for _ in range(n)]

    for u in range(n):
        for v,weight in G[u]:
            G2[u][v] = weight
            G2[v][u] = weight
    
    Floyd_Warshall(G2)

    result = 0
    for i in range(len(P)-1):
        result += G2[P[i]][P[i+1]]
    
    return result
    
runtests(robot, all_tests = True)
