#Dariusz Cebula
#Algorytm przechodzi w pętli przez wszytkie podtablice T[i:i+p] i wyszukuje w nich k-tego największego elementu
#za pomocą algorytmu quick select, który korzysta z partition z quick sorta i znajduje go w O(p) ,gdzie p to długośc tego przedziału
#Jeżeli aktualnie przeszukiwany przedział nie zmieni hierarchi liczb to nie musimy wywoływać auick_select tylko dodać do sumy poprzedni k-ty element
#(z poprzedniego przedziału usuniemy liczbę większą od k-tego elemetu i do aktualnego dodamy większą i to samo dla mniejszych). Na koniec zwraca sumę
#Szacunkowa złożoność O(np)

from kol1testy import runtests
        
def partition(A,l,r):
    x = A[r]
    i = l - 1
    for j in range(l,r):
        if A[j] > x:
            A[i+1],A[j] = A[j],A[i+1]
            i += 1
    A[i+1],A[r] = A[r],A[i+1]
    return i + 1

def quick_select(A,l,r,index):
    pivot = partition(A,l,r)

    if pivot == index:
        return A[pivot]

    if pivot < index:
        return quick_select(A,pivot+1,r,index)
    else:
        return quick_select(A,l,pivot-1,index)


def ksum(T, k, p):
    n = len(T)
    sum = 0
    for i in range(n-p+1):
        if i > 1 and T[i-1] > x and T[i+p-1] > x:
            sum += x
        elif i > i and T[i-1] < x and T[i+p-1] < x:
            sum += x
        else:
            curr = T[i:i+p]
            x = quick_select(curr,0,len(curr)-1,k-1)
            sum += x
    
    return sum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
