import random
#Time Complexity O(n^2)

def SelectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index],arr[i] = arr[i],arr[min_index]
    return arr

def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def InsertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j -= 1
    return arr
    
def InsertionSort2(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j > -1 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            # print(arr)
        arr[j+1] = key
        # print(arr)
    return arr

#Time Complexity O(nlog(n))

def MergeSort(arr):
    n = len(arr)
    if(n>1):
        mid = n//2
        L = arr[:mid]
        R = arr[mid:]

        MergeSort(L)
        MergeSort(R)

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
    return arr

def QuickSort(arr): #Always pick the first element as a pivot
    n = len(arr)
    if(n < 2):
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        more = [j for j in arr[1:] if j >= pivot]
        return QuickSort(less) + [pivot] + QuickSort(more)



tab = [random.randint(1,1000) for _ in range(15)]
print(tab)
# print(SelectionSort(tab))
# print(BubbleSort(tab))
# print(InsertionSort(tab))
# print(InsertionSort2(tab))
# print(MergeSort(tab))
print(QuickSort(tab))