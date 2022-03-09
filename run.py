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
        break
path = (
    sys.argv[pathIndex]
    if sys.argv[1][0:14] == "/Users/ibrahim"
    else os.getcwd() + "/" + sys.argv[pathIndex]
)
options = " "
for i in range(pathIndex + 1, len(sys.argv)):
    options += " " + sys.argv[i]
args = ""
for i in range(1, pathIndex):
    args += " " + sys.argv[i]

args += " "
#print(pathIndex)
def confirm():
    while not (str(input("would u like to proceed?[y/n]: ")) == "y"):pass


def goTo(pathing):  # goes to the path
    os.chdir(pathing)


file = path.split("/")[len(path.split("/")) - 1]

pathTo = path.replace(file, "")

extention = file.split(".")[1] if not file.find(".") == -1 else ""

fileNoExtension = file.split(".")[0] if not file.find(".") == -1 else ""


def runSmart(extension):
    command = None
    if extension == "java":
        command = "     javac " + args + file + options + " && java " + fileNoExtension
    elif extension == "cpp":
        command = (
            "     g++ -o " + args + fileNoExtension + options + " " + file + " && ./" + fileNoExtension
        )
    elif extension == "c":
        command = (
            "     gcc -o " + args + fileNoExtension + options + " " + file + " && ./" + fileNoExtension
        )
    elif extension == "py":
        command = "     python3 " + args + file + options
    elif extension == "js":
        command = "      node " + args + file + options
    elif extension == "bash" or extension == "sh":
        command = "      bash " + args + file + options
    elif extension == "m":
        command = (
            '      /Applications/MATLAB_R2021a.app/bin/matlab -nodesktop -r "run '
            + file
            + '"'
        )
    elif extension == "v":
	command = "     vlog *.v && vsim -c " + fileNoExtension
    else:
        print("please use a valid extension")
        return
    if command != None:
        #print(command)
        os.system(command)


def removeExecutables():
    os.system("find . -name '*.class' -delete")
    os.system("find . -name '%s' -delete" % fileNoExtension)
    os.system("rm -rf __pycache__ > /dev/null 2>&1")
    os.system("find . -name '*.pyc' -delete")


print("\n")
goTo(pathTo)
runSmart(extention)
removeExecutables()
print("\n")
exit()
