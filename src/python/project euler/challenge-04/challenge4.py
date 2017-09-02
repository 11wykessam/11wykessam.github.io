# challenge is to find the largest palindrome made from the product of two three digit numbers

def isPalindrome(n) :
    n = str(n)
    palindrome = True
    for i in range(int(len(n)/2)) :
        if n[i] != n[len(n) - 1 - i] :
            palindrome = False
    return palindrome



def findPalindromes(limit) :
    palindromes = []

    for i in range(limit, 0, -1) :
        if isPalindrome(i) :
            palindromes.append(i)

    return palindromes

answer = 0

for i in range(999, 100, -1) :
    for j in range(999, 100, -1) :
        n = i * j
        if isPalindrome(n) :
            if n > answer :
                answer = n

print(answer)