''' Sum of First N Natural Numbers using loops'''

n = int(input("Enter a number you want sum :"))
num = n
sum = 0

for i in range(0,num+1):
    sum = sum+i

print(f"The sum of {n} numbers is {sum}")


