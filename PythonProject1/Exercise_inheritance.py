from Inheritance import Dog
#single 1
class Animal:
    def __init__(self,name):
        self.name=name
class Cat(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color=color
d1=Cat("David","black")
print(d1.name,d1.color)
#single 2
class Company:
    def __init__(self,name):
        self.name=name
class Employee(Company):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary=salary
e1=Employee("Anu",100000)
print(e1.name,e1.salary)
#multilevel inheritance 1
class Person:
    def __init__(self,name):
        self.name=name
class Employee(Person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary=salary
class Manager(Employee):
    def __init__(self,name,salary,emp_id):
        super().__init__(name,salary)
        self.emp_id=emp_id
em1=Manager("varshh",50000,10)
print(em1.name,em1.salary,em1.emp_id)
###multilevel -2
class Animal:
    def __init__(self,name):
        self.name=name
class Mammal(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
class Dog(Mammal):
    def __init__(self,name,breed,age):
        super().__init__(name,breed)
        self.age=age
m1=Dog("buddy","golden_retriver",7)
print(m1.name,m1.breed,m1.age)
##multiple
class Phone:
    def __init__(self,number):

        self.number=number
class Camera:
    def __init__(self,megapixel):

        self.megapixel=megapixel
class SmartPhone(Phone,Camera):
    def __init__(self,number,megapixel,storage):
        Phone.__init__(self,number)
        Camera.__init__(self,megapixel)
        self.storage=storage
s1=SmartPhone(111,10,256)
print(s1.number,s1.megapixel,s1.storage)
##multiple 2
class ContentCreator:
    def __init__(self,name):
        self.name=name
class Teacher:
    def __init__(self,experience):
        self.experience=experience
class OnlineTrainer(ContentCreator,Teacher):
    def __init__(self,name,experience,Timing):
        ContentCreator.__init__(self,name)
        Teacher.__init__(self,experience)
        self.Timing=Timing
c1=OnlineTrainer("anu","5","9-5" )
print(c1.name,c1.experience,c1.Timing)
##Hierarchial-1
class Vehicle:
    def __init__(self,number):
        self.number=number

class Car(Vehicle):
    def __init__(self,number,color):
        Vehicle.__init__(self,number)
        self.color=color
class Bike(Vehicle):
    def __init__(self,number,type):
        Vehicle.__init__(self,number)
        self.type=type
class Trunk(Vehicle):
    def __init__(self,number,weight):
        Vehicle.__init__(self,number)
        self.weight=weight

c1=Car(123,"red")
b1=Bike(123,"blue")
t1=Trunk(123,45)
print(c1.number,c1.color,b1.number,b1.type,t1.number,t1.weight)
##hierarchial2
class Shape:
    def __init__(self,size):
        self.size=size
class Circle(Shape):
    def __init__(self,size,radius):
        Shape.__init__(self,size)
        self.radius=radius
class Rectangle(Shape):
    def __init__(self,size,height):
        Shape.__init__(self,size)
        self.height=height
class Triangle(Shape):
    def __init__(self,size,width):
        Shape.__init__(self,size)
        self.width=width
c1=Circle(12,1.2)
b1=Rectangle(12,12)
t1=Triangle(12,7)
print(c1.size,c1.radius)
print(b1.size,b1.height)
print(t1.size,t1.width)




