#Dariusz Cebula
#Algorytm na początku oblicza najkrótszą drogę bez kradzieży z s do t za pomocą algorytmu Dijkstry
#i zapisuję ją aby potem porównać z drogami które uwzględniają kradzież. Następnie dla każdego wierzchołka
#uruchamia Zmodyfikowany algorytm Dijkstry, który mnoży każdą krawędź przez 2 i dodaje r. Z tej pętli wybieramy
#najlepszą ściężkę która uwzględnia kradzież. Na koniec zwracamy min ze ścieżki bez kradzieży i z kradzieżą
#Szacowana złożoność algorytmu O(V^2logV)

from egz1Atesty import runtests

from queue import PriorityQueue

def relax(distance,parent,u,v,weight):
        if distance[v] > distance[u] + weight:
            distance[v] = distance[u] + weight
            parent[v] = u
            return True
        return False

def Dijkstra(G,s):
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

    return distance

def Dijkstra_stealing(G,s,r):
    n = len(G)
    distance = [float('inf') for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[s] = 0
    Q = PriorityQueue()
    Q.put((0,s))
    while not Q.empty():
        dist, u = Q.get()
        dist = dist
        visited[u] = True
        for v,weight in G[u]:
            weight = weight * 2 + r
            if not visited[v] and relax(distance,parent,u,v,weight):
                Q.put((dist+weight,v))

    return distance

def gold(G,V,s,t,r):
  # tu prosze wpisac wlasna implementacje
  n = len(G)
  distance = Dijkstra(G,s)
  min_path_without_stealing = distance[t]

  min_path_with_stealing = float('inf')
  for i in range(n):
      curr_min = 0
      curr_min += distance[i]
      distance_stealing = Dijkstra_stealing(G,i,r)
      curr_min += distance_stealing[t] - V[i]
      if curr_min < min_path_with_stealing:
          min_path_with_stealing = curr_min


  return min(min_path_without_stealing,min_path_with_stealing)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
