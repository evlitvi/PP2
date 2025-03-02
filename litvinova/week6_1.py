#Python builtin functions exercises
#1
import math
import time 

def list_multi(x):
    return math.prod(x)

print(list_multi([1,2,3,4,5]))

#2
def countLowAndUp(s):
    lower, upper = 0, 0
    for c in s:
        if c.islower():
            lower+=1
        else:
            upper+=1
    return upper, lower

print(countLowAndUp("Hello World"))

#3
def isPalindrome(s):
    return s == "".join(reversed(s))

print(isPalindrome("level"))

#4
def delayedSqrt(ms, num):
    time.sleep(ms/1000)
    return math.sqrt(num)

n = 25
ms = 5000
print(f"Square root of {n} after {ms} miliseconds is {delayedSqrt(ms, n)}")

#5
def allElmsAreTrue(t):
    return all(t)

tuple1 = (1, True, "True")
tuple2 = (1, True, "")
print(allElmsAreTrue(tuple1))
print(allElmsAreTrue(tuple2))