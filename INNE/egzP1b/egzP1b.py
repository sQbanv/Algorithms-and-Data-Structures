from egzP1btesty import runtests 

from queue import PriorityQueue
from math import inf


def turysta( G, D, L ):
    # #tutaj proszę wpisać własną implementację
    # # n = 0
    # # for i in G:
    # #     if i[0] > n:
    # #         n = i[0]
    # #     if i[1] > n:
    # #         n = i[1]
    # # n += 1
    # n = L + 1
    # # print(G)
    # G2 = [[] for _ in range(n)]
    # for i in range(len(G)):
    #     G2[G[i][0]].append((G[i][1],G[i][2]))
    #     G2[G[i][1]].append((G[i][0],G[i][2]))

    # # print(G2)
    # # print(G2[L])
    # return Dijkstra(G2,D,L)
    size = 0
    for v, u, w in G:
        size = max(size, u)
    N = [[]for _ in range(size + 1)]
    for v, u, w in G:
        N[v].append((u, w))
        N[u].append((v, w))
    distance = [[inf]*3 for _ in range(size + 1)]
    q = PriorityQueue()
    for i in range(3):
        distance[D][i] = 0
    q.put((0, D, 3))
    while not q.empty():
        w1, v, ilosc = q.get()
        for u, w2 in N[v]:
            if ilosc > 0 and u != L:
                if distance[u][ilosc - 1] > w1 + w2:
                    distance[u][ilosc - 1] = w1 + w2
                    q.put((distance[u][ilosc - 1], u, ilosc - 1))
            elif ilosc == 0 and u == L:
                distance[L][0] = min(distance[L][0], w1 + w2)
    return min(distance[L])

runtests ( turysta )

# G = [
# (0, 1, 9), (0, 2, 1),
# (1, 2, 2), (1, 3, 8),
# (1, 4, 3), (2, 4, 7),
# (2, 5, 1), (3, 4, 7),
# (4, 5, 6), (3, 6, 8),
# (4, 6, 1), (5, 6, 1)
# ]
# D = 0
# L = 6
# print(turysta(G,D,L))