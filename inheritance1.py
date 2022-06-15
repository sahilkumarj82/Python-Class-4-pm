
import pandas as pd

class Student:
    def __init__(self):
        file=pd.read_csv("student.csv")
        self.student=list(file["Name"])
    def ShowStudent(self):
        return self.student
    pass

class Teacher:
    def __init__(self):
        file=pd.read_csv("teacher.csv")
        self.teacher=list(file["Name"]) 
    def ShowTeacher(self):
        return self.teacher
    pass

class Combine(Teacher,Student):
    def __init__(self):
        Teacher.__init__(self)
        Student.__init__(self)
        # self.Total = len(self.teacher)+len(self.student)
        pass
    def ShowCombine(self):
        self.both =  self.teacher + self.student 
        return self.both
    pass


Show = input("Enter the data u want to see : ").lower()

if Show=="student" :
    StudentList = Student()
    print(StudentList.ShowStudent())
elif Show=="teacher" :
    TeacherList=Teacher()
    print(TeacherList.ShowTeacher())
elif Show=="combine":
    CombineList=Combine()
    print(CombineList.Total)
    # print(CombineList.ShowCombine())