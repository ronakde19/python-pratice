''' Palindrome Number Checker '''

def palindrome(n):
    original = n
    rev = 0
    while (n!=0):
        ld = n%10
        rev = rev*10+ld
        n = n//10
    if (rev == original):
        return "Palindrome"
    else:
        return "Not a Palindrome"    
    
number = int(input("Enter a number you want to check : "))
print(palindrome(number))


