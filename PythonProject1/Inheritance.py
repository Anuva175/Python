class Animal:
    def speak(self):
        print("I am animal")
class Dog(Animal):
    def bark(self):
        print("dog bark")
d=Dog()
d.speak()#inherited
d.bark()#child's own method
####
class Person:
    def __init__(self,name):#parent constructor
        self.name=name
class Employee(Person):
    def __init__(self,name,emp_id):
        super().__init__(name) # call parent constructor,we use super
        self.emp_id=emp_id
e=Employee("anu",1)
print(e.name)
print(e.emp_id)