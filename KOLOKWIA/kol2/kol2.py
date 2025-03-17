#Dariusz Cebula
#Algorytm na początku znajduje MST za pomocą algorytmu Kruskala przy pomocy Find i Union.
#Po znalezieniu MST sprawdza czy spełnia on warunki podane w zadaniu jeśli tak to zlicza wartości krawędzi i zwaraca
#a jeśli nie to usuwa największą krawędż z MST i uruchamia algorytm jeszcze raz do momentu 
#aż będzie możliwe utworzenie MST
#Szacowana złożoność O(VE*logE)

from kol2testy import runtests

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

def beautree(G):
    # tu prosze wpisac wlasna implementacje
    # print(G)
    n = len(G)
    curr_edges = []
    for u in range(n):
        for v,weight in G[u]:
            curr_edges.append([u,v,weight])

    curr_edges = sorted(curr_edges,key=lambda item:item[2])
    
    edges = []
    for i in range(0,len(curr_edges),2):
        edges.append(curr_edges[i])
    # print(edges)
    # print(edges)
    while len(edges) > n - 1:
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]
        MST = []
        rest = []
        taken = 0
        m = float('inf')
        M = -1
        for edge in edges:
            x = Find(parent,edge[0])
            y = Find(parent,edge[1])
            if x != y:
                if taken == 0:
                    m = edge[2]
                if taken == n - 2:
                    M = edge[2]
                Union(parent,rank,x,y)
                taken += 1
                MST.append(edge)
            else:
                rest.append(edge)

        if len(MST) < n - 1:
            return None 
        m_rest = rest[0][2]
        M_rest = rest[len(rest)-1][2]
        if M_rest < m or m_rest > M:
            break
        else:
            to_remove = MST[len(MST) - 1]
            edges.remove(to_remove)
        
       
        # print(m,M)
        # print(MST)
        # print(rest)

    # print(MST)
    sum = 0
    for i in range(len(MST)):
        sum += MST[i][2]

    return sum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )
