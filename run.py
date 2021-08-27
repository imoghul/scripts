#!/usr/bin/python
import sys
import os
import argparse
import pathlib


parser = argparse.ArgumentParser()
# parser.add_argument()


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
    if command != None:
        os.system(command)


def removeExecutables():
    os.system("find . -name '*.class' -delete")
    os.system("find . -name '%s' -delete" % fileNoExtension)


print("\n")
goTo(pathTo)
runSmart(extention)
removeExecutables()
print("\n")
exit()
