#16. Build a Student class storing id, name, and marks. Add methods to calculate grade.
class Student:
    def __init__(self,id,name,marks):
        self.id=id
        self.name=name
        self.marks=marks
    def grade(self):

        if self.marks>=90:
            return "A"
        elif self.marks>=80:
            return "B"
        elif self.marks>=70:
             return "C"
        else:
            return "D"
s=Student(1,"anu",95)
print(s.grade())
#17. Implement a Product → ElectronicProduct (inheritance) where Electronics adds warranty years.
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class ElectronicProduct(Product):
    def __init__(self,name,price,warranty):
        super().__init__(name,price)
        self.warranty=warranty
e=ElectronicProduct("Electronic",9000,5)
print(e.name,e.price,e.warranty)
#18. Create a Payment class with credit-card and UPI subclasses overriding process_payment().
class Payment:
    def process_payment_method(self):
        return "Process Payment"
class CreditCardPayment(Payment):
    def process_payment_method(self):
        return "Paid using creditcard"
class UPI(Payment):
    def process_payment_method(self):
        return "Paid using UPI"
p1=CreditCardPayment()
p2=UPI()
print(p1.process_payment_method())
print(p2.process_payment_method())
#create a vehicle class and car bike subclasses override max_speed
class Vehicle:
    def max_speed(self):
        return "Max Speed"
class car(Vehicle):
    def max_speed(self):
        return 180
class Bike(Vehicle):
    def max_speed(self):
        return 120
c=car()
print(c.max_speed())
b=Bike()
print(b.max_speed())
#Implement operator overloading:add two objects of account to return total balance
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def __add__(self,other):
        return BankAccount(self.balance+other.balance)
    def __str__(self):
        return f"Balance: {self.balance}"
a1=BankAccount(100)
a2=BankAccount(200)
a3=a1+a2
print(a3)
#Build a shopping cart class implementing add,remove,total,apply_discount
class ShoppingCart:
    def __init__(self):
        self.items={}
    def add(self,item,price):
        self.items[item]=price
    def remove(self,item):
        if item in self.items:
            del self.items[item]
    def total(self):
        return sum(self.items.values())
    def apply_discount(self,percent):
        return self.total()*(1-percent/100)
cart=ShoppingCart()
cart.add('Bag',100)
cart.add('shoe',200)
print(cart.total())
print(cart.apply_discount(5))
#Create a library class to store book and a method to search by title or author
class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,title,author):
        self.books.append((title,author))
    def search(self,keyword):
        return [b for b in self.books if keyword.lower() in b[0].lower() or keyword.lower() in b[1].lower()]
lib=Library()
lib.add_book('python Basics',"John")
lib.add_book('python advanced',"James")
print(lib.search('python'))
#23. Create a User class and an Admin subclass that can delete a user (override methods).
