import random
import math
#Insertionsort O(n^2)

def insertion_sort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

#Mergesort O(nlogn)

def merge_sort(A):
    n = len(A)
    if n > 1:
        mid = n//2

        L = A[:mid]
        R = A[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

#Quicksort O(nlogn)

def partition(A,l,r):
    x = A[r]
    i = l - 1
    for j in range(l,r):
        if A[j] <= x:
            A[i+1],A[j] = A[j],A[i+1]
            i += 1
    A[i+1],A[r] = A[r],A[i+1]
    return i + 1

def quick_sort(A,l,r):
    while l<r:
        pivot = partition(A,l,r)
        if pivot - l < r - pivot:
            quick_sort(A,l,pivot-1)
            l = pivot + 1
        else:
            quick_sort(A,pivot+1,r)
            r = pivot - 1

#Heapsort O(nlogn)
def parent(i): return (i-1)//2

def left(i): return 2*i + 1

def right(i): return 2*i + 2

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

def build_heap(A):
    n = len(A)
    for i in range(parent(n-1),-1,-1):
        heapify(A,i,n)

def heap_sort(A):
    n = len(A)
    build_heap(A)
    for i in range(n-1,0,-1):
        A[0],A[i] = A[i],A[0]
        heapify(A,0,i)

#Counting Sort O(n+k)
#zał: liczby z zakresu [0,k]

def counting_sort(A,k):
    n = len(A)
    C = [0 for _ in range(k)]
    B = [0 for _ in range(n)]

    for i in range(n):
        C[A[i]] += 1
    
    for i in range(1,k):
        C[i] += C[i-1]

    for i in range(n-1,-1,-1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
    
    for i in range(n):
        A[i] = B[i]

#Radix Sort O(nt)

def counting_sort_num(A,pos):
    n = len(A)
    C = [0 for _ in range(10)]
    B = [0 for _ in range(n)]

    for i in range(n):
        index = (A[i]//pos)%10
        C[index] += 1
    
    for i in range(1,10):
        C[i] += C[i-1]

    for i in range(n-1,-1,-1):
        index = (A[i]//pos)%10
        B[C[index]-1] = A[i]
        C[index] -= 1
    
    for i in range(n):
        A[i] = B[i]

def radix_sort(A):
    max_num = max(A)
    
    pos = 1
    while max_num // pos > 0:
        counting_sort_num(A,pos)
        pos *= 10

#Bucket Sort O(n)
#zał: liczby równomiernie rozłożone na przedziale [0,1)

def bucket_sort(A):
    n = len(A)
    B = [[] for _ in range(n)]

    for i in range(n):
        B[int(n*A[i])].append(A[i])
    
    for i in range(n):
        insertion_sort(B[i])

    k = 0
    for i in range(n):
        for j in range(len(B[i])):
            A[k] = B[i][j]
            k += 1
    
#Quick Select O(n)

def partition_quick_select(A,l,r):
    x = A[r]
    i = l - 1
    for j in range(l,r):
        if A[j] <= x:
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


T = [random.randint(0,1000) for _ in range(15)]
# T = [0.1,0.5,0.4,0.93,0.42,0.67,0.88,0.13,0.17,0.11]
print(T)
radix_sort(T)
print(T)