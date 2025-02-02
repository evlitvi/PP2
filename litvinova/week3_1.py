import random
#Python Functions
    #1
grams = int(input())
def to_ounces(g):
    return g*28.3495231

print(to_ounces(grams))

    #2
fahrenheit = int(input())
def to_centigrade(f):
    return (5/9)*(f-32)

print(to_centigrade(fahrenheit))

    #3
heads, legs = 35, 94
def solve(numheads, numlegs):
    rabbits = (numlegs - 2*numheads)/2
    chickens = numheads - rabbits
    print(f"{rabbits} rabbits and {chickens} chickens")

solve(heads,legs)

    #4
nums = input().split()
nums = [int(num) for num in nums]
def filter_prime(nums):
    return [num for num in nums if num>1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))]

print(filter_prime(nums))    

    #5
str1=input()
def strPermutation(str):
    if len(str) == 1:
        return [str]
    permutations = []

    for i in range(len(str)):
        current = str[i]
        remaining = str[:i] + str[i+1:]

        perms = strPermutation(remaining)

        for j in range(len(perms)):
            permutations.append(current + perms[j])
    return permutations

print(strPermutation(str1))

    #6
str2=input()
def reverseSentence(str):
    words = str.split()
    return ' '.join(words[::-1])
  
print(reverseSentence(str2))

    #7
nums2=input().split()
nums2 = [int(num) for num in nums2]
def has_33(nums):
    result = False
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            result = True
            break
    return result

print(has_33(nums2))

    #8
nums3 = input().split()
nums3 = [int(num) for num in nums3]
def has_007(nums):
    result = False
    for i in range(len(nums)-2):
        if nums[i:i+3] == [0,0,7]:
            result = True
            break
    return result

print(has_007(nums3))

    #9
PI = 3.14
radius = int(input())
def volumeOfSphere(r,PI):
    return (4/3)*PI*(r**3)
print(volumeOfSphere(radius,PI))

    #10
nums4 = input().split()
nums4=[int(num) for num in nums4]
def uniqueNums(nums):
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums

print(uniqueNums(nums4))

    #11
str3=input().lower()
def isPalindrome(str):
    return str == str[::-1]

print(isPalindrome(str3))

    #12
nums5 = input().split()
nums5 = [int(num) for num in nums5]
def histogram(nums):
    for num in nums:
        print('*' * num)

histogram(nums5)

    #13
name = input("Hello! What is your name? ")
print(f"Well, {name}, I am thinking of a number between 1 and 20. Take a guess. ")
ranNum = random.randint(1,20)
def guessTheNumber(name):
    n=0
    while(True):
        guess=int(input())
        n+=1
        if guess>ranNum:
            print("Your guess is too high. Take a guess. ")
        elif guess<ranNum:
            print("Your guess is too low. Take a guess. ")
        elif guess == ranNum:
            print(f"Good job, {name}! You guessed my number in {n} guesses!") 
            break
guessTheNumber(name)    
