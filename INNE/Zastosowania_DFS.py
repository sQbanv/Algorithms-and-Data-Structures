#1 Sortowanie topologiczne DAGu
def topological_sort(G):
    def DFS_Visit(G,u):
        nonlocal sorted_graph
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS_Visit(G,v)
        sorted_graph = [u] + sorted_graph

    n = len(G)
    visited = [False for _ in range(n)]
    sorted_graph = []
    
    for u in range(n):
        if not visited[u]:
            DFS_Visit(G,u)

    return sorted_graph

G = [[1,2],[3,2],[4],[5],[5],[6,7],[],[]]
# print(topological_sort(G))

#2 Znajdywanie cyklu Eulera
def euler_cycle(G):
    n = len(G)
    cycle = []

    def DFS_Visit(G,u):
        visited[u] = True
        for v in G[u]:
            G[u].remove(v)
            G[v].remove(u)
            DFS_Visit(G,v)
        cycle.append(u)

    visited = [False for _ in range(n)]

    DFS_Visit(G,0)

    for i in range(n): #sprawdzanie czy spójny i czy wszystkie stopnie wierzchołków parzyste
        if len(G[i])%2 == 1 or visited[i] == False:
            return False

    return cycle

# G = [[1,2],[0,2,3,4],[0,1,3,4],[1,2,4,5],[1,2,3,5],[3,4]]
# print(euler_cycle(G))


def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2

        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][1] >= R[j][1]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

#3 Zliczanie silnie spójnych składowych
def strongly_connected_components(G):
    def DFS_Visit(G,u):
        nonlocal time
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS_Visit(G,v)
        time += 1
        times[u] = time

    def DFS_Visit2(G,u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS_Visit2(G,v)

    n = len(G)
    time = 0
    times = [-1 for i in range(n)]
    visited = [False for _ in range(n)]
    for u in range(n):
        if not visited[u]:
            DFS_Visit(G,u)

    G_T = [[] for _ in range(n)]

    for u in range(n):
        for v in G[u]:
           G_T[v].append(u) 

    print(G_T)

    visited = [False for _ in range(n)]
    for i in range(n):
        times[i] = (i,times[i])
    merge_sort(times)

    counter = 0
    for u in times:
        if not visited[u[0]]:
            DFS_Visit2(G_T,u[0])
            counter += 1

    return counter    

G = [[1],[2],[0,3,8],[4,6],[5],[3],[5],[8],[9],[5,10],[3,7]]
# G = [[1],[2],[0,3,8],[4,6],[5],[3,9],[5],[8],[9],[10],[3,7]]
# print(strongly_connected_components(G))


#4 Znajdywanie mostów w grafie
def find_bridges(G):
    def DFS_Visit(G,u):
        nonlocal time
        visited[u] = True
        times[u] = time
        low[u] = time
        time += 1

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFS_Visit(G,v)

                low[u] = min(low[u],low[v])

                if low[v] > times[u]:
                    bridges.append((u,v))
            
            elif v != parent[u]:
                low[u] = min(low[u], times[v])

    
    n = len(G)
    time = 0
    times = [-1 for _ in range(n)]
    low = [float('inf') for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    bridges = []
    for u in range(n):
        if not visited[u]:
            DFS_Visit(G,u)
    
    return bridges



G = [[1,6],[0,2],[1,3,6],[2,4,5],[3,5],[3,4],[0,2,7],[6]]
# print(find_bridges(G))