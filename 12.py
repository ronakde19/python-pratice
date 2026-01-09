''' To check a number is positive, negative or zero '''

num = int(input("Enter a number : "))

if (num>0):
    print(f"The {num} is a positive integer (+ve)")
elif (num==0):
    print("The number is 0")
else:
    print(f"The {num} is a negative integer (-ve)")