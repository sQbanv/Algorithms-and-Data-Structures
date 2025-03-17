#Dariusz Cebula
#Algorytm zaczyna przeszukiwanie od środka i zapisuje długość potencjalnego palindromu.
#Potem zaczyna przechodzić w pętli zewnętrznej po dwóch słowach: jeden z prawej i jeden z lewej.
#Na początku każdej iteracji pętli zewnętrznej sprawdzamy czy przeszukiwane słowo może być 
#dłuższe od znalezionego już palindromu. Jeśli nie to mamy pewność, że naleźliśmy już
#najdłuższy palindrom i możemy go zwrócić
#Jeśli tak sprawdza jeden palindrom po prawej i jeden po lewej zaczynając od długośi 3
#i przechodzi pętlą wewnętrzną tak długo aż litery będą sobie równe i nie wyjdą poza zakres
#na końcu pętli zapisujemy jak jest dłuższy wynik.
#Każda iteracja pętli zewnętrznej przechodzi o jeden w lewo dla lewej strony i 
#o jeden w prawo dla prawej strony.
#Na koniec jak będzie potrzeba to dla słowa na wejściu o parzystej długości musimy jeszcze sprawdzić
#słowo długości 3 na początku, gdyż nie będzie uwzględnione w pętli
#Szacunkowa złożonośc algorytmu: O(n^2)

from zad1testy import runtests

def ceasar( s ):
    n = len(s)
    mid = n//2

    curr_length = 1
    max_length = 0

    i = mid - 1
    j = mid + 1

    if s[i] == s[j]: #sprawdzanie środkowego słowa
        i -= 1
        j += 1
        curr_length += 2

        while i >= 0 and j < n and s[i] == s[j]:
            curr_length += 2
            i -= 1
            j += 1

        max_length = curr_length
    
    i = mid - 1
    j = mid + 1

    i_left = i - 1
    j_left = j - 1 
    i_right = i + 1
    j_right = j + 1

    while i_left > 0 and j_right < n:
        curr_i_left = i_left
        curr_j_left = j_left
        curr_i_right = i_right
        curr_j_right = j_right

        possible_max_length = ((n-(curr_i_right+1))*2)+1

        if possible_max_length <= max_length:
            return max_length

        curr_length = 1

        if s[curr_i_left] == s[curr_j_left]: #sprawdzanie lewego słowa
            curr_i_left -= 1
            curr_j_left += 1
            curr_length += 2

            while curr_i_left >= 0 and curr_j_left < n and s[curr_i_left] == s[curr_j_left]:
                curr_length += 2
                curr_i_left -= 1
                curr_j_left += 1

            if curr_length > max_length:
                max_length = curr_length
        
        curr_length = 1

        if s[curr_i_right] == s[curr_j_right]: # sprawdzanie prawego słowa
            curr_i_right -= 1
            curr_j_right += 1
            curr_length += 2

            while curr_i_right >= 0 and curr_j_right < n and s[curr_i_right] == s[curr_j_right]:
                curr_length += 2
                curr_i_right -= 1
                curr_j_right += 1

            if curr_length > max_length:
                max_length = curr_length

        i_left -= 1
        j_left -= 1
        i_right += 1
        j_right += 1

    if n%2==0: #dla słowa o parzystej dlugości na końcu musimy sprawdzić słowo długości 3 na początku
        curr_length = 0
        if s[0] == s[2]:
            curr_length = 3
        if curr_length > max_length:
            max_length = curr_length

    return max_length

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
