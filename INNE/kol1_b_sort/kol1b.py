from kol1btesty import runtests

def merge_sort_by_length(A):
    n = len(A)
    if n > 1:
        mid = n//2

        L = A[:mid]
        R = A[mid:]

        merge_sort_by_length(L)
        merge_sort_by_length(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if len(L[i]) <= len(R[j]):
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

def str_to_arr(s):
    n = len(s)
    arr = []
    for i in range(n):
        arr.append(s[i])
    return arr

def arr_to_str(arr):
    n = len(arr)
    s = ''
    for i in range(n):
        s += arr[i]
    return s

def merge_sort_string(A):
    n = len(A)
    if n > 1:
        mid = n//2

        L = A[:mid]
        R = A[mid:]

        merge_sort_string(L)
        merge_sort_string(R)

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

    return A

def counting_sort_string(A):
    n = len(A)
    C = [0 for _ in range(26)]
    B = [0 for _ in range(n)]

    for i in range(n):
        index = ord(A[i]) - ord('a')
        C[index] += 1

    for i in range(1,26):
        C[i] += C[i-1]

    for i in range(n-1,-1,-1):
        index = ord(A[i]) - ord('a')
        B[C[index]-1] = A[i]
        C[index] -= 1
    
    for i in range(n):
        A[i] = B[i]
    
    return A

# def f(T):
#     # tu prosze wpisac wlasna implementacje
#     n = len(T)
#     for i in range(n):
#         curr = str_to_arr(T[i])
#         curr = counting_sort_string(curr)
#         curr = arr_to_str(curr)
#         T[i] = curr

#     # print(T)
#     merge_sort_by_length(T)
#     # print(T)

#     max_anagram = 0
#     curr_anagram = 1
#     for i in range(n-1):
#         if T[i] == T[i+1]:
#             curr_anagram += 1
#         else:
#             if curr_anagram > max_anagram:
#                 max_anagram = curr_anagram
#             curr_anagram = 1

#     if curr_anagram > max_anagram:
#         max_anagram = curr_anagram

#     return max_anagram


def count_letters_in_word(word):
    result = [0]*26
    for character in word:
        result[ord(character) - 97] +=1
    return result

def find_max(A):
    n = len(A)
    max_val = 0
    for i in range(26):
        for j in range(n):
            if(A[j][i] > max_val):
                max_val = A[j][i]
    return max_val 
    
def counting_sort(A, i, k):
    n = len(A)
    C = [0]*(k+1)
    B = [0]*n

    for j in range(n):
        C[(A[j][i])] = C[(A[j][i])]+1

    for j in range(1,k):
        C[j] += C[j-1]
    
    for j in range(n-1, -1, -1):
        B[C[A[j][i]]-1] = A[j]
        C[A[j][i]]-=1
    for j in range(n):
        A[j] = B[j]

def f(T):
    to_sort_array = [count_letters_in_word(word) for word in T]
    max_k = find_max(to_sort_array)
    for i in range(26-1,-1,-1):
        counting_sort(to_sort_array,i,max_k+1)

    max_len = 1
    curr_len = 1
    for i in range(1, len(to_sort_array)):
        if(to_sort_array[i] == to_sort_array[i-1]):
            curr_len += 1
        else:
            if(curr_len>max_len):
                max_len = curr_len
            curr_len = 1
    return max(max_len,curr_len)

# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )

