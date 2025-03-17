from egzP3atesty import runtests
from math import inf

class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None

def knapsack(W,P,B):
    n = len(W)
    F = [[0 for b in range(B+1)] for i in range(n)]
    for b in range(W[0],B+1):
        F[0][b] = P[0]
    for b in range(B+1):
        for i in range(1,n):
            F[i][b] = F[i-1][b]
            if b - W[i] >= 0:
                F[i][b] = max(F[i][b],F[i-1][b-W[i]] + P[i])
    return F[n-1][B]

def wybory(T):
    #tutaj proszę wpisać własną implementację
    sum = 0             
    for el in T:
      S = el.fundusze
      P = []
      W = []
      curr = el
      while curr != None:
        P.append(curr.wyborcy)
        W.append(curr.koszt)
        curr = curr.next
      sum += knapsack(W,P,S)
    return sum

runtests(wybory, all_tests = True)