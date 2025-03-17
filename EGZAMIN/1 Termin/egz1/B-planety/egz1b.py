#Dariusz Cebula
#Algorytm dynamiczny, gdzie DP[i][b] - oznacza minimalny koszt dotarcia do i-tej planety mając b ton paliwa.
#Tworzymy tablicę DP - gdzie wiersze to planety, a kolumny to ilość paliwa w baku. Każda komórka na pocztku ma inf.
#Na początku dla planety A ustawiamy koszty początkowe dla każdej tony paliwa tyle ile kosztuje paliwo na tej planecie.
#Dodatkowo sprawdzamy czy jest dostępny teleport z planety A, jeśli tak to dla wartości w b=0 teleportujemy się + koszt.
#Następnie w pętli będziemy przechodzić po wszystkich planetach i wartościach paliwa.
#W każdej iteracji obliczmy dystans z poprzedniej planety i zapisujemy wartość (jeśli mniejsza od aktualnej) dotarcia tutaj z możliwych ilości paliwa z poprzedniej planety.
#Potem jeszcze zapisujemy koszt (jesli mniejszy niż aktualny) gdy tankujemy konkretną ilość paliwa na tej stacji
#Na koniec dla b = 0, sprawdzamy czy jest dostępna teleportacja i zapisujemy wartość w miejscu teleportacji (aktualna wartość + koszt)
#Zwracamy minimum z wartości w ostatnim wierszu
#Szacowana złożoność algorytmu O(n*E)

from egz1btesty import runtests

def planets( D, C, T, E ):
    # tu prosze wpisac wlasna implementacje
    n = len(D)
    DP = [[float('inf') for b in range(E+1)] for i in range(n)]
    
    for b in range(E+1):
        DP[0][b] = C[0] * b

    if T[0][0] != 0:
        DP[T[0][0]][0] = DP[0][0] + T[0][1]

    for i in range(1,n):
        for b in range(E+1):
            dist = D[i] - D[i-1]
            #podróż bez teleportu
            if b + dist <= E:
                DP[i][b] = min(DP[i][b],DP[i-1][b+dist])

            if b - 1 >= 0:
                DP[i][b] = min(DP[i][b],DP[i][b-1] + C[i])
            
            #teleport do planety
            if T[i] != i and b == 0:
                DP[T[i][0]][b] = min(DP[T[i][0]][b],DP[i][b] + T[i][1])

    return min(DP[n-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True)