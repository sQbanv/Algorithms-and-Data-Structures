#Dariusz Cebula
#Algorytm na początku sortuje tablice za pomocą sortowania przez scalanie w porządku malejącym
#następnie w pętli przechodzi po elementach dodatkowo odejmując liczbę dni i sumuje to wyniku
#jak trafi na element który po odjęciu ma 0 lub mniej to przerywa pętle i zwraca wynik
#Szacowana złożoność algorytmu to O(nlogn)

from zad2testy import runtests

def mergeSort(arr):
    n = len(arr)
    if n > 1:
        mid = n//2

        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def snow( S ):
    # tu prosze wpisac wlasna implementacje
    n = len(S)
    day = 0
    result = 0

    mergeSort(S)

    for i in range(n):
        if S[i] - day > 0:
            result += S[i] - day
        else:
            break
        day += 1

    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
