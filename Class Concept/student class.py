class student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def display_details(self):
        print("The information is",self.name,self.roll,self.marks)
    def calculate_grade(self):
        if self.marks>=90:
            return 'A'
        elif self.marks>=75:
            return 'B'
        elif self.marks>=50:
            return 'C'
        else: return "Fail"

name=input("Enter the name:")
roll=int(input("Enter the roll:"))
marks=int(input("Enter the marks:"))
s1=student(name,roll,marks)
s1.display_details()
gr=s1.calculate_grade()
print("The grade is:",gr)

name=input("Enter the name:")
roll=int(input("Enter the roll:"))
marks=int(input("Enter the marks:"))
s2=student(name,roll,marks)
s2.display_details()
gr=s2.calculate_grade()
print("The grade is:",gr)
        
        
