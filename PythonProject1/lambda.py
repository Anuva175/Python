# lambda arguments: expression
square=lambda x:x*x
print(square(5))

add=lambda x,y:x+y
print(add(3,4))

generate_line=lambda user: f"Hello{user},welcome to python training"
def write_dynamic_line(user,filename):
    with open(filename,"w") as f:
        f.write(generate_line(user))
write_dynamic_line("anu","welcome.txt")
##
def write_employee_record(id,name,salary):
    record=f"""
    Employee Record
    ID:{id}
    Name:{name}
    Salary:{salary}
    """
    with open("employee.txt","a") as f:
      f.write(record)

write_employee_record(101,"anu",75000)
write_employee_record(102,"arjun",55000)
with open("employee.txt","r") as f:
    print(f.read())

