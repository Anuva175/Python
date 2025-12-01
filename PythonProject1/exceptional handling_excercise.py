#Write a program that takes two numbers as input and handles division by zero using try–except.
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
try:
    print(a/b)
except ZeroDivisionError:
    print("Division by zero")
#  Write a program to read a file. Handle FileNotFoundError and PermissionError.
'''f=open("test.txt","r")
try:
    print(f.read())
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission Error")'''
#Write a function that converts a string to integer and handles invalid inputs.
try:
    value=int("anu")
    print(value)
except ValueError:
    print("Invalid input")
#Build a safe list access function: if index is out of range, return a message instead of error.
def safe_get(lst, index, message="Index out of range"):
    if 0<=index<len(lst):
        return lst[index]
    else:
        return message
my_list=[1,2,3,4,5,6,7,8,9,10]
print(safe_get(my_list,1))#2
print(safe_get(my_list,2))#3
print(safe_get(my_list,11))#index out of range
#Create a function that raises a custom exception InvalidAgeError if age < 18.
def check_age(age):
    if age<18:
        raise ValueError("Age is less than or equal to 18")
    return "Allowed"
print(check_age(18))
#Write a program that attempts to convert items of a list to integers, handling conversion errors individually.
items=["10","20","abc","def","90"]
converted=[]
for i in items:
    try:
        num=int(i)
        converted.append(num)
    except ValueError:
        print(f"Cannot Convert'{i}' to integer")
        converted.append("null")
print("Convertedlist:",converted)
#Create a bank withdrawal function that raises LowBalanceError when balance is insufficient.
balance=1000
class loadbalanceerror(Exception):
    pass
def withdraw(amount,balance):
    if amount > balance:
        raise loadbalanceerror("Insufficient balance")
    return balance-amount
print(withdraw(10,1000))