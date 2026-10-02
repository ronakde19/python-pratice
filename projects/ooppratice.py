class Student():
    def __init__(self,name,marks,attendance):
        self.name = name
        self.marks = marks
        self.attendance = attendance

    def calculate_grade(self):
        if self.marks >=90:
            return "A"
        elif self.marks >=75:
            return "B"
        else:
            return "C"

s1 = Student("Ronak",92,50)
print(s1.calculate_grade( nh))
