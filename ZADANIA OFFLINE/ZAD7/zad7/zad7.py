#Dariusz Cebula
#Algorytm tworzy tablice F n x n gdzie F[i][j] to najdłuższa droga do miejsca (i,j)
#Algorytm na początku przechodzi po pierwszej kolumnie i zapisuje ilość kroków do przejścia
#Potem przechodzi w pętli po reszcie kolumn, gdzie raz przechodzi od 0 do n-1 a drugi raz odwrotnie.
#jednocześnie sprawdzając drogi z których można dojść do tego miejsca i dodaje do wyniku 1 ruch.
#Na koniec zwraca wartość na elemencie (n-1,n-1)
#Szacowana złożoność algorytmu O(n^2)

from zad7testy import runtests
        
def maze(L):
    n = len(L)
    F = [[-1 for _ in range(n)] for _ in range(n)]
    flag = False
    for i in range(n):
        if L[i][0] == '#':
            flag = True
        if not flag:
            F[i][0] = i
        else:
            F[i][0] = -1

    for j in range(1,n-1):
        for i in range(n):
            if L[i][j] == "#":
                F[i][j] = -1
            else:
                curr = max(F[i-1][j],F[i][j-1])
                if curr == -1:
                    F[i][j] = max(F[i][j],-1)
                else:
                    F[i][j] = max(F[i][j],curr + 1)

        curr_k = F[n-1][j-1]
        for i in range(n-1,-1,-1):
            if L[i][j] == '#':
                F[i][j] = -1
                curr_k = -1
            else:
                curr = max(curr_k,F[i][j-1])
                if curr == -1:
                    F[i][j] = max(F[i][j],-1)
                    curr_k = -1
                else:
                    F[i][j] = max(F[i][j],curr + 1)
                    curr_k = curr + 1
                    
    for i in range(n):
        if L[i][n-1] == "#":
            F[i][n-1] = -1
        else:
            curr = max(F[i-1][n-1],F[i][n-1-1])
            if curr == -1:
                F[i][n-1] = -1
            else:
                F[i][n-1] = curr + 1


    # for i in range(n+1):
    #     print(F[i])
    return F[n-1][n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )


# def maze(L):
#     max_path = 0
#     n = len(L)
#     visited = [[False for _ in range(n)] for _ in range(n)]
#     def rek(A,i,j,length):
#         if i == n-1 and j == n-1:
#             nonlocal max_path
#             if length > max_path:
#                 max_path = length
#             return
        
#         visited[i][j] = True

#         if i+1<n and not visited[i+1][j] and A[i+1][j] != '#':
#             rek(A,i+1,j,length+1)
#         if j+1<n and not visited[i][j+1] and A[i][j+1] != "#":
#             rek(A,i,j+1,length+1)
#         if i-1>=0 and not visited[i-1][j] and A[i-1][j] != '#':
#             rek(A,i-1,j,length+1)

#         visited[i][j] = False

#         return

#     rek(L,0,0,0)
#     return max_path