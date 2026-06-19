#Challenge 16: Create a class Person. Use self to store name and age. Display values using a method.

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def show(self):
#         print("Name of person:",self.name)
#         print("Age of person:",self.age)
# p1=Person("Parth",19)
# p1.show()


#Challenge 17: Create a class Animal. Store animal_name and color. Print values using self.

# class Animal:
#     def __init__(self,animal_name,color):
#         self.animal_name=animal_name
#         self.color=color

#     def display(self):
#         print("Animal Name:",self.animal_name)
#         print("Color of Animal:",self.color)

# a1=Animal("Lion","Brown")
# a1.display()

# Challenge 18: Create a class Vehicle. Store company and model. Display details using a method and self.

# class Vehicle:
#     def __init__(self,company,model):
#         self.company=company
#         self.model=model
#     def display(self):
#         print("Name of company:",self.company)
#         print("Model of Vehicle:",self.model)

# v1=Vehicle("BMW","X7")
# v1.display()

# Challenge 19: Create a class Teacher. Store teacher_name and subject. Display teacher information using self.

# class Teacher:
#     def __init__(self,teacher_name,sub):
#         self.teacher_name=teacher_name
#         self.sub=sub
#     def display(self):
#         print("Name of Teacher:",self.teacher_name)
#         print("Name of Subject:",self.sub)

# t1=Teacher("Jyoti","Coding")
# t1.display()

# Challenge 20: Create a class Player. Store player_name and team. Print details using self.

class Player:
    def __init__(self,player_name,team):
        self.player_name=player_name
        self.team=team
    def display(self):
        print("Name of Player:",self.player_name)
        print("Name of Team:",self.team)

p1=Player("Hardik Pandya","Mumbai Indians")
p1.display()