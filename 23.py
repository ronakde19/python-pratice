''' Facctorial of a number using function '''

def fact(n):
    num = 1
    for i in range(1,n+1):
        num = num*i
    return num

n = int(input("Enter Your Number :"))
print(fact(n))
