#int and strings, separate them into two tuples:
total=[10,20,30,40,50,"apple","banana","mango"]
num=[]
str=[]
for i in total:
    if isinstance(i,int):
        num.append(i)
    else:
        str.append(i)
print(num)
print(str)
#Given a tuple of numbers, determine whether it is strictly increasing.
t=(1,2,3,4)
is_increasing=True
for i in range(len(t)-1):
    if t[i]>=t[i+1]:
        is_increasing=False
        break
print(is_increasing) #true

#a tuple of words and return a new tuple where each word is reversed.
words=("anu","divya","priya")
result=[]
for w in words:
    rev=""
    for ch in w:
        rev=ch+rev
    result.append(rev)
print(result)#['una', 'ayvid', 'ayirp']