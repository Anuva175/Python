try:
    x=10/0
except ZeroDivisionError:
    print("Cannot divide by zero")
##value error:
try:
    num=int(input("Enter the number: "))
    print(10/num)
except ValueError:
    print("Invalid number") #alphabets
except ZeroDivisionError:
    print("Cannot divide by zero")
#try except finally
try:
    f=open("data.txt","r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("closing operation completed")
##
try:
    value=int("50")
except ValueError:
    print("Invalid number")##if error occurs this will be exceuted
else:
    print("Coversion successful: ",value)#if the conversion went fine,conversion successful the value
#how do you manually raise it by using the syntax raise
def check_age(age):
    if age<18:
        raise ValueError("Age must be 10 or above")
    return "Allowed"
print(check_age(18))#print(check_age(15))#triggers exception

#how do we create custom exception,which we create?
class LowBalanceError(Exception):
    pass
def withdraw(amount,balance):
    if amount > balance:
        raise LowBalanceError("Insufficient funds")
    return balance-amount
print(withdraw(10,100))