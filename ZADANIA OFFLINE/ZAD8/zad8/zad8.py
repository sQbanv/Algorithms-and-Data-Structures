#Dariusz Cebula
#Algorytm na początku tworzy tablice jednowymiarową w której zapisuje gdzie są plamy oleju i ile jest w nich oleju.
#Robi to rekurencyjnie dla plam które są w zasięgu pierwszego wiersza.
#Następnie za pomocą algorytmu zachłannego oblicza minimalną ilość zatankowania, aby dotrzeć do ostatniego indeksu listy.
#Zawsze pobieramy olej z pierwszego pola, potem idziemy po kolejnych indeksach zapisując do kolejki priorytetowej napotkane plamy oleju.
#kiedy wejdziemy na pole mając 0 paliwa to bierzemy największe pole oleju, które jest w kolejce priorytetowej. I robimy to aż do końca listy.
#Takie zachłanne rozwiązanie daje poprwane odpowiedzi w optymalnym czasie
#Szacowana złożoność algorytmu O(nlogn)

from zad8testy import runtests

from queue import PriorityQueue

def plan(T):
    # tu prosze wpisac wlasna implementacje
    n = len(T[0])
    F = [0 for _ in range(n)]

    amount = 0

    def oil(arr,i,j):
        if i >= len(arr) or i < 0 or j >= len(arr[0]) or j < 0 or arr[i][j] == 0:
            return
        nonlocal amount 
        amount += arr[i][j]
        arr[i][j] = 0

        oil(arr,i-1,j)
        oil(arr,i,j-1)
        oil(arr,i,j+1)
        oil(arr,i+1,j)

    for j in range(n):
        if T[0][j] != 0:
            oil(T,0,j)
            F[j] = amount
            amount = 0

    # min_step = float('inf')
    # def rek(arr,i,fuel,step):
    #     # print(i,fuel,step)
    #     if fuel < 0 or i >= len(arr):
    #         return
        
    #     if i == len(arr) - 1:
    #         nonlocal min_step
    #         min_step = min(step,min_step)
    #         return
        
    #     for j in range(1,fuel+arr[i]+1):
    #         rek(arr,i+j,fuel+arr[i]-j,step + 1)

    # rek(F,0,0,0)

    # def steps(A):
    #     count = 0
    #     for i in range(len(A)):
    #         count += A[i]
    #     F = [[float('inf')] * (count+1) for _ in range(len(A))]
    #     F[0][A[0]] = 0
    #     for i in range(len(A)):
    #         for j in range(count):
    #             if F[i][j] != float('inf'):
    #                 k = i + 1
    #                 while k < len(A) and j >= k - i:
    #                     index = i + j + A[k] - k
    #                     F[k][index] = min(F[k][index],F[i][j]+1)
    #                     k += 1
    #     return min(F[-1])

    PQ = PriorityQueue()
    fuel = 0
    counter = 0

    for i in range(n):
        if F[i] != 0:
            PQ.put(-1*F[i])
        if fuel == 0 and i < n - 1:
            max_energy = -1*PQ.get()
            fuel += max_energy
            counter += 1
        fuel -= 1

    # print(F)
    return counter


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )
