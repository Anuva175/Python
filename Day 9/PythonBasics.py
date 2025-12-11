#Ex 1 Write a program that reads a string and prints the number of vowels, consonants, and digits.
'''new=input("Enter a string:")
v=0
c=0
d=0
for i in new:
    if i in "aeiou":
        v=v+1
    elif i not in "aeiou" and i.isalpha():
        c=c+1
    elif i.isdigit():
        d=d+1
print(v)
print(c)
print(d)'''
#2. Create a function that takes a sentence and returns a dictionary of word frequencies.
'''new=input("Enter a string:")
def word(sentence):
    words=sentence.split()
    freq={}
    for i in words:
        freq[i]=freq.get(i,0)+1
    return freq
print(word(new))'''
#Implement a mini calculator with add, subtract, multiply, and divide using functions.
'''def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
a=float(input("Enter a num:"))
b=float(input("Enter b num:"))
print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))'''
#Write a program that reads N numbers and returns the second highest value without sorting.
'''nums=[10,20,30,40,50]
first=second=float('-inf')
for i in nums:
    if i>first:
        second=first
        first=i
    elif first>i>second:
        second=i
print(second)'''

'''num=[10,20,30,40,50]
num.remove(max(num))
print(max(num))'''
#Read 10 values and store them into a list without using loops (use list comprehension).
''''num=[1,2,3,4,5,6,7,8,9,10]
new=[n for n in num]
print(num)'''





