''' Fibbonacci Series '''

def fibo(n):
    f0 = 0       # initial 0
    f0 = 0       # initial 1
    f1 = 1
    print(f0,f1, end=" ")   # print first 2 digits
    for i in range(3,n+1):
        ans = f0 + f1       
        print(ans, end=" ")
        f0 = f1
        f1 = ans

num = int(input("Enter the number : "))
fibo(num)