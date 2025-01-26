#Booleans
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Operators
print((6 + 3) - (6 + 3))

#Lists
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

print(thislist[-1])

thislist[0] = "blackcurrant"
print(thislist)

thislist.append("orange")
print(thislist)

thislist.remove("banana")
print(thislist)

for x in thislist:
    print(x)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
print(newlist)

thislist2 = [100, 50, 65, 82, 23]
thislist2.sort()
print(thislist2)

mylist = thislist.copy()
print(mylist)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

#Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

print(thistuple[-1])

list3 = list(thistuple)
list3[1] = "kiwi"
thistuple = tuple(list3)
print(thistuple)

fruits2 = ("apple", "banana", "cherry")
(green, yellow, red) = fruits2
print(green)
print(yellow)
print(red)

for x in thistuple:
    print(x)

mytuple = fruits2 * 2
print(mytuple)

#Sets
thisset = {"apple", "banana", "cherry"}
print(thisset)

for x in thisset:
    print(x)

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thisset.discard("banana")
print(thisset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

model = thisdict.get("model")

thisdict.update({"year": 2020})

thisdict["color"] = "red"
print(thisdict)

thisdict.pop("model")
print(thisdict)

for x in thisdict:
    print(x)

mydict = thisdict.copy()
print(mydict)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#If else
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

#While Loop
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#For Loop
for_list = ["apple", "banana", "cherry"]
for x in for_list:
    print(x)
    if x == "banana":
        break