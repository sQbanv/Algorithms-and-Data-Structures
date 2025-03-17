import random

def countingSort(arr,k):
    n = len(arr)
    C = [0 for _ in range(k)]
    B = [0 for _ in range(n)]

    for i in range(n):
        C[arr[i]] += 1
    
    for i in range(1,k):
        C[i] = C[i] + C[i-1]

    for i in range(n-1,-1,-1):
        B[C[arr[i]]-1] = arr[i]
        C[arr[i]] -= 1
    
    for i in range(n):
        arr[i] = B[i]

# A = [random.randint(0,1000) for _ in range(100)]
# print(A)
# countingSort(A,1000)
# print(A)

def create_random_string_of_given_length(d):
    str = ''
    for i in range(d):
        str += chr(random.randint(97,122))
    return str

def countingSort_letters(arr,d,base):
    n = len(arr)
    C = [0 for _ in range(26)]
    B = [0 for _ in range(n)]

    for i in range(n):
        index = ord(arr[i][d]) - ord('a')
        C[index] += 1

    for i in range(1,base):
        C[i] = C[i] + C[i-1]

    for i in range(n-1,-1,-1):
        index = ord(arr[i][d]) - ord('a')
        B[C[index]-1] = arr[i]
        C[index] -= 1
    
    for i in range(n):
        arr[i] = B[i]


def radixSort(arr,d):
    n = len(arr)
    for curr_d in range(d-1,-1,-1):
        countingSort_letters(arr,curr_d,26)
            


def counting_sort_letters(arr,pos,base):
    n = len(arr)
    C = [0 for _ in range(base)]
    B = [0 for _ in range(n)]

    for i in range(n):
        if len(arr[i])-1 < pos:
            index = 0
        else:
            index = ord(arr[i][pos])-ord('a')
        
        C[index] += 1
    
    for i in range(1,base):
        C[i] = C[i] + C[i-1]
    
    for i in range(n-1,-1,-1):
        if len(arr[i])-1 < pos:
            index = 0
        else:
            index = ord(arr[i][pos]) - ord('a')
        
        B[C[index]-1] = arr[i]
        C[index] -= 1
    
    for i in range(n):
        arr[i] = B[i]

def radixSort_words(arr):
    n = len(arr)
    max_length = 0
    for i in range(n):
        curr = len(arr[i])
        if curr > max_length:
            max_length = curr

    for letter in range(max_length-1,-1,-1):
        counting_sort_letters(arr,letter,26)

d = 10
B = [create_random_string_of_given_length(random.randint(2,5)) for _ in range(10)]
print(B)
radixSort_words(B)
print(B)

