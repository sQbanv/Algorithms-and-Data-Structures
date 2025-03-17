from queue import PriorityQueue

def relax(u,v,distance,parent):
    if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        parent[v[0]] = u
        return True
    return False

def Dijkstra(G,s):
    n = len(G)
    distance = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    distance[s] = 0
    Q = PriorityQueue()
    Q.put((0,s))
    while not Q.empty():
        dist, u = Q.get()
        for v in G[u]:
            if not visited[v[0]] and relax(u,v,distance,parent):
                Q.put((dist + v[1],v[0]))
        visited[u] = True
    return parent,distance


G = [[(1,5),(2,0),(3,0)],[(0,5),(2,21),(3,1)],[(0,0),(1,21),(3,0),(4,7)],[(0,0),(1,1),(2,0),(4,13),(5,16)],[(2,7),(3,13),(6,4)],[(3,16),(6,1)],[(4,4),(5,1)]]
print(Dijkstra(G,1))

def relax(u,v,distance,parent):
    if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        parent[v[0]] = u
        return True
    return False

def Bellman_Ford(G,s):
    n = len(G)
    distance = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[s] = 0

    for _ in range(n-1):
        for u in range(n):
            for v in G[u]:
                relax(u,v,distance,parent)

    for u in range(n):
        for v in G[u]:
            if distance[v[0]] > distance[u] + v[1]:
                return False

    return parent,distance

G3 = [[(1,3)],[(2,1)],[(3,2)],[(1,-7),(4,-7)],[]]
G4 = [[(1,6),(2,7)],[(3,5),(2,8),(4,-4)],[(3,-3),(4,9)],[(1,-2)],[(3,7),(0,2)]]
print(Bellman_Ford(G4,0))