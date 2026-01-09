''' Sum of First N Natural Numbers using loops'''

n = int(input("Enter a number you want sum :"))
num = n
sum = 0
while(num!=0):
    sum = sum+num
    num-=1

print(f"The sum of {n} numbers is {sum}")
