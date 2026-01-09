''' Multiplication table of any number '''
n = int(input("Enter the number you want : "))

for i in range (1,11):
    print(f"{n} x {i} = {n*i}")