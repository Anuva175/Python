from calendar import error


class Student:
    pass
s1=Student() # new --new object is being created
s2=Student()

#Example 2
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s3=Student("anu","22")
s4=Student("div","21")
s5=Student("varsh","12")
print(s3.name)
print(s3.age)
print(s5.age,s5.name)
print(s4.age,s4.name)

#Example 3
class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def display(self):
        print("Brand:",self.brand)
        print("model:",self.model)
        print("year:",self.year)
#creating three car objects
car1=Car("bmw",'10',2020)
car1.display() #displaying details
print() #it will give one line to the nxt to display
car2=Car("toyota",'10',2020)
car2.display() #displaying details
print()
car3=Car("tesla",'10',2020)
car3.display() #displaying details

#Example 4
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("name:",self.name)
        print("salary:",self.salary)
e1=Employee("anu",25000)
e2=Employee("varsh",25000)
e1.display()
print()
e2.display()
print()


#nextexample
balance =0
class Account:

    def withdraw(self,amount):
        global balance
        balance-=amount
    def deposit(self,amount):
        global balance
        balance+=amount
acc=Account()
acc.deposit(100)
acc.withdraw(50)
print(balance)
#####
num1=10
num2=20
class Calculator:
    def add(self,num1,num2):
        return num1+num2
    def sub(self,num1,num2):
        return num1-num2
    def mul(self,num1,num2):
        return num1*num2
    def div(self,num1,num2):
        if(num1==0):
            return "error"
        else:
            return num1/num2
maths=Calculator()
print(maths.add(10,20))
print(maths.sub(10,20))
print(maths.mul(10,20))
print(maths.div(10,20))

###
class Student:
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def total(self):
        return self.m1+self.m2+self.m3
    def percentage(self):
        return(self.total()/300)*100
    def display(self):
        print("name:",self.name)
        print("m1: ",self.m1)
        print("m2: ",self.m2)
        print("m3: ",self.m3)
        print("Total: ",self.total())
        print("Percentage: ",self.percentage())
obj1=Student("anu",99,40,98)
obj1.display()
