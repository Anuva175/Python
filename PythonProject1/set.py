#Sets dont allow duplicates
data={1,2,2,3,3,3}
print(data)

#how to create a set
s2={10,20,30}
empty=set() #correct way to create an empty set

#add operations
s={1,2,3}
s.add(6)
print(s)
s.update([4,5,6])
print(s)

#remove operations
s.remove(3) #raises error if not found
print(s)
s.discard(11) #it does nothing if not found
print(s)

#Union
a={1,2,3}
b={3,4,5}
print(a|b) #{1, 2, 3, 4, 5}
print(a-b) #{1, 2}
print(b-a) #{4,5}

s={10,20,30}
print(30 in s) #true

for item in{4,8,12}:
    print(item)

num=[1,2,3,3,4,5]
unique=list(set(num))
print(unique) #[1, 2, 3, 4, 5]

student={
    "name":"anu",
    "age":18,
    "city":"cbe"
}
'''print(student["name"]) #anu
print(student["age"])  #18
print(student["city"])#cbe
print(student.get("name"))#anu
student["email"]="anu@gamil.com"
student["city"]="trichy"
print(student["email"])#anu@gmail.com
print(student["city"])#trichy

student.pop("city") #remove by key
print(student)
#del student["city"] #delete
print(student)
student.clear()
print(student) #empty dictionary'''

for k in student.keys(): #left side
    print(k)
for v in student.values(): #right side values eg anu
        print(v)
for k,v in student.items():
            print(k,v) #items both key n value