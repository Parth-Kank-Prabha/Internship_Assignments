# file=open("Student.txt","x")
# file=open("Student.txt","w")
# file.write("Name: Parth")
# file.close()

# file = open("Student.txt","r")
# data= file.read()
# print(data)
# file.close()

# file=open("Student.txt","a")
# file.write("\nCity:pune")
# file.close()
# file=open("Student.txt","r")
# data=file.read()
# print(data)
# file.close()

# file=open("Student.txt","r")
# data=file.readline()
# print(data)
# file.close()

# import os
# if os.path.exists("Student.txt"):
#     print("file exists")
# else:
#     print("File not found")


file=open("Student.txt","w")
file.write("")
file=open("Student.txt","a")
for i in range(5):
    name = input(f"Enter Student{i+1} name:")
    file.write(f"\nStudent {i+1} :{name}")
file=open("Student.txt","r")
data=file.read()
print(data)
file.close()