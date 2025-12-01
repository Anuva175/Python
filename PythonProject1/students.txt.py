def generate_certificate():
    with open("students.txt","r") as f:
        names=f.read().splitlines()
    for name in names:
        with open(f"{name}_certificate.txt","w") as certi:
            certi.write(f"Certificate of Completion\nAwarded to:{name}")
generate_certificate()