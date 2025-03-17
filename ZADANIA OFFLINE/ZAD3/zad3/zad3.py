#Dariusz Cebula
#Algorytm na początku tworzy nową tablicę do której dodaje wszystkie słowa oraz ich odwrotność
#potem sortuje tą tablicę sortowaniem przez scalanie.
#na koniec przechodzimy po posortowanej tablicy i zliczamy słowa równoważne. Gdy natrafi na palindrom
#to dzieli wynik przez pół. Na koniec zwraca największą siłę w tej tablicy
#Szacunkowa złożoność O(n+nlogn)

from zad3testy import runtests

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
            if L[i] <= R[j]:
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
        
def strong_string(T):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    max_strength = 0

    new_T = []

    for i in range(n):
        new_T.append(T[i])
        new_T.append(T[i][::-1])
    
    mergeSort(new_T)

    curr_strength = 1
    for i in range(n*2-1):
        if new_T[i] == new_T[i+1]:
            curr_strength += 1
        else:
            if new_T[i] == new_T[i][::-1]:
                curr_strength = curr_strength//2
            if curr_strength > max_strength:
                max_strength = curr_strength
            curr_strength = 1
    
    return max_strength

# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )