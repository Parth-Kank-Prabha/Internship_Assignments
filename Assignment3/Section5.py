#Challenge 21: Create a class Student with instance attributes name, roll_no, and marks. Create three students and display details.

# class Student:
#     def __init__(self,name,roll_no,marks):
#         self.name=name
#         self.roll_no=roll_no
#         self.marks=marks
#     def display(self):
#         print("Name of Student:",self.name)
#         print("Roll number of Student:",self.roll_no)
#         print("Marks of Student:",self.marks)

# s1=Student("Parth",30,78)
# s1.display()

# s2=Student("Ayush",16,89)
# s2.display()

# s3=Student("Rohan",15,80)
# s3.display()

# Challenge 22: Create a class Employee with instance attributes emp_id, emp_name, and department. Display all employee details.

# class Employee:
#     def __init__(self,emp_id,emp_name,dept):
#         self.emp_id=emp_id
#         self.emp_name=emp_name
#         self.dept=dept
#     def display(self):
#         print("ID of Employee:",self.emp_id)
#         print("Name of Employee:",self.emp_name)
#         print("Department of Employee:",self.dept)
# e1=Employee(100,"Parth Kank","AIML")
# e1.display()

# e2=Employee(101,"Rohan","ENTC")
# e2.display()

# Challenge 23: Create a class Hospital with instance attributes doctor_name and specialization. Create multiple objects and display details.

# class Hospital:
#     def __init__(self,doc_name,specialization):
#         self.doc_name=doc_name
#         self.specialization=specialization
#     def display(self):
#         print("Name of Doctor:",self.doc_name)
#         print("Specialization of Doctor:",self.specialization)
# d1=Hospital("Dr. Rohan","Nuero Specialist")
# d1.display()

# d2=Hospital("Dr. Ayush","Heart Specialist")
# d2.display()

# Challenge 24: Create a class Course with instance attributes course_name, duration, and fees. Display course details.

# class Course:
#     def __init__(self,course_name,duration,fees):
#         self.course_name=course_name
#         self.duration=duration
#         self.fees=fees
#     def display(self):
#         print("Name of Course:",self.course_name)
#         print("Duration of Course:",self.duration)
#         print("Fees of course:",self.fees)

# c1=Course("AIML","3 years",300000)
# c1.display()

# Challenge 25: Create a class CricketPlayer with instance attributes player_name, runs, and matches. Display player details.

class CricketPlayer:
    def __init__(self,player_name,runs,matches):
        self.player_name=player_name
        self.runs=runs
        self.matches=matches
    def display(self):
        print("Name of Player:",self.player_name)
        print("Runs of Player:",self.runs)
        print("Matches of Player:",self.matches)

p1=CricketPlayer("Rohit Sharma",15000,234)
p1.display()
