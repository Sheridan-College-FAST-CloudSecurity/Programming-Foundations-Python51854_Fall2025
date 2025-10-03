class Person:#Parent class or base class
    def __init__(self,age,address):
        self.age=age
        self.__address=address

    def getAdderss(self):
        return self.__address
    def setAddress(self,new_address):
        self.__address=new_address
    def display(self):
       print(self.address)
   

#p1.display()
# NOT ALLOWED BECAUSE display is 
# the member of Student class not Person class '''
class Student(Person):#child class of Person
    #id,name
    def __init__(self,id,name,marks):#This is a constructor
        self.id=id #Self is current instance.
        self.name=name
        self.__marks=marks #private variable
#Encapsulating private and public variables in the class
    def display(self):
        print(f"Student id: {self.id}")
        print(f"Student name: {self.name}")
        print(f"Student marks: {self.__marks}")
    
    #Getter Method :to get the value of the private variable
    def getMarks(self):
        return self.__marks
    
    #Setter method:to set and validate the private varible
    def setMarks(self,new_marks):
        if new_marks>=0 and new_marks<=100:
            self.__marks=new_marks
        else:
            print("invalid number")
class Faculty(Person):
    def __init__(self,coursesTaught):
        self.coursesTaught=coursesTaught
    def display(self):
        print(f"Courses Taught: {self.coursesTaught}")

class ITStudent (Student):#Multilevel inheritance
    def __init__(self,programmingLangugeLearnt):
        self.programmingLangugeLearnt=programmingLangugeLearnt
    def display(self):
        print(f"programmingLangugeLearnt: {self.programmingLangugeLearnt}")

s1=Student(10,"Asim",100)#s1 is the object of a Student class
s2=Student(11,"Justin",100)
s1.age=20
s2.name="Jayanta"
print(s2.getMarks())
s2.setMarks(99)
s1.setAddress("Brampton")
print(s1.getAdderss())

print(f"s1.id: {s1.id}")
print(f"s1.age: {s1.age}")
print(s1.name,s2.id,s2.name)
s1.display()#call member function with an object
s2.display()
p1=Person(22,"Brampton")
print(f"person object {p1.age},{p1.getAdderss()}")
p1.name="sdfdfd"#dynamic object creation not inheritance

print(p1.name)
p1.id=100
print(p1.id)
#p1.setMarks(100)
f1=Faculty("PROG32758")
f1.display()
itStudent1=ITStudent("python")
itStudent1.id=12
itStudent1.name="Gurpreet"
itStudent1.setMarks(100)
itStudent1.setAddress("Brampton")
itStudent1.display()
print(itStudent1.getAdderss(),itStudent1.id,
      itStudent1.name)
print(itStudent1.getMarks())
