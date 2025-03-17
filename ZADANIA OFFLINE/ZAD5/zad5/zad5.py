#Dariusz Cebula
#Algorytm na początku konwertuje dane krawędzie na graf w reprezentacji listy sąsiedztwa
#Potem tworzy w tym grafie cykl pomiędzy wierzchołkami z tablicy S z krawędziami o wadze 0
#Na koniec przeszukujemy graf za pomocą algorytmu Dijkstra, który najkrótszą ścieżkę w grafie ważonym
#Szacunkowa złożoność algorytmu O(E*logV)

from zad5testy import runtests
from queue import PriorityQueue

def relax(u,v,distance):
    if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        return True
    return False

def Dijkstra(G,s):
    n = len(G)
    distance = [float('inf') for _ in range(n)]
    visited = [False for _ in range(n)]
    distance[s] = 0
    Q = PriorityQueue()
    Q.put((0,s))
    while not Q.empty():
        dist, u = Q.get()
        for v in G[u]:
            if not visited[v[0]] and relax(u,v,distance):
                Q.put((dist + v[1],v[0]))
        visited[u] = True
    return distance


def spacetravel( n, E, S, a, b ):
    # tu prosze wpisac wlasna implementacje
    G = [[] for _ in range(n)]
    for i in range(len(E)):
        G[E[i][0]].append((E[i][1],E[i][2]))
        G[E[i][1]].append((E[i][0],E[i][2]))

    for i in range(len(S)-1):
        G[S[i]].append((S[i+1],0))

    G[S[len(S)-1]].append((S[0],0))
    distance = Dijkstra(G,a)

    if distance[b] == float('inf'):
        return None
    else:
        return distance[b]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
