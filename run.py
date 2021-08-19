#!/usr/bin/python
import sys
import os


def formatIt(string):
    string = str(string)
    return string.replace(" ", "\ ").replace(")", "\)").replace("(", "\(")


directory = os.getcwd() + "/"
path = directory
for i in range(1, len(sys.argv)):
    if i > 1:
        path += " " + sys.argv[i]
    else:
        path += sys.argv[i]
if len(sys.argv) > 2:
    print(sys.argv[2:])

def confirm():
    inp = str(raw_input("would u like to proceed?[y/n]: "))
    while not (inp == "y"):
        inp = str(raw_input("would u like to proceed?[y/n]: "))


def getFile():  # returns file with extension
    elements = path.split("/")
    return elements[len(elements) - 1]


def getPathTo():  # returns entire path to file without file
    return path.replace(getFile(), "")


def getExtension():  # returns extension
    if not getFile().find(".") == -1:
        return getFile().split(".")[1]
    return ""


def getFileNoExtension():  # returns file without extension
    if not getFile().find(".") == -1:
        return getFile().split(".")[0]
    return ""


def goTo(pathing):  # goes to the path
    os.chdir(pathing)


def runJava():
    command = "     javac " + getFile() + " && java " + getFileNoExtension()
    os.system(command)


def runCpp():
    command = (
        "     g++ -o "
        + getFileNoExtension()
        + " "
        + getFile()
        + " && ./"
        + getFileNoExtension()
    )
    os.system(command)


def runC():
    command = (
        "     gcc -o "
        + getFileNoExtension()
        + " "
        + getFile()
        + " && ./"
        + getFileNoExtension()
    )
    os.system(command)


def runPy():
    command = "     python3 " + getFile()
    os.system(command)


def runJs():
    command = "      node " + getFile()
    os.system(command)


def runMatlab():
    command = (
        '      /Applications/MATLAB_R2021a.app/bin/matlab -nodesktop -r "run '
        + getFile()
        + '"'
    )
    os.system(command)


def runSmart(extension):
    if extension == "java":
        runJava()
    elif extension == "cpp":
        runCpp()
    elif extension == "c":
        runC()
    elif extension == "py":
        runPy()
    elif extension == "js":
        runJs()
    elif extension == "m":
        runMatlab()
    else:
        print("please use a valid extension")


def removeExecutables():
    os.system("find . -name '*.class' -delete")
    os.system("find . -name '%s' -delete"%getFileNoExtension())


print("\n")
goTo(getPathTo())
runSmart(getExtension())
removeExecutables()
print("\n")
exit()