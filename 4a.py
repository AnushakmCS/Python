class student:
    def init(self):
        self.sid=None
        self.age=None
        self.marks=None
    def validate_marks(self):
        if self.marks>=0 and self.marks<=100:
            return True
        else:
            print("Enter Valid marks")
            return False
    def validate_age(self):
        if self.age>0:
            return True
        else:
            print("Enter Valid age")
            return False
    def check_qualification(self):
        if self.marks>=65 and self.age>20:
            print("CongrasulationEligible")
        else:
            print("Not Eligible")
    def setter(self):
        self.sid=int(input("Enter sid:-"))
        self.age=int(input("Enter age:-" ))
        self.marks=int(input("Enter marks;-"))

    def getter(self):
        print("Student Details are")
        print("Sid : ",self.sid)
        print("Age : ", self.age)
        print("Marks : ",self.marks)


print("enter the no of students")
n=int(input())

for i in range(0,n):
    p=student()
    p.setter()
    p.validate_marks()
    p.validate_age()
    p.check_qualification()
    p.getter()
