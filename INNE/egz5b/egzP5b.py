from egzP5btesty import runtests 

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



# def find_articulation_points(G):
#     n = len(G)
#     low    = [0] * n
#     times  = [0] * n
#     is_art = [False] * n
#     time   = 0
    
#     def dfs(root, u, parent):
#         nonlocal time
#         time += 1
#         low[u] = times[u] = time
#         out_deg = 0
        
#         for v in G[u]:
#             if v == parent: continue
#             if not times[v]:
#                 out_deg += dfs(root, v, u) + u == root
#                 low[u] = min(low[u], low[v])
#                 if times[u] <= low[v]:
#                     is_art[u] = True
#             else:
#                 low[u] = min(low[u], times[v])
        
#         return out_deg
    
#     return is_art

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

def koleje ( B ):
    #tutaj proszę wpisać własną implementację
    for i in range(len(B)):
        if B[i][0] > B[i][1]:
            B[i] = (B[i][1],B[i][0])
    
    B = sorted(B,key=lambda item:item[1])
    B = sorted(B,key=lambda item:item[0])
    
    n = 0
    for edge in B:
        n = max(n,edge[1])
    n += 1
    G = [[] for _ in range(n)]
    last = None
    for i in range(len(B)):
        if last != B[i]:
            last = B[i]
            G[B[i][0]].append(B[i][1])
            G[B[i][1]].append(B[i][0])
    
    articulation_points = find_articulation_points(G)

    return len(articulation_points)

runtests ( koleje, all_tests=True )
