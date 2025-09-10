"""
PYTHON OOP CONCEPTS - DEMONSTRATION SCRIPT
-------------------------------------------
This program demonstrates the major Object-Oriented Programming (OOP) concepts in Python:
1. Classes & Objects
2. __init__() and __str__()
3. Methods and 'self'
4. Modify/Delete properties & objects
5. Inheritance & super()
6. Iterators (__iter__, __next__, StopIteration)
7. Polymorphism (functions, classes, inheritance)
"""

print("\n==============================")
print(" OOP in Python - Demonstration ")
print("==============================\n")

# ------------------------------------------------------
# 1. CLASSES AND OBJECTS
# ------------------------------------------------------

print("1. CLASSES AND OBJECTS")
print("----------------------")

class MyClass:
    x = 5  # a class attribute

# Create object
p1 = MyClass()
print(f"Created an object p1 from MyClass with x = {p1.x}")

# ------------------------------------------------------
# 2. __init__() and __str__()
# ------------------------------------------------------

print("\n2. __init__() and __str__()")
print("---------------------------")

class Person:
    def __init__(self, name, age):
        self.name = name   # instance attribute
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

p2 = Person("John", 36)
print("Person object with __str__:", p2)

# ------------------------------------------------------
# 3. METHODS AND SELF
# ------------------------------------------------------

print("\n3. METHODS AND SELF")
print("-------------------")

class PersonWithMethod:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p3 = PersonWithMethod("Alice", 28)
p3.greet()

# Important Note: 'self' refers to the instance itself.
# You can technically rename 'self', but it's not recommended.

# ------------------------------------------------------
# 4. MODIFY / DELETE PROPERTIES AND OBJECTS
# ------------------------------------------------------

print("\n4. MODIFY / DELETE PROPERTIES AND OBJECTS")
print("-----------------------------------------")

p3.age = 30
print("Modified age of Alice to:", p3.age)

del p3.age
print("Deleted Alice's age property (no longer exists).")

# ------------------------------------------------------
# 5. INHERITANCE
# ------------------------------------------------------

print("\n5. INHERITANCE")
print("--------------")

class PersonParent:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Child class
class Student(PersonParent):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)  # inherit parent's init
        self.graduationyear = year

    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}!")

s1 = Student("Mike", "Olsen", 2019)
s1.printname()
s1.welcome()

# ------------------------------------------------------
# 6. ITERATORS
# ------------------------------------------------------

print("\n6. ITERATORS")
print("------------")

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:   # stop after 5 numbers
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

print("Iterator output:")
for num in myiter:
    print(num)

# ------------------------------------------------------
# 7. POLYMORPHISM
# ------------------------------------------------------

print("\n7. POLYMORPHISM")
print("----------------")

# Function polymorphism
print("len() works on different types:")
print("String:", len("Hello World!"))
print("Tuple:", len(("apple", "banana", "cherry")))
print("Dictionary:", len({"brand": "Ford", "model": "Mustang", "year": 1964}))

# Class polymorphism
class Car:
    def move(self):
        print("Drive!")

class Boat:
    def move(self):
        print("Sail!")

class Plane:
    def move(self):
        print("Fly!")

print("\nClass polymorphism demonstration:")
for vehicle in (Car(), Boat(), Plane()):
    vehicle.move()

# Inheritance polymorphism
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class CarVehicle(Vehicle):
    pass

class BoatVehicle(Vehicle):
    def move(self):
        print("Sail!")

class PlaneVehicle(Vehicle):
    def move(self):
        print("Fly!")

print("\nInheritance polymorphism demonstration:")
for v in (CarVehicle("Ford", "Mustang"), BoatVehicle("Ibiza", "Touring 20"), PlaneVehicle("Boeing", "747")):
    print(f"{v.brand} {v.model}:", end=" ")
    v.move()

print("\n==============================")
print(" END OF OOP DEMONSTRATION ")
print("==============================")
