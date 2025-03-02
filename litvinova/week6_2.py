#Python Directories and Files exercises
#1

import os
import string

path = "C:\\Users\\Evlit\\Desktop\\works"

def list_directories(path):
    print("Directories: ")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

list_directories(path)

def list_directories_and_files(path):
    directs = []
    files = []
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            directs.append(item)
        elif os.path.isfile(os.path.join(path, item)):
            files.append(item)
    print("Directories: ", directs)
    print("Files: ", files)

list_directories_and_files(path)

def files_in_specific_path(path):
    print(f"Files in {path}: ")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

specificPath = "C:\\Users\\Evlit\\Desktop\\works\\litvinova"
files_in_specific_path(specificPath)

#2
def checkPath(path):
    print(
        f"Path exists: {os.path.exists(path)}",
        f"Readability: {os.access(path, os.R_OK)}",
        f"Writability: {os.access(path, os.W_OK)}",
        f"Executability: {os.access(path, os.X_OK)}",
        sep="\n"
    )

checkPath(path)

#3
def check_path_info(path):
    if os.path.exists(path):
        print(f"Path '{path}' exist")
        print(f"Directory: {os.path.dirname(path)}")
        print(f"Filename: {os.path.basename(path)}")
    else:
        print(f"Path '{path}' does not exist")

check_path_info("C:\\Users\\Evlit\\Desktop\\works\\litvinova\\week6_2.py")
check_path_info("C:\\Users\\Evlit\\Desktop\\works\\litvinova\\cp")

#4
lines = ["Hello World!\n", "My name is Eva\n", "Bye-bye\n"]
with open("pythonLines.txt", "w") as file:
    file.writelines(lines)

with open("pythonLines.txt", "r") as file:
    print(len(file.readlines()))

#5
my_list = ["Cake", "Apple", "Pear"]

with open("foodList.txt", "w") as file:
    file.write("\n".join(my_list))

#6
folder = "C:\\Users\\Evlit\\Desktop\\works\\alphabet"

os.makedirs(folder, exist_ok=True)

for letter in string.ascii_uppercase:
    filename = os.path.join(folder, f"{letter}.txt")
    with open(filename, "w") as file:
        file.write(f"{letter}")

#7
with open("pythonLines.txt", "r") as infile, open("copy.txt", "w") as outfile:
    for line in infile:
        outfile.write(line)


#8
def delete_file(path):
    if not os.path.exists(path):
        print(f"File on '{path}' does not exist")
        return
    if not (os.access(path, os.R_OK) and os.access(path, os.W_OK)):
        print("Access is prohibited")
        return

    try:
        os.remove(path)
        print(f"'{path}' was deleted")
    except Exception as e:
        print(f"{e}")