class Payment:
    def enter_details(self):
        input("Enter the details of your payment")

    def notification(self):
        print("Your payment is successful")

class UPI(Payment):
    def enter_details(self):
        upi = input("Enter your UPI id: ")

    def notification(self):
        print(f"Your UPI Payment is successful")

class InternetBanking(Payment):
    def enter_details(self):
        input("Enter your account details: ")

    def notification(self):
        print("Amount transferred successfully")

class AmazonPay(Payment):
    def enter_details(self):
        input("Enter your Amazon Pay details: ")

    def notification(self):
        print("Amount transferred successfully")

class CreditCard(Payment):
    def enter_details(self):
        input("Enter your Credit Card details: ")

    def notification(self):
        print("Amount transferred successfully")

class DebitCard(Payment):
    def enter_details(self):
        input("Enter your Debit Card details: ")

    def notification(self):
        print("Amount transferred successfully")

p1 = UPI()
p2 = InternetBanking()
p3 = AmazonPay()
p4 = CreditCard()
p5 = DebitCard()



amount = int(input("Enter the amount : "))
balance = 5000
if amount > balance:
    print("Sorry, You don't have sufficient funds in your account")

else:
    print("Choose your mode of payment from the following: \n1.UPI\n2.Internet Banking \n3.Amazon Pay \n4.Credit Card \n5.Debit Card")
    payment_mode = int(input("Enter the payment mode : "))
    if payment_mode == 1:
        p1.enter_details()
        p1.notification()

    elif payment_mode == 2:
        p2.enter_details()
        p2.notification()

    elif payment_mode == 3:
        p3.enter_details()
        p3.notification()

    elif payment_mode == 4:
        p4.enter_details()
        p4.notification()

    elif payment_mode == 5:
        p5.enter_details()
        p5.notification()
