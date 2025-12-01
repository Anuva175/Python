def generate_certificate():
    with open("employee.txt","w") as f:
        f.write("Certificate of Completion")
    with open("employee.txt","r") as f:
        names=f.read().splitlines()
    for name in names:
        with open(f"{name}_certificate.txt","w") as certi:
            certi.write(f"Certificate of Completion\nAwarded to:{name}")
generate_certificate()
##Ex-2
def write_certificate():
    with open("student_names.txt", "r") as f:
        student_names = [line.strip() for line in f.readlines() if line.strip()]

    content = "This is certify {name} has successfully completed the course"

    for n in student_names:
        certificate = content.format(name=n)
        filename = f"{n}_Certificate.txt"
        with open(filename, "w") as f:
            f.write(certificate)


write_certificate()
##Ex-3
'''def AttendanceLog(name,timestamp):
    if timestamp>9:
        status="Present"
    else:
        status="Absent"
    list=f"""
    List of students
    name:{name}
    timestamp:{timestamp}
    status:{status}
    """
    with open("attendance.txt","a") as f:
        f.write(list)
AttendanceLog("anu",11)
AttendanceLog("divya",6)
with open("attendance.txt","r") as f:
    print(f.read())'''




