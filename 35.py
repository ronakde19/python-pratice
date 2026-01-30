# __init.__constructor

class Student :
    def __init__(self,name,age):
        self.name = name   # instance variable
        self.age = age

s1 = Student("Ronak",20)
s2 = Student("Amit",21)

print(s1.name,s1.age)
print(s2.name,s2.age)