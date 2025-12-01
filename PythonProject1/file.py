#writing to a file
with open("Sample.txt","w") as f:
    f.write("Hello\n")
    f.write("World")

#Reading from the same file
with open("Sample.txt","r") as f:
    content=f.read()
    print(content)
###Ex-1Write a Python program to create a file named notes.txt and write 5 lines of text into it.
with open("notes.txt","w") as f:
    f.write("Welcome\n")
    f.write("to\n")
    f.write("the\n")
    f.write("Python\n")
    f.write("Training\n")
    ##Ex-2Write a program to read and print the contents of notes.txt line by line.
with open("notes.txt","r") as f:
    content=f.read()
    print(content)
##Ex-3 Write a program that appends a new line to an existing file notes.txt that says:
##"This is an appended line."
with open("notes.txt", "a") as f:
    f.write("This is an appended line.\n")
with open("notes.txt", "r") as f:
    print(f.read())
##Ex-4 Write a program that counts the number of lines in a given file.
filename=input("Enter the file name: ")
count=0
with open("notes.txt","r") as f:
    for line in f:
        count+=1
print(count)
##Ex-5 Write a program that reads a file and counts the number of words in it.
filename=input("Enter the file name: ")
count=0
with open("notes.txt","r") as f:
    for line in f:
        words=line.split()
        count+=len(words)
print("total words: ",count)
##Ex-6 Write a program to copy the contents of one file ( source.txt ) to another file ( backup.txt ).
with open("source.txt", "w") as f:
    f.write("Copy the text")

with open("source.txt", "r") as file:
    text = file.read()

with open("backup.txt", "w") as src:
    src.write(text)

with open("backup.txt", "r") as dest:
    print(dest.read())
#Ex-7 Write a program that reads a text file and prints only those lines that contain the word "Python" .
with open("new.txt", "w") as n:
    n.write("welcome to the python training")
    n.write("java is my favorite language")
with open("new.txt","r") as n:
    for line in n:
        if "Python" in line:
            print(line)
#Ex-8 Write a program to read a CSV file named students.csv and print name and marks of each student.
