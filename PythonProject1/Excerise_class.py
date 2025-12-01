class Product:
    def __init__(self,name,price,quntity):
        self.name=name
        self.price=price
        self.quntity=quntity
    def method(self):
        print(self.price*self.quntity)
sub1=Product("Sub Product",100,6)
sub1.method()
#ex-7
class Customer:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    def check(self):
        if self.age>=25:
            print(self.name+" is eligible")
        else:
            print(self.name+" is not eligible")
c1=Customer("rahul",22,"Mumbai")
c1.check()
#ex-8
'''class BankAccount:
    def __init__(self,deposit,withdraw,balance):
        self.deposit=deposit
        self.withdraw=withdraw
        self.balance=balance'''
###ex-9
class Mobile:
    def __init__(self,brand,model,storage):
        self.brand=brand
        self.model=model
        self.storage=storage
    def update(self,new_storage):
        if new_storage>self.storage:
          self.storage=new_storage
m1=Mobile("samsung",24,256)
m1.update(new_storage=500)
print(m1.storage)
###ex-10
class HighStudent:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def total(self):
        return self.m1+self.m2+self.m3
    def percentage(self):
        return (self.total()/300)*100
    def grade(self):
        g=self.percentage()
        if g>=90:
            return "A"
        elif g>=80:
            return "B"
        elif g>=70:
            return "C"
        else:
            return "D"
st1=HighStudent(98,85,55)
st1.grade()
print(st1.grade())
##
class ShoppingCart:
    def __init__(self):
        self.items=[]
    def add_item(self,name,price,):
        self.items.append((name,price))
        print(name,"added to cart")
    def remove_item(self,name):
        for item in self.items:
            if item[0]==name:
                self.items.remove(item)
                print(name,"removed from cart")
                return
            print(name,"not in cart")
    def total_cost(self):
        total=0
        for item in self.items:
            total+=item[1]
        return total
    def apply_discount(self,percent):
        total=self.total_cost()
        discount=(total*percent)/100
        final_price=total-discount
        return final_price
    def display_items(self):
        if not self.items:
            print("No items to display")
            return
        print("items to display:")
        for name,price in self.items:
            print(name,"=",price)
cart=ShoppingCart()
cart.display_items()
print(cart.items)
print(cart.total_cost())


