from zad3testy import runtests

def insertion_sort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

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

def bucket_sort(A):
    n = len(A)
    B = [[] for _ in range(n)]

    for i in range(n):
        B[int(A[i])].append(A[i])
    
    for i in range(n):
        insertion_sort(B[i])
        # merge_sort(B[i])
    
    k = 0
    for i in range(n):
        for j in range(len(B[i])):
            A[k] = B[i][j]
            k += 1

def SortTab(T,P):

    bucket_sort(T)

    return T

runtests( SortTab )