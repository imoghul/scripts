#!/usr/bin/python
import sys
import os
import argparse
import pathlib


parser = argparse.ArgumentParser()



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
# if len(sys.argv) > 2:
#     print(sys.argv[2:])


def confirm():
    inp = str(input("would u like to proceed?[y/n]: "))
    while not (inp == "y"):
        inp = str(input("would u like to proceed?[y/n]: "))


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
    return "     javac " + getFile() + " && java " + getFileNoExtension()


def runCpp():
    return "     g++ -o " + getFileNoExtension() + " " + getFile() + " && ./" + getFileNoExtension()


def runC():
    return "     gcc -o " + getFileNoExtension() + " " + getFile() + " && ./" + getFileNoExtension()


def runPy():
    return "     python3 " + getFile()


def runJs():
    return "      node " + getFile()


def runMatlab():
    return '      /Applications/MATLAB_R2021a.app/bin/matlab -nodesktop -r "run ' + getFile() + '"'


def runSmart(extension):
    command = None
    if extension == "java":
        command = runJava()
    elif extension == "cpp":
        command = runCpp()
    elif extension == "c":
        command = runC()
    elif extension == "py":
        command = runPy()
    elif extension == "js":
        command = runJs()
    elif extension == "m":
        command = runMatlab()
    else:
        print("please use a valid extension")
    if(command!=None):os.system(command)


def removeExecutables():
    os.system("find . -name '*.class' -delete")
    os.system("find . -name '%s' -delete"%getFileNoExtension())


print("\n")
goTo(getPathTo())
runSmart(getExtension())
removeExecutables()
print("\n")
exit()