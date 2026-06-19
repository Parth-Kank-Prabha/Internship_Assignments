# Challenge 26: Create a class Rectangle with an instance method calculate_area(). Take length and width from constructor.

# class Rectangle:
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     def calculate_area(self):
#         return self.l * self.b

# r1=Rectangle(12,3)

# print("Length:",r1.l)
# print("Width:",r1.b)
# print("Area of Rectangle:",r1.calculate_area())

# Challenge 27: Create a class Circle with an instance method calculate_area(). Take radius from constructor.

# class Circle:
#     def __init__(self,r):
#         self.r=r

#     def calculate_area(self):
#         return 3.14 * self.r * self.r
    
# c1=Circle(5)

# print("Radius:",c1.r)
# print("Area of Circle:",c1.calculate_area())

# Challenge 28: Create a class Employee with an instance method annual_salary(). Calculate yearly salary.        

# class Employee:
#     def __init__(self,emp_name,monthly_salary):
#         self.emp_name=emp_name
#         self.monthly_salary=monthly_salary
#     def annual_salary(self):
#         return self.monthly_salary * 12
    
# e1=Employee("Parth Kank",25000)

# print("Employee Name:",e1.emp_name)
# print("Monthly Salary:",e1.monthly_salary)
# print("Annual Salary:",e1.annual_salary())

# Challenge 29: Create a class Student with an instance method calculate_percentage(). Calculate percentage from marks.

# class Student:
#     def __init__(self,stud_name,marks_obtained,total_marks):
#         self.stud_name=stud_name
#         self.marks_obtained=marks_obtained
#         self.total_marks=total_marks

#     def calculate_percentage(self):
#         return (self.marks_obtained /  self.total_marks) * 100
    
# s1=Student("Parth",478,600)

# print("Name of Stuent:",s1.stud_name)
# print("Marks of Student:",s1.marks_obtained)
# print("Percentage of Student:",s1.calculate_percentage())

# Challenge 30: Create a class BankAccount with methods deposit() and withdraw(). Update account balance.

# class BankAccount:
#     def __init__(self,accountant_name,balance):
#         self.accountant_name=accountant_name
#         self.balance=balance

#     def deposite(self,amount):
#         self.balance += amount
#         print("Deposited Succesfully:",amount)

#         print("Balance after deposite:",self.balance)

#     def withdraw(self,amount):
#         if  amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawl Succesful")
#         else:
#             print("Insufficient Balance")

#         print("Balance after withdrawl:",self.balance)

# c1=BankAccount("Parth Kank",8000)
# c1.deposite(2000)
# c1.withdraw(10000)

