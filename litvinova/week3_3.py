import math
#1
class StringChange:
    def __init__(self):
        self.text = ""
    
    def getString(self):
        self.text = input("Enter a string: ")
    
    def printString(self):
        print(self.text.upper())

str1 = StringChange()
str1.getString()
str1.printString()

#2

class Shape:
    def __init__(self):
        pass

    def area(self):
        print(0)
    
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length**2)

square1 = Square(5)
square1.area()

#3

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        print(self.length * self.width)

rect1 = Rectangle(5,4)
rect1.area()

#4

class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def show(self):
         print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, x_move, y_move):
        self.x += x_move
        self.y += y_move

    def dist_to_point(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def dist(self, x, y):
        return math.sqrt((self.x - x)**2 + (self.y - y)**2)
    
point1 = Point(2,3)
point2 = Point(5,5)
point1.show()
point1.move(2,2)
point1.show()
print(point1.dist_to_point(point2))
print(point1.dist(4,6))
#5

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"New balance: {self.balance}")

    def withdrawal(self, amount):
        if amount> self.balance:
            print("Insufficient funds. Withdrawal denied.")
        else:
            if amount > 0:
                self.balance -= amount
                print(f"Withdrawal of {amount} was successful. New balance: {self.balance}")

card1 = Account("Yevgeniya", 3000)
card1.withdrawal(5000)
card1.deposit(2000)
card1.withdrawal(5000)

#6

nums = input().split()
nums = [int(num) for num in nums]

def is_prime(num):
    if num<2:
        return False
    else:
        for i in range (2, num//2+1):
            if num%i == 0:
                return False
        return True
    
prime_nums = list(filter(lambda x: is_prime(x), nums))
print(prime_nums)
    

