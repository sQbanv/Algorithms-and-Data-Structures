from kolutesty import runtests

def mergeSort(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2

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
        


def ice_cream( T ):
    # tu prosze wpisac wlasna implementacje
    mergeSort(T)

    result = 0
    minutes = 0
    for i in range(len(T)):
        if T[i] - minutes <= 0:
            break
        result += T[i] - minutes
        minutes += 1

    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = True )

# T = [5, 1, 3, 7, 8]
# ice_cream(T)
