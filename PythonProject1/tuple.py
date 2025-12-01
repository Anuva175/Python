'''fruits=('apple','banana','mango')
print(fruits[0])
print(fruits[1])
print(fruits[-1])'''

'''nums=[1,2,2,2,5]
print(nums.count(2))'''#3

'''letters=['a','b','c','d','e','f']
print(letters.index('a'))''' #0

'''data=10,20,30 #packing 
a,b,c=data  #unpacking
print(a,b,c)'''

'''nums=(1,2,3)
nums[1]=5 #Error:tuple does not support item assignment'''

numbers=(33,20,30,60,50)
max=numbers[0]
min=numbers[0]
for num in numbers:
    if num>max:
        max=num
        if num<min:
        min=num
print(max)
print(min)