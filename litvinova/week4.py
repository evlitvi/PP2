#Python Math library
#1
import math
degree = int(input("Input degree: "))
radians = degree*(math.pi/180)
print(f"Output radian {radians:.6f}")
#2
height = int(input("Height: "))
base1 = int(input("Base, first value: "))
base2 = int(input("Base, second value: "))
area = 0.5 * (base1+base2)*height
print(f"Expected Output: {area}")
#3
numOfSides = int(input("Input number of sides: "))
lenOfSide = int(input("Input the length of a side: "))
polygonArea = (numOfSides * lenOfSide**2)/(4*math.tan(math.pi/numOfSides))
print(f"The area of the polygon is: {int(polygonArea)}")
#4
baseLen = int(input("Length of base: "))
parHeight = int(input("Height of parallelogram: "))
parArea = baseLen*parHeight
print(f"Expected Output: {parArea}")