"""
Ehsan chowdhury
feb 10, 2026
Lab 6: objects and classes 
"""
print("\n ----- Example 1: Create a class -----")
class Circle(object):
    def __init__(self, radius,color):
        self.radius = radius 
        self.color = color 

    #method 
    def add_radius(self,r):
        self.radius += r
        return self.radius
    
class Rectangle(object):
    def __init__(self, height, width, color ):
        self.height = height
        self.width = width 
        self.color = color 

    # method to calculate the area
    def area(self):
        return self.width * self.height
    
    # method to claculate 
    def perimeter(self):
        return self.height * self.width 
# creating an instance of the class, which is an object 
circle1 = Circle(4, "red")
circle2 = Circle(10, "green")

rectangle1 = Rectangle(2,5,"magenta")
rectangle2 = Rectangle(7,3,"blue")

# accessing information in an object 
print(f"The color of circle2 = {circle2.color}")
print(f"The width of rectangle1 = {rectangle1.width}")

# updating data in an object 
# change circle1 color from 'red' to 'yellow'
print(f"The color of circle1 before the update = {circle1.color}")
circle1.color = "yellow"
print(f"The color of circle1 after the update = {circle1.color}")

# accessing a method 
print(f"Radius of circle2 = {circle2.radius}")
# update the raidus by adding 5
circle2.add_radius(5)
print(f"Radius of circle2 after method add_radius = {circle2.radius}")

# accessing methods in Rectangle 
print(f"The area of the rectangle1 with {rectangle1.width} and height {rectangle1.height} is {rectangle1.area()}")
print(f"The perimeter of rectangle2 = {rectangle2.perimeter()}")

print("\n---------- EXERCISE ----------")

# Create a BankAccount class
class BankAccount(object):
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 250.50   # initialize balance as 250.50
    
    # Method to deposit
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance = {self.balance}")
    
    # Method to withdraw
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance = {self.balance}")
        else:
            print("Insufficient funds. Withdrawal cannot be made.")

# Creating an instance of the BankAccount class
useraccount = BankAccount(123456789, "Ehsan chowdhury")

# Demonstrating deposits and withdrawals
useraccount.withdraw(700)    
useraccount.deposit(1000)    
useraccount.withdraw(500)    

# Prompt result
print(f"Final balance = {useraccount.balance}")