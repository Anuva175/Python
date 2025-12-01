'''num=int(input("Enter a number: "))
num1=int(input("Enter another number: "))
num2=int(input("Enter another number: "))
if num>num1 and num1>num2:
    print(num)
elif num1>num and num1>num2:
    print(num1)
else:
    print(num2)'''
##Ex-2
'''a="madam"
rev=a[::-1]
if a==rev:
    print("Palindrome")
else:
    print("Not Palindrome")'''
##Ex-3
str="apple"
count={}
for char in str:
    if char in count:
        count[char]+=1
    else:
        count[char]=1
print(count)  #{'a': 1, 'p': 2, 'l': 1, 'e': 1}
#Ex-4
string="anu@$%"
for i in string:
    if i.isalpha():
        print(i,end="") #anu
#Ex-5
arr=[10,10,20,30,30]
new=[]
for i in arr:
    if i not in new:
        new.append(i)
print(new)
#Ex-6
def rotate(lst,n):
    n=n%len(lst)
    return lst[-n:]+lst[:-n]##right position
nums=[1,2,3,4,5]
rotated=rotate(nums,3)
print(rotated)
##Ex-7
##Given a list of strings, return a new list containing only strings longer than 4 characters.arr=["apple","orange","kiw"]
words=["apple","hi","dog","banana"]
new=[]
for i in words:
    if len(i)>4:
        new.append(i)
print(new)
##Ex-8 Write a program to convert a list of tuples into a dictionary.
t={"name:anu","age:22","salary:50000"}
print(t)
#Ex-9
tu={10,20,30,40}
result=max(tu)
print(result)
