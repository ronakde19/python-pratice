''' Greet user Hello '''

def greet(name):      # throwing the value to the function
    gr = "Hello, How are you doing " + name   # string concatination
    return gr  # returning the function

name = input("Enter Your Name : ")
print( greet(name))