import random

def mergeSort(A,index,x):
    n = len(A)
    if n > 1:
        mid = n//2

        L = A[:mid]
        R = A[mid:]

        mergeSort(L,index,x)
        mergeSort(R,index,x)

        i = j = k = 0

        if x == 0:
            while i < len(L) and j < len(R):
                if L[i][index] <= R[j][index]:
                    A[k] = L[i]
                    i += 1
                else:
                    A[k] = R[j]
                    j += 1
                k += 1
        elif x == 1:
            while i < len(L) and j < len(R):
                if L[i][index] >= R[j][index]:
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
        
def counting_sort_pretty(A,index,x):
    n = len(A)
    C = [0 for _ in range(10)]
    B = [0 for _ in range(n)]

    for i in range(n):
        C[A[i][index]] += 1

    if x == 0:
        for i in range(1,10):
            C[i] = C[i] + C[i-1]
    elif x == 1:
        for i in range(8,-1,-1):
            C[i] = C[i] + C[i+1]

    for i in range(n-1,-1,-1):
        B[C[A[i][index]]-1] = A[i]
        C[A[i][index]] -= 1

    for i in range(n):
        A[i] = B[i]

def pretty_sort(A):
    n = len(A)

    arr = []

    for i in range(n):
        num = A[i]
        digits = [0 for _ in range(10)]
        while num > 0:
            digits[num%10] += 1
            num //= 10
        
        one_digit = 0
        many_digits = 0
        for j in range(10):
            if digits[j] == 1:
                one_digit += 1
            elif digits[j] > 1:
                many_digits += 1
        
        arr.append((A[i],one_digit,many_digits))

    # mergeSort(arr,2,0)
    # mergeSort(arr,1,1)
    counting_sort_pretty(arr,2,0)
    counting_sort_pretty(arr,1,1)


    for i in range(n):
        A[i] = arr[i][0]

# T = [123,445,28,22,4456]
# T = [random.randint(10,10000) for _ in range(15)]
# print(T)
# pretty_sort(T)
# print(T)

def mergeSort_chaos(A):
    n = len(A)
    if n > 1:
        mid = n//2

        L = A[:mid]
        R = A[mid:]

        mergeSort_chaos(L)
        mergeSort_chaos(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][0] <= R[j][0]:
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
         

def chaos_index(A):
    n = len(A)

    arr = []

    for i in range(n):
        arr.append((A[i],i))

    print(arr)
    mergeSort_chaos(arr)
    print(arr)

    max_k = 0

    for i in range(n):
        curr_k = abs(arr[i][1] - i)
        if curr_k > max_k:
            max_k = curr_k

    return max_k

# T = [0,2,1.1,2]
# T = [random.randint(1,100) for _ in range(15)]
# print(chaos_index(T))

def partition(A,l,r):
    x = A[r]
    i = l - 1
    for j in range(l,r):
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i + 1

def find_position(A,l,r,k):
    index = partition(A,l,r)

    if index == k:
        return A[index]
        
    if index > k:
        return find_position(A,l,index-1,k)
        
    return find_position(A,index+1,r,k)

def section(A,p,q):
    n = len(A)
    find_position(A,0,n-1,p)
    find_position(A,p,n-1,q)
    return A[p:q+1]

# T = [random.randint(145,205) for _ in range(50)]
# print(section(T,2,7))

# T = [25,14,17,18,31,10,9,14,26]
# print(find_position(T,0,len(T)-1,len(T)//2))

def insertion_sort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
            
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


# T = [0.79,0.13,0.16,0.64,0.39,0.20,0.89,0.53,0.71,0.42]
# print(T)
# bucket_sort(T)
# print(T)

#================================================================

# def magic_fives(A,k):
#     n = len(A)
#     n_5 = n//5
#     B = [A[i:i+5] for i in range(0,n,5)]

#     print(B)

#     for i in range(len(B)):
#         insertion_sort(B[i])

#     print(B)
        
#     medians = []
#     for i in range(len(B)):
#         medians.append(B[i][len(B[i])//2])

#     if len(medians) <= 5:
#         insertion_sort(medians)
#         pivot = medians[len(medians)//2]
#     else:
#         pivot = magic_fives(medians,len(medians)/2)

#     low = [j for j in A if j < pivot]
#     high = [j for j in A if j > pivot]

#     i = len(low)
#     if i < k:
#         return magic_fives(low,i)
#     elif i > k:
#         return magic_fives(high,i-k-1)
#     else:
#         return pivot

# def magic_fives(A,k):
#     n = len(A)
#     if n <= 10:
#         insertion_sort(A)
#         return A[k]
#     else:
#         B = [A[i:i+5] for i in range(0,n,5)]

#         for i in range(len(B)):
#             insertion_sort(B[i])
        
#         medians = []
#         for i in range(len(B)):
#             medians.append(B[i][len(B[i])//2])
        
#         pivot = magic_fives(medians,len(medians)//2)

#         low = [i for i in A if i < pivot]
#         equal = [i for i in A if i == pivot]
#         high = [i for i in A if i > pivot]

#         if len(low) <= k:
#             return magic_fives(low,k)
#         elif len(low) + len(equal) <= k:
#             return pivot
#         else:
#             return magic_fives(high,k-len(low)-len(equal))

# T = [10,4,11,5,6,2,9,16,13,21,24,18,20,7,8,31,29]
# # T = [2,4,1,5,7,10,3]
# print(T)
# print(magic_fives(T,0))

#=====================================================================

#ZAD5 Masz daną tablicę zawierającą n (n >= 11) liczb naturalnych w zakresie [0,k].
#Zamieniono 10 liczb z tej tablicy na losowe liczby spoza tego zakresu (np. dużo większe lub ujemne).
#Napisz algorytm, który posortuje tablicę w czasie O(n)

def insertion_sort_zad5(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

def counting_sort_zad5(A,k):
    n = len(A)
    C = [0 for _ in range(k+1)]
    B = [0 for _ in range(n)]

    for i in range(n):
        C[A[i]] += 1

    for i in range(1,k+1):
        C[i] = C[i] + C[i-1]

    for i in range(n-1,-1,-1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

    for i in range(n):
        A[i] = B[i]
     

def zad5(A,k):
    n = len(A)

    B = []
    C = []

    for i in range(n):
        if A[i] >= 0 and A[i] <= k:
            B.append(A[i])
        else:
            C.append(A[i])
    
    counting_sort_zad5(B,k)
    insertion_sort_zad5(C)

    x = 0
    while C[x] < 0:
        x += 1

    D = C[:x] + B + C[x:]
    
    for i in range(n):
        A[i] = D[i]


# k = 20
# T = [random.randint(0,20) for _ in range(30)]
# T += [-25,101,-4,88,-99,-42,44,91,74,61]
# print(T)
# zad5(T,k)
# print(T)

#ZAD7 Dana jest tablica zawierająca n liczb z zakresu [0,n^2-1]. 
#Napisz algorytm, który posortuje taką tablicę w czasie O(n).

#sorujemy najpierw przez %n potem przez %n^2. Dla większego zakresu analogicznie

def counting_sort_zad7_A(A):
    n = len(A)
    C = [0 for _ in range(n)]
    B = [0 for _ in range(n)]

    for i in range(n):
        index = A[i]%n
        C[index] += 1
    
    for i in range(1,n):
        C[i] = C[i] + C[i-1]

    for i in range(n-1,-1,-1):
        B[C[A[i]%n]-1] = A[i]
        C[A[i]%n] -= 1
    
    for i in range(n):
        A[i] = B[i]

def counting_sort_zad7_B(A):
    n = len(A)
    C = [0 for _ in range(n)]
    B = [0 for _ in range(n)]

    for i in range(n):
        index = A[i]//n
        C[index] += 1
    
    for i in range(1,n):
        C[i] = C[i] + C[i-1]

    for i in range(n-1,-1,-1):
        index = A[i]//n
        B[C[index]-1] = A[i]
        C[index] -= 1
    
    for i in range(n):
        A[i] = B[i]
    
def zad7(A):
    counting_sort_zad7_A(A) #A[i]%n
    counting_sort_zad7_B(A) #A[i]//n


# zad7_n = 100
# T = [random.randint(0,zad7_n**2-1) for _ in range(zad7_n)]
# print(T)
# zad7(T)
# print(T)

#ZAD7B n liczb z zakresu [0,n^3-1]

def counting_sort_zad7b(A,curr_n):
    n = len(A)
    C = [0 for _ in range(n)]
    B = [0 for _ in range(n)]

    for i in range(n):
        index = (A[i]//n**curr_n)%n
        C[index] += 1
    
    for i in range(1,n):
        C[i] += C[i-1]

    for i in range(n-1,-1,-1):
        index = (A[i]//n**curr_n)%n
        B[C[index]-1] = A[i]
        C[index] -= 1
    
    for i in range(n):
        A[i] = B[i]

def zad7b(A):
    counting_sort_zad7b(A,0)
    counting_sort_zad7b(A,1)
    counting_sort_zad7b(A,2)

# zad7b_n = 100
# T = [random.randint(0,zad7b_n**3-1) for _ in range(zad7b_n)]
# print(T)
# zad7b(T)
# print(T)

#ZAD4 Zaproponuj klasę reprezentującą strukturę danych, która w konstruktorze dostaje tablicę liczb
#naturalnych długości n o zakresie [0,k]. Ma ona posiadać metodę count_num_in_range(a,b) -
#ma ona zwracać informację o tym, ile liczb w zakresie [a,b] było w tablicy, ma działać w czasie O(n).

class counter:
    def __init__(self,T,k):
        self.k = k
        self.T = T
        self.C = [0 for _ in range(k+1)]

        n = len(T)

        for i in range(n):
            self.C[T[i]] += 1
        
        for i in range(1,k+1):
            self.C[i] += self.C[i-1]

    def count_num_in_range(self,a,b):
        if a > 0 and b <= self.k:
            return self.C[b] - self.C[a-1]
        
# T = counter([0,1,2,3,4,5,6,7,8,9,10,4,5,4,5,6],10)
# print(T.count_num_in_range(3,6))


#Dany jest ciąg przediałów domkniętych [a1,b1], ... ,[an,bn]. Proszę zaproponować algorytm, który
#znajduje taki przedział [at,bt], w którym w całości zawiera się jak najwięcej przedziałów.

def partition_interval(A,l,r,index):
    x = A[r][index]
    i = l - 1
    for j in range(l,r):
        if A[j][index] <= x:
            A[i+1],A[j] = A[j],A[i+1]
            i += 1
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def quick_sort_interval(A,l,r,index):
    while l < r:
        pivot = partition_interval(A,l,r,index)
        if pivot - l < r - pivot:
            quick_sort_interval(A,l,pivot-1,index)
            l = pivot + 1
        else:
            quick_sort_interval(A,pivot+1,r,index)
            r = pivot - 1

def the_most_intervals(T):
    n = len(T)
    quick_sort_interval(T,0,n-1,0)
    for i in range(n):
        T[i] = (T[i][0],T[i][1],i)
    
    quick_sort_interval(T,0,n-1,1)
    for i in range(n):
        T[i] = (T[i][0],T[i][1],T[i][2],i)

    max_interval = max_index = 0
    for i in range(n):
        if T[i][3] - T[i][2] > max_interval:
            max_interval = T[i][3] - T[i][2]
            max_index = i
    
    print(T)
    return (T[max_index][0],T[max_index][1])

# T = [(4,8),(5,9),(1,2),(1,3),(2,8),(3,7),(4,6),(8,9),(6,10),(6,11),(9,14),(11,16),(3,4)]
# print(T)
# print(the_most_intervals(T))


#Dana jest klasa:
#class Node:
#   val = 0
#   next = None
#rerprezentująca węzeł jednokierunkowego łańcucha odsyłaczowego, w którym wartości val
#poszczególnych węzłów zostały wygenerowane zgodnie z rozkładem jednostajnym na przedziale [a,b].
#Napisz procedurę sort(list), która sortuje taką listę. Funkcja powinna być jak najszybsza

class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = None

def create_link_list_from_array(A):
    head = Node(A[0])
    p = head
    for i in range(1,len(A)):
        p.next = Node(A[i])
        p = p.next
    return head

def print_link_list(L):
    while L is not None:
        print(f"{L.val}",end=" -> ")
        L = L.next   
    print()

def length_of_link_list(L):
    length = 0
    while L is not None:
        length += 1
        L = L.next
    return length

def remap_link_list_1(L,a,b):
    while L is not None:
        L.val = (L.val,L.val-a)
        L.val = (L.val[0],L.val[1]/(b-a))
        L = L.next
    
def remap_link_list_2(L):
    while L is not None:
        L.val = L.val[0]
        L = L.next

def insertion_sort_link_list(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j].val[1] > key.val[1]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

def bucket_sort_link_list(L,n):
    B = [[] for _ in range(n+1)]

    while L is not None:
        curr = L
        L = L.next
        index = int(n*curr.val[1])
        curr.next = None
        B[index].append(curr)

    for i in range(n+1):
        insertion_sort_link_list(B[i])
    
    head = Node(None)
    curr = head
    for i in range(n+1):
        for j in range(len(B[i])):
            curr.next = B[i][j]
            curr = curr.next
    
    return head.next

def sort_link_list(L,a,b):
    n = length_of_link_list(L)
    remap_link_list_1(L,a,b)
    L = bucket_sort_link_list(L,n)
    remap_link_list_2(L)
    return L

# a = 6
# b = 28
# T = [random.randint(a,b) for _ in range(10)]
# L = create_link_list_from_array(T)
# print_link_list(L)
# L = sort_link_list(L,a,b)
# print_link_list(L)


#Dana jest dwuwymiarowa tablica T o rozmiarach N × N wypełniona liczbami naturalnymi (liczby
#są parami różne). Proszę zaimplementować funkcję Median(T), która przekształca tablicę T , tak
#aby elementy leżące pod główną przekątną nie były większe od elementów na głównej przekątnej,
#a elementy leżące nad główną przekątną nie były mniejsze od elementów na głównej przekątnej.
#Algorytm powinien być jak najszybszy oraz używać jak najmniej pamięci ponad tę, która potrzebna
#jest na przechowywanie danych wejściowych (choć algorytm nie musi działać w miejscu). Proszę
#podać złożoność czasową i pamięciową zaproponowanego algorytmu.

#Przykład. Dla tablicy:
#T = [ [ 2, 3, 5],
#[ 7,11,13],
#[17,19,23] ]
#wynikiem jest, między innymi tablica:
#T = [ [13,19,23],
#[ 3, 7,17],
#[ 5, 2,11] ]

def print_array(A):
    n = len(A)
    for i in range(n):
        print(A[i])

def merge_sort_median(A):
    n = len(A)
    if n > 1:
        mid = n//2

        L = A[:mid]
        R = A[mid:]

        merge_sort_median(L)
        merge_sort_median(R)

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

def median(A):
    n = len(A)
    B = []
    for i in range(n):
        B.extend(A[i])

    merge_sort_median(B)

    bottom = []
    middle = []
    top = []

    j = 0
    while j < (len(B)-n)//2:
        bottom.append(B[j])
        j += 1
    
    for i in range(n):
        middle.append(B[j])
        j += 1

    while j < len(B):
        top.append(B[j])
        j += 1

    i = j = k = 0

    for x in range(n):
        for y in range(n):
            if x == y:
                A[x][y] = middle[j]
                j += 1
            elif x < y:
                A[x][y] = top[i]
                i += 1
            else:
                A[x][y] = bottom[k]
                k += 1


# T = [ [ 2, 3, 5],
# [ 7,11,13],
# [17,19,23] ]

# T = [[25,14,9,17],
# [21,15,2,5],
# [4,7,1,10],
# [18,20,11,6],
# ]
# print_array(T)
# median(T)
# print_array(T)