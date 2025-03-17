from collections import deque
from queue import PriorityQueue

def BFS(G,s): #O(V+E) - listowa; O(V^2) - macierzowa
    n = len(G)
    distance = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[s] = 0
    visited[s] = True
    Q = deque()
    Q.append(s)
    while len(Q) != 0:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                distance[v] = distance[u] + 1
                parent[v] = u
                visited[v] = True
                Q.append(v)
    
    return distance,parent,visited


def DFS(G): #O(V+E) - listowa; O(V^2) - macierzowa
    def DFS_Visit(G,u):
        nonlocal time
        visited[u] = True
        times[u] = time
        time += 1
        for v in G[u]:
            if not visited[v]:
                parent[v] = v
                DFS_Visit(G,v)

    n = len(G)
    time = 0
    times = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    for u in range(n):
        if not visited[u]:
            DFS_Visit(G,u)

    return times,parent


def topological_sort(G): #O(V+E) - listowa; O(V^2) - macierzowa
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


def euler_cycle(G): #O(V+E) - listowa; O(V^2) - macierzowa | łatwo popaść w pułapke O(V^2 + VE) - listowa; O(V^3) - macierzowa
    def DFS_Visit(G,u):
        visited[u] = True
        for v in G[u]:
            G[u].remove(v)
            G[v].remove(u)
            DFS_Visit(G,v)
        cycle.append(u)

    n = len(G)
    visited = [False for _ in range(n)]
    cycle = []

    DFS_Visit(G,0)

    for i in range(n): #sprawdzanie czy spójny i parzysty stopień wierzchołka
        if len(G[i])%2 == 1 or visited[i] == False:
            return False
        
    return cycle


def strongly_conected_components(G): #O(V+E) - listowa; O(V^2) - macierzowa
    def DFS_Visit_1(G,u):
        nonlocal time
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS_Visit_1(G,v)
        time += 1
        times[u] = time

    def DFS_Visit_2(G,u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS_Visit_2(G,v)

    n = len(G)
    time = 0
    visited = [False for _ in range(n)]
    times = [-1 for _ in range(n)]
    for u in range(n):
        if not visited[u]:
            DFS_Visit_1(G,u)

    G_T = [[] for _ in range(n)]

    for u in range(n):
        for v in G[u]:
            G_T[v].append(u)

    for i in range(n):
        times[i] = (i,times[i])
    times = sorted(times,key=lambda item:item[1])
    visited = [False for _ in range(n)]

    counter = 0
    for u in times:
        if not visited[u[0]]:
            DFS_Visit_2(G_T,u[0])
            counter += 1
    
    return counter


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
                low[u] = min(low[u],times[v])
                

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

def find_articulation_points(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    discovery_time = [float('inf')] * num_vertices
    low_time = [float('inf')] * num_vertices
    parent = [-1] * num_vertices
    is_articulation_point = [False] * num_vertices
    time = 0

    def dfs(vertex):
        nonlocal time
        children_count = 0
        visited[vertex] = True
        discovery_time[vertex] = low_time[vertex] = time
        time += 1

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                parent[neighbor] = vertex
                children_count += 1
                dfs(neighbor)
                low_time[vertex] = min(low_time[vertex], low_time[neighbor])

                if parent[vertex] == -1 and children_count > 1:
                    is_articulation_point[vertex] = True

                if parent[vertex] != -1 and low_time[neighbor] >= discovery_time[vertex]:
                    is_articulation_point[vertex] = True

            elif neighbor != parent[vertex]:
                low_time[vertex] = min(low_time[vertex], discovery_time[neighbor])

    for v in range(num_vertices):
        if not visited[v]:
            dfs(v)

    articulation_points = []
    for v in range(num_vertices):
        if is_articulation_point[v]:
            articulation_points.append(v)

    return articulation_points


def Dijkstra(G,s): # O(ElogV) - listowa; O(V^2) - macierzowa
    def relax(distance,parent,u,v,weight):
        if distance[v] > distance[u] + weight:
            distance[v] = distance[u] + weight
            parent[v] = u
            return True
        return False


    n = len(G)
    distance = [float('inf') for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[s] = 0
    Q = PriorityQueue()
    Q.put((0,s))
    while not Q.empty():
        dist, u = Q.get()
        visited[u] = True
        for v,weight in G[u]:
            if not visited[v] and relax(distance,parent,u,v,weight):
                Q.put((dist+weight,v))

    return distance,parent


def Bellman_Ford(G,s): # O(VE)
    def relax(distance,parent,u,v,weight):
        if distance[v] > distance[u] + weight:
            distance[v] = distance[u] + weight
            parent[v] = u
            return True
        return False

    n = len(G)
    distance = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[s] = 0

    for i in range(n-1):
        for u in range(n):
            for v,weight in G[u]:
                relax(distance,parent,u,v,weight)

    for u in range(n):
        for v,weight in G[u]:
            if distance[v] > distance[u] + weight:
                return False
            
    return distance,parent


def Floyd_Warshalla(G): # O(V^3)
    n = len(G)
    distance = G
    parent = [[j for _ in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if distance[i][j] == float('inf') or distance[i][j] == 0:
                parent[i][j] = None

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    parent[i][j] = parent[k][j]

    for i in range(n):
        if distance[i][i] < 0:
            #negative weight cycle
            return False
        
    return parent

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
        

def Find(parent,x):
    if x != parent[x]:
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
    
    return MST


def MST_Prim(G):
    n = len(G)
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    weights = [float('inf') for _ in range(n)]
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


def bfs(G,s,t,parent):
    n = len(G)
    Q = deque()
    visited = [False for _ in range(n)]
    visited[s] = True
    Q.append(s)
    while len(Q) != 0:
        u = Q.popleft()
        for v in range(n):
            if not visited[v] and G[u][v] != 0:
                visited[v] = True
                parent[v] = u
                Q.append(v)
    return visited[t]


def edmonds_karp_matrix(G,s,t):
    n = len(G)
    parent = [None for _ in range(n)]
    max_flow = 0
    while bfs(G,s,t,parent):
        curr_flow = float('inf')
        curr = t
        while curr != s:
            curr_flow = min(curr_flow,G[parent[curr]][curr])
            curr = parent[curr]
        max_flow += curr_flow
        v = t
        while v != s:
            u = parent[v]
            G[u][v] -= curr_flow
            G[v][u] += curr_flow
            v = parent[v]
    return max_flow