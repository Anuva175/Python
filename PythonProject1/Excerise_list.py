'''nums=[23,89,12,78,55,42]
largest=float('-inf')
second=float('-inf')
for n in nums:
    if n>largest:
        second=largest
        largest = n
    elif largest>n>second:
      second=n
print(second)'''

'''num=[0,3,0,5,7,0,9]
result=[]
zeros=0
for n in num:
    if n==0:
        zeros=zeros+1
    else:
        result.append(n)
output=result+[0]*zeros
print(output)'''
#— Interchange First and Last Elements
'''num=['a','b','c','d','e']
num[0],num[4]=num[4],num[0]
print(num)'''
#primeno
'''nums = [10, 11, 12, 13, 17, 20, 23]
prime=0
for n in nums:
    for i in range(2,nums):
        if n%i==0:
            prime=prime+1
    if prime==0:
        print
            break
        else:
           print(nums)'''
#Given a list of integers, rearrange the list so that all negative numbers appear first and all positive
#numbers appear later,
num=[-4,-5,-1,2,3,4,5]
neg=[]
pos=[]
for n in num:
    if n<0:
        neg.append(n)
    else:
        pos.append(n)
result=neg+pos
print(result) #[-4, -5, -1, 2, 3, 4, 5]

#remove all string length is >3
words=["apple","ball","call","hi","ok"]
remove=[]
for n in words:
    if len(n)>3:
        remove.append(n)
print(remove)#['apple', 'ball', 'call']

a=[[1, 2], [3, 4], [5]]
flat=[]
for n in a:
    for x in n:
        flat.append(x)
print(flat)#[1, 2, 3, 4, 5]





