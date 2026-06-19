#Challenge 1: Create a module named calculator.py containing functions add(), subtract(), multiply(), divide(). Import the module in another file and perform all operations.
# import  Calculator 

# print("Addition is:",Calculator.add(30,10))
# print("substraction is:",Calculator.subtract(30,10))
# print("multiploication is:",Calculator.multiply(30,10))
# print("division is:",Calculator.divide(20,10))

#Challenge 2: Create a module named employee.py. Store employee name and salary. Create a function to display employee details. Import and use the function in another file.
# import Employee

# Employee.Emp_display()

# Challenge 3: Import the math module and write a program to find square root of 144, value of pi, and factorial of 6.
# import math

# print("Square root of 144:",math.sqrt(144))
# print("Value of PI:",math.pi)
# print("Factorial of 6:",math.factorial(6))


# Challenge 4: Import the random module and generate a random number between 1 and 100 and a random choice from ['Python', 'Java', 'React', 'Django'].
# import random 

# print("Random Number:",random.randint(1,100))
# print("Random choice:",random.choice(['Python', 'Java', 'React', 'Django']))

# Challenge 5: Create a custom module area.py with functions area_circle() and area_rectangle(). Import the module and calculate areas.
# import Area

# print("Area of Circle is:",Area.area_circle(5))
# print("Area of rectangle is :",Area.area_rectangle(10,13))


# Challenge 6: Create a class Student with attributes name and age. Create an object and display the values.
# class Student:
#     Name = "Parth"
#     Age = 18

# s1 = Student()
# print("Student Name:",s1.Name)
# print("Student Age:",s1.Age)


# Challenge 7: Create a class Car with attributes brand and model. Create two objects and display details.
# class Car:
#     Model = "Punch"
#     Brand = "Tata"

# s1 = Car()
# print("Model of Car:",s1.Model)
# s2= Car()
# print("Brand of Car:",s2.Brand)

# Challenge 8: Create a class Book with attributes title, author, and price. Create three objects and display details.
# class Book:
#     Title = "Bhagvat Geeta"
#     author = "Vyasa"
#     price = 299
# s1=Book()
# print("Title of Book:",s1.Title)
# s2=Book()
# print("Author of Book:",s2.author)
# s3=Book()
# print("Price of Book:",s3.price)

# Challenge 9: Create a class Laptop with attributes brand, RAM, and price. Create two objects and print information.
# class Laptop:
#     brand = "ASUS"
#     RAM = "6GB"
#     price = 70000

# s1 = Laptop()
# print("Brand of Laptop:",s1.brand)
# s2 = Laptop()
# print("RAM of Laptop:",s2.RAM)
# s3 = Laptop()
# print("Price of Laptop:",s1.price)

# Challenge 10: Create a class Mobile with attributes company, model, and storage. Create multiple objects and display details

class Mobile:
    company = "Apple / Iphone"
    model = "17 pro"
    storage = "256GB"

s1 = Mobile()
print("Company of Mobile:",s1.company)
s2 = Mobile()
print("Model of Mobile:",s2.model)
s3 = Mobile()
print("Storage of Mobile:",s3.storage)
