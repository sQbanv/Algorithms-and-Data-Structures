from zad9testy import runtests

# def min_cost( O, C, T, L ):
#     # tu prosze wpisac wlasna implementacje
#     print(O)
#     print(C)
#     n = len(O)
#     for i in range(n):
#         O[i] = (O[i],i)
#     O = sorted(O)
#     new_C = [-1 for _ in range(n)]
#     for i in range(n):
#         new_C[i] = C[O[i][1]]
    # print(new_C)
    # prev = 0
    # curr = 0
    # max_value = -1
    # result = 0
    # for i in range(T,L,T):
    #     while curr < n and O[curr][0] < i:
    #         curr += 1
    #     # print(O[prev:curr])
    #     curr_value = min(new_C[prev:curr])
    #     max_value = max(max_value,curr_value)
    #     result += curr_value
    #     prev = curr

    # result -= max_value
    # return result
    
# def min_cost(O, C, T, L):
#     dp = [float('inf')] * (L + 1)
#     dp[0] = 0

#     for i in range(1, L + 1):
#         if i <= T:
#             for j in range(len(O)):
#                 if O[j] <= i:
#                     dp[i] = min(dp[i], C[j] + dp[i - O[j]])
#         else:
#             for j in range(len(O)):
#                 if O[j] <= i - T:
#                     dp[i] = min(dp[i], C[j] + dp[i - O[j] - T])

#     return dp[L]

# def min_cost(O, C, T, L):
#     parking_distances = sorted(zip(O, C))
#     current_pos = 0
#     total_cost = 0
#     max_distance = T

#     print(parking_distances)

#     for distance, cost in parking_distances:
#         if distance - current_pos <= max_distance:
#             max_distance = max(max_distance, 2 * T)
#         else:
#             total_cost += cost
#             current_pos = distance
#             max_distance = 2 * T

#     if current_pos < L:
#         total_cost += parking_distances[-1][1]

#     return total_cost

# def min_cost(O, C, T, L):
#     dp = [float('inf')] * (L + 1)
#     dp[0] = 0

#     for i in range(1, L + 1):
#         if i <= T:
#             for j in range(len(O)):
#                 if O[j] <= i:
#                     dp[i] = min(dp[i], C[j] + dp[i - O[j]])
#         else:
#             for j in range(len(O)):
#                 if O[j] <= i - T:
#                     dp[i] = min(dp[i], C[j] + dp[i - O[j] - T])

#         for k in range(i):
#             if dp[k] != float('inf'):
#                 for j in range(len(O)):
#                     if O[j] == i - k:
#                         dp[i] = min(dp[i], dp[k] + C[j])

#     return dp[L]

# def min_cost(O, C, T, L):
#     n = len(O)  # Liczba parkingów na trasie
#     dp = [float('inf')] * (n + 1)  # Tablica przechowująca koszt minimalny do dotarcia do danego parkingu
#     dp[0] = 0  # Koszt dojazdu do pierwszego parkingu (miasta A) wynosi 0

#     for i in range(1, n + 1):
#         max_dist = min(2 * T, O[i-1] - O[i-2] if i > 1 else O[i-1])  # Maksymalna odległość, którą można przejechać bez postoju na bieżącym parkingu

#         for j in range(i):
#             dist = O[i - 1] - O[j]  # Odległość między parkingami j i i
#             if dist <= max_dist:
#                 cost = dp[j] + C[i - 1]  # Koszt dotarcia do parkingu i z postoju na parkingu j
#                 dp[i] = min(dp[i], cost)

#     return dp[n]  # Zwracamy koszt minimalny dojazdu do ostatniego parkingu (miasta B)

# def minimalny_koszt_parkowania(trasa, oplata, T,L):
#     n = len(trasa)
#     koszt = [float('inf')] * n  # Inicjalizacja tablicy kosztów
#     koszt[0] = 0  # Koszt dla miasta A
    
#     for i in range(1, n):
#         for j in range(i-1, max(-1, i-2*T), -1):
#             aktualny_koszt = koszt[j] + oplata[i]
#             koszt[i] = min(koszt[i], aktualny_koszt)
    
#     return koszt[n-1]  # Zwracamy minimalny koszt dla miasta B

def min_cost(O, C, T, L):
    n = len(O)  # liczba parkingów na trasie
    min_costs = [float('inf')] * (n + 1)  # tablica minimalnych kosztów
    min_costs[0] = 0  # minimalny koszt dojazdu do pierwszego parkingu

    for i in range(1, n + 1):
        for j in range(i - 1, max(0, i - 2 * T) - 1, -1):
            cost = min_costs[j] + C[j]  # koszt dotarcia do pozycji j z minimalnym kosztem
            if O[i - 1] - O[j] <= T:  # sprawdzenie, czy można przejechać do parkingu i wykorzystać wyjątek
                cost = min(cost, min_costs[j] + C[j] + C[i - 1])  # koszt z uwzględnieniem zatrzymania się na parkingu i wyjątku
            min_costs[i] = min(min_costs[i], cost)  # aktualizacja minimalnego kosztu dla pozycji i

    return min_costs[n]  # minimalny koszt dotarcia do miasta B



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )

O = [17, 20, 11, 5, 12]
C = [9, 7, 7, 7, 3]
T = 7
L = 25
print(min_cost(O,C,T,L))