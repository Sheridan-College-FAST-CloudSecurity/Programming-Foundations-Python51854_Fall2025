class Camera:
    '''def __init__(self,name,brand):
        self.name=name
        self.brand=brand'''
    def takePhoto(self):
        print("Photo taken")
    def display(self):
        print("Camerta display")
class Phone:
    def makeACall(self):
        print("Make a call")
    def display(self):
        print("Phone display")
class SmartPhone(Phone,Camera):
    def useInternet():
        print("Browsing")
    
myPhone=SmartPhone()
myPhone.makeACall()
myPhone.takePhoto()
myPhone.display()
class Animal:
    def speak(self):
        print("animals speak")
class Dog (Animal):
    def speak(self):
        print("dog speaks")
class Cat (Animal):
    def speak(self):
        print("cat speaks")
animals=[Dog(),Cat(),Animal()]
for a in animals:
    a.speak()
    #Polymorphism one name many uses