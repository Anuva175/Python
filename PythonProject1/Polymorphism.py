class Notification:
    def send(self,message):
        print("Sending notification: ",message)
class EmailNotification(Notification):
    def send(self,message):
        print("Sending email: ",message)
class SMSNotification(Notification):
    def send(self,message):
        print("Sending sms: ",message)
class PushNotification(Notification):
    def send(self,message):
        print("Sending push: ",message)
n1=EmailNotification()
n1.send("Your order is confirmed")

n2=SMSNotification()
n2.send("your otp is 5252")

n3=PushNotification()
n3.send("You have a new message")
###
class Payment:
    def Pay(self,message):
        print("Available Balance: ",message)
class GooglePay(Payment):
    def Pay(self,message):
        print("Mode of Payment:",message)
class PhonePay(Payment):
    def Pay(self,message):
        print("status of order:",message)
class Paytm(Payment):
    def Pay(self,message):
        print("order number:",message)
p1=GooglePay()
p1.Pay("GooglePay")
p2=PhonePay()
p2.Pay("your order is confirmed")
p3=Paytm()
p3.Pay("your order number is 123456")
##overloading
class Mathops:
    def add(self,a,b=0,c=0):
        return a+b+c
m=Mathops()
print(m.add(5))
print(m.add(5,6))
print(m.add(5,8,9))
##
class Mathops:
    def add(self,*args):
        return sum(args)
m=Mathops()
print(m.add(2))
print(m.add(2,3))
print(m.add(2,3,4))