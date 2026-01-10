''' Check a number is even or odd using function '''

def checkoddev(n):
    if(n%2==0):
        return "even"
    else:
        return "odd"
    
num = int(input("Enter a Number : "))
print(checkoddev(num))