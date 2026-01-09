''' Reverse of a number '''

num = int(input("Enter a number : "))
n = num
rev = 0
ld =0

while (num!=0):
    ld = num%10
    rev = rev*10+ld
    num = num//10

print(f"The reverse of {n} is {rev}")
    
