''' Generate reverse of a number using function'''

def reverse(n):
    num = 0
    while (n!=0):
        ld = n%10
        num = num*10+ld
        n = n//10
    return num

digit = int(input("Enter the number you want to reverse : "))
print(reverse(digit))
