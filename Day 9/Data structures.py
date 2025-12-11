#6. Given a list of product prices, remove duplicates while maintaining order.
'''list=[10,20,20,30,10,40,50]
result=[]
for i in list:
    if i not in result:
        result.append(i)
print(result)'''
#7. Merge two lists into a dictionary of {key: value} where list1 is keys and list2 is values.
'''list1=["a","b","c"]
list2=[1,2,3]
d=dict(zip(list1,list2))
print(d)'''
#8. Given a dictionary of student marks, return the top 3 students.
'''marks={"A":90,"B":100,"C":70,"D":60}
top3=sorted(marks.items(),key=lambda x:x[1],reverse=True)[:3]
print(top3)
#9. Flatten a nested list like [[1,2],[3,4],[5,6]] into a single list.
nested=[[1,2],[3,4],[5,6]]
d=[x for n in nested for x in n]
print(d)
#Find common elements between three sets.
a={1,2,2,3}
b={2,3,4}
c={5,6,2,3}
print(a & b & c)'''
#Convert a list of tuples to a dictionary only if keys are unique
list=[("a",1),("b",2),("c",3)]
d={}
for k,v in list:
    if k not in d:
        d[k]=1
print(d)
#12. Given a tuple of names, return one tuple with unique names.
names=("anu","varsini","anu")
unique=tuple(dict.fromkeys(names))
print(unique)
#13. Build a program to reverse every alternate element in a list.
lst=["one","two","three","four","five","six"]
for i in range(1,len(lst),2):
    lst[i]=lst[i][::-1]
print(lst)
#14. From a dictionary of employees, filter only employees with salary above 60000.
emp={
    "A":40000,
    "B":50000,
    "C":60000,
    "D":70000,
    "E":80000,
}
filtered={k:v for k,v in emp.items() if v>60000}
print(filtered)
#15. Given two dictionaries, combine them but sum values for matching keys.
d1={"a":10,"b":20,"c":30}
d2={"b":40,"c":50,"d":60}
result={}
for k in set(d1)|set(d2):
    result[k]=d1.get(k,0)+d2.get(k,0)
print(result)
