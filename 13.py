''' Find Largest of Three Numbers without max'''

n1 = int(input("Enter Number 1 : "))
n2 = int(input("Enter Number 2 : "))
n3 = int(input("Enter Number 3 : "))

if (n1>n2) & (n1>n3) :
    print(f"{n1} is the largest number")
elif (n2>n1) & (n2>n3) :
    print(f"{n2} is the largest number")
else:
    print(f"{n3} is the largest number")