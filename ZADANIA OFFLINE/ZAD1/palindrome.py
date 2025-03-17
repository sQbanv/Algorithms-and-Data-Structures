def isPalindrome(s):
    if s == s[::-1]:
        return True
    return False

def isPalindrome2(s):
    n = len(s)
    i = 0
    j = n-1
    while i!=j and s[i] == s[j]:
        i += 1
        j -= 1
    if i==j:
        return True
    else:
        return False

def findPalindromeLength(s):
    n = len(s)

    if n%2==1:
        curr_n = len(s)
    else:
        curr_n = len(s) - 1
    
    while curr_n!=1:
        i = 0
        j = curr_n-1

        while j < n:
            curr_i = i
            curr_j = j

            while curr_i != curr_j and s[curr_i] == s[curr_j]:
                curr_i += 1
                curr_j -= 1

            if curr_i == curr_j:
                return curr_n
            else:
                i += 1
                j += 1
                
        curr_n -= 2

    return curr_n

def findPalindromeLength2(s):
    n = len(s)
    
    length = 3
    max_length = 0

    i = 0
    j = length - 1

    while j < n:
        curr_i = i
        curr_j = j
        curr_length = length

        while curr_i != curr_j and s[curr_i] == s[curr_j]:
            curr_i += 1
            curr_j -= 1
            
        if curr_i == curr_j:
            curr_i = i - 1
            curr_j = j + 1
            while curr_i >= 0 and curr_j < n and s[curr_i] == s[curr_j]:
                curr_length += 2
                curr_i -= 1
                curr_j += 1
            if curr_length > max_length:
                max_length = curr_length
        
        i += 1
        j += 1

    return max_length

def findPalindromeLength3(s):
    n = len(s)
    mid = n//2

    curr_length = 3
    max_length = 0

    i = mid - 1
    j = mid + 1

    if s[i] == s[j]:
        i -= 1
        j += 1

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
        print(possible_max_length,max_length,curr_i_right+1)

        if possible_max_length <= max_length:
            return max_length

        curr_length = 1

        if s[curr_i_left] == s[curr_j_left]:
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

        if s[curr_i_right] == s[curr_j_right]:
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

    if n%2==0:
        curr_length = 0
        if s[0] == s[2]:
            curr_length = 3
        if curr_length > max_length:
            max_length = curr_length

    return max_length

pal = "abcdefgfedcba"
pal2 = "akontnoknonabcddcba"
pal3 = "aaaaaaaaab"
# print(isPalindrome(pal))
# print(isPalindrome2(pal))
# print(findPalindromeLength2(pal3))
print(findPalindromeLength3(pal3))