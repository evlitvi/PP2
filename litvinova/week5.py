#Python RegEx exercises
import re
def match_string(pattern, s):
    if re.fullmatch(pattern, s):
        return True
    return False
#1
pattern1 = r'^ab*$'
print(match_string(pattern1, "abbbb"))
print(match_string(pattern1, "abbbbc"))

#2
pattern2 = r'^ab{2,3}$'
print(match_string(pattern2, "abb"))
print(match_string(pattern2, "ab"))

#3
pattern3 = r'^[a-z]+_[a-z]+$'
print(match_string(pattern3, "abc_zxc_abbbccc_ssssss"))
print(match_string(pattern3, "a_abc, abc"))

#4
pattern4 = r'^[A-Z][a-z]+$'
print(match_string(pattern4, "Abcdef"))
print(match_string(pattern4, "ABcdef"))

#5
pattern5 = r'^a.*b$'
print(match_string(pattern5, "a6$.-b"))
print(match_string(pattern5, "a6$.-"))

#6
def replace(s):
    pattern = r'[ .,]'
    return re.sub(pattern, ':', s)

print(replace("Hello, World! How are you?"))

#7
def snakeCaseToCamelCase(s):
    words = s.lower().split("_")
    return words[0] + "".join(x.capitalize() for x in words[1:])

print(snakeCaseToCamelCase("snake_case"))

#8
def split_at_uppercase(s):
    pattern = r'[^A-Z]+|[A-Z][^A-Z]*'
    return re.findall(pattern, s)

print(split_at_uppercase("Hello World. My name is Yevgeniya"))

#9
def insertSpace(s):
    pattern = r'([a-z])([A-Z])'
    return re.sub(pattern, r'\1 \2', s)

print(insertSpace("InsertSpace spaceInsert"))

#10
def to_snake_case(s):
    pattern = r'([a-z])([A-Z])'
    snake_case = re.sub(pattern, r'\1_\2', s)
    return snake_case.lower()

print(to_snake_case("CamelCase"))   

