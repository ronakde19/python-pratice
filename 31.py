class Teacher:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)

t1 = Teacher('Ronak', 45)
t1.display()