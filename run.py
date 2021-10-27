#!/usr/bin/python
import sys
import os
import argparse

if len(sys.argv) < 2:
    exit()


def formatIt(string):
    string = str(string)
    return string.replace(" ", "\ ").replace(")", "\)").replace("(", "\(")


pathIndex = -1
for i in range(1, len(sys.argv)):
    if not sys.argv[i].find("/") == -1 or not sys.argv[i].find(".") == -1:
        pathIndex = i
path = (
    sys.argv[pathIndex]
    if sys.argv[1][0:14] == "/Users/ibrahim"
    else os.getcwd() + "/" + sys.argv[pathIndex]
)
args = ""
for i in range(pathIndex + 1, len(sys.argv)):
    args += " " + sys.argv[i]
options = ""
for i in range(1, pathIndex):
    options += " " + sys.argv[i]

# print(options)
# print(args)
def confirm():
    inp = str(input("would u like to proceed?[y/n]: "))
    while not (inp == "y"):
        inp = str(input("would u like to proceed?[y/n]: "))


def goTo(pathing):  # goes to the path
    os.chdir(pathing)


file = path.split("/")[len(path.split("/")) - 1]

pathTo = path.replace(file, "")

extention = file.split(".")[1] if not file.find(".") == -1 else ""

fileNoExtension = file.split(".")[0] if not file.find(".") == -1 else ""


def runSmart(extension):
    command = None
    if extension == "java":
        command = "     javac " + file + " && java " + fileNoExtension
    elif extension == "cpp":
        command = (
            "     g++ -o " + fileNoExtension + " " + file + " && ./" + fileNoExtension
        )
    elif extension == "c":
        command = (
            "     gcc -o " + fileNoExtension + " " + file + " && ./" + fileNoExtension
        )
    elif extension == "py":
        command = "     python3 " + file
    elif extension == "js":
        command = "      node " + file
    elif extension == "bash" or extension == "sh":
        command = "      bash " + file
    elif extension == "m":
        command = (
            '      /Applications/MATLAB_R2021a.app/bin/matlab -nodesktop -r "run '
            + file
            + '"'
        )
    else:
        print("please use a valid extension")
        return
    command += args
    if command != None:
        os.system(command)


def removeExecutables():
    os.system("find . -name '*.class' -delete")
    os.system("find . -name '%s' -delete" % fileNoExtension)
    os.system("rm -rf __pycache__")
    os.system("find . -name '*.pyc' -delete")


print("\n")
goTo(pathTo)
runSmart(extention)
removeExecutables()
print("\n")
exit()
