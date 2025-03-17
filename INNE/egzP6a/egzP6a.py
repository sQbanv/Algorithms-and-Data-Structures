from egzP6atesty import runtests 

def count_letters(s):
    n = len(s)
    counter = 0
    for i in range(n):
        if ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z'):
            counter += 1
    return counter

def merge_sort(A):
    n = len(A)
    if n > 1:
        mid = n//2

        L = A[:mid]
        R = A[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k =0

        while i < len(L) and j < len(R):
            if L[i][2] >= R[j][2]:
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

def partition(A,l,r):
    x = A[r]
    i = l - 1
    for j in range(l,r):
        if A[j][1] >= x[1]:
            A[j],A[i+1] = A[i+1],A[j]
            i += 1
    A[i+1],A[r] = A[r],A[i+1]
    return i + 1

def quick_select(A,l,r,index):    
    pivot = partition(A,l,r)

    if pivot == index:
        return A[pivot]

    if pivot > index:
        quick_select(A,l,pivot-1,index)
    else:
        quick_select(A,pivot+1,r,index)

def google ( H, s ):
    #tutaj proszę wpisać własną implementację
    #O(nk+nlogn)
    # n = len(H)
    # max_len = 0
    # for i in range(n):
    #     curr_n = len(H[i])
    #     H[i] = (H[i],curr_n,count_letters(H[i]))
    #     if curr_n > max_len:
    #         max_len = curr_n

    # B = [[] for _ in range(max_len+1)]
    # for i in range(n):
    #     B[H[i][1]].append(H[i])

    # for i in range(max_len+1):
    #     merge_sort(B[i])
    
    # k = 0
    # for i in range(max_len,-1,-1):
    #     for j in range(len(B[i])):
    #         H[k] = B[i][j]
    #         k += 1

    # result = str(H[s-1][0])
    # return result

    #O(nk)
    n = len(H)
    max_len = 0
    for i in range(n):
        curr_len = len(H[i])
        if curr_len > max_len:
            max_len = curr_len
    
    B = [[] for _ in range(max_len+1)]

    for i in range(n):
        B[len(H[i])].append(H[i])
    

    sum = 0
    goal_id = 0
    for i in range(max_len,-1,-1):
        sum += len(B[i])
        if s <= sum:
            goal_id = i
            break
    
    T = B[goal_id]
    for i in range(len(T)):
        letters = 0
        for letter in T[i]:
            if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
                letters += 1
        T[i] = (T[i],letters)

    start_index = 0
    end_index = len(T) - 1
    search_index = s - (sum - len(T)) - 1

    quick_select(T,start_index,end_index,search_index)

    return T[search_index][0]


runtests ( google, all_tests=True )