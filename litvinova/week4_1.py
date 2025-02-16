#Python iterators and generators
#1
def square_Gen(n):
    for i in range(1, n+1):
        yield i**2

num = int(input())
for square in square_Gen(num):
    print(square)

#2
def even_Gen(n):
    for i in range(n):
        if i%2==0:
            yield str(i)

num2 = int(input())
print(", ".join(even_Gen(num2)))

#3
def divBy3And4_Gen(n):
    for i in range(n):
        if i%3==0 and i%4==0 :
            yield i

num3 = int(input())
for num in divBy3And4_Gen(num3):
    print(num)

#4
def squares_Gen(a, b):
    for i in range(a, b+1):
        yield i**2

num4 = int(input())
num5 = int(input())
for num in squares_Gen(num4, num5):
    print(num)

#5
def downToZero_Gen(n):
    for i in range(n,-1,-1):
        yield i

num6 = int(input())
for num in downToZero_Gen(num6):
    print(num)