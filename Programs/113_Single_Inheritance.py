class person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

class Student(person):
    def __init__(self, name, age, rollNo, marks):
        super(Student, self).__init__(name, age)
        self.rollNo = rollNo
        self.marks = marks
    
    def getRollNo(self):
        return self.rollNo
    
    def getMarks(self):
        return self.marks

s = Student("Krutarth", 20, 1, 90)
print(s.getName())
print(s.getAge())
print(s.getRollNo())
print(s.getMarks())

p = person("Krutarth", 20)
print(p.getName())
print(p.getAge())