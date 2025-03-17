import random

#HEAPSORT O(n*logn)
def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def parent(i):
    return (i-1)//2

def heapify(A,i,n):
    l = left(i)
    r = right(i)
    max_ind = i
    
    if l < n and A[l] > A[max_ind]:
        max_ind = l
    if r < n and A[r] > A[max_ind]:
        max_ind = r
    
    if max_ind != i:
        A[i],A[max_ind] = A[max_ind],A[i]
        heapify(A,max_ind,n)

def buildheap(A):
    n = len(A)
    for i in range(parent(n-1),-1,-1):
        heapify(A,i,n)

def HeapSort(A):
    n = len(A)
    buildheap(A)
    for i in range(n-1,0,-1):
        A[0],A[i] = A[i],A[0]
        heapify(A,0,i)

# tab2 = [random.randint(1,1000) for _ in range(15)]
# print(tab2)
# HeapSort(tab2)
# print(tab2)

#MERGESORT O(n*logn)
def MergeSort(arr):
    n = len(arr)
    if n > 1:
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

# tab = [random.randint(1,1000) for _ in range(15)]
# print(tab)
# MergeSort(tab)
# print(tab)

#QuickSort O(n*logn)
def partition(arr,l,r):
    x = arr[r]
    i = l - 1
    for j in range(l,r):
        if arr[j] <= x:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[r] = arr[r],arr[i+1]
    return i+1

def randomized_partition(arr,l,r):
    i = random.randint(l,r)
    arr[i],arr[r] = arr[r],arr[i]
    return partition(arr,l,r)

def quickSort(arr,l,r):
    if l < r:
        pivot = partition(arr,l,r)
        quickSort(arr,l,pivot-1)
        quickSort(arr,pivot+1,r)

def quickSort2(arr,l,r):
    while l<r:
        pivot = partition(arr,l,r)
        if pivot - l < r - pivot:
            quickSort2(arr,l,pivot-1)
            l = pivot + 1
        else:
            quickSort2(arr,pivot+1,r)
            r = pivot - 1

# tab = [random.randint(1,1000) for _ in range(15)]
# print(tab)
# quickSort(tab,0,len(tab)-1)
# print(tab)

def create_random_string_of_given_length(d):
    str = ''
    for i in range(d):
        str += chr(random.randint(97,122))
    return str

tab = [create_random_string_of_given_length(random.randint(2,7)) for _ in range(25)]
print(tab)
quickSort(tab,0,len(tab)-1)
print(tab)