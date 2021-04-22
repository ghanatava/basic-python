class Student:
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name

    def __str__(self):
        return "class str is called"
    def __len__(self):
        return len(self.name)
    def __del__(self):
        print('student is destroyed') 

student=Student(10,'Naruto')
print(str(student))
print(len(student))
del(student)