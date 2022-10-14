class Personal:
    def __init__(self,name,phno):
        self.name=name
        self.phno=phno
    def display(self):
        print(self.name,self.phno)
class Student1(Personal):
    def __init__(self,rollno,branch,name,phno):
        self.rollno=rollno
        self.branch=branch
        super().__init__(name,phno)
    def display(self):
        print(self.rollno,self.branch,self.name,self.phno)
        super().display()
class Employee(Personal):
    def __init__(self,empid,salary,name,phno):
        self.empid=empid
        self.salary=salary
        super().__init__(name,phno)
    def display(self):
        print(self.empid,self.salary,self.name,self.phno)
        super().display()

s1=Student1(123,'CSE','Teju',1234567)
s1.display()
s2=Student1(456,100000,'Usha',87654321)
s2.display()

'''
priority of variables
sub class instance variable
super class instance variable
sub class class variable
super class class variable
'''
