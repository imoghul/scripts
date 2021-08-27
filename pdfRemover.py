import sys
import glob
import os.path
import time
from time import gmtime
from datetime import datetime, date

files = (
    glob.glob("/Users/ibrahim/Downloads/*.pdf")
    + (glob.glob("/Users/ibrahim/Downloads/*.docx"))
    + (glob.glob("/Users/ibrahim/Downloads/*.ppt"))
    + (glob.glob("/Users/ibrahim/Downloads/*.txt"))
)
# print(files)
scannedPDFs = []
tbRem = []


def formatIt(string):
    string = str(string)
    return string.replace(" ", "\ ").replace(")", "\)").replace("(", "\(")


for f in files:
    if True:  # ((f[25:len(f)])[0:16]=="Scanned Document"):
        scannedPDFs.append(f)
currTime = datetime.strptime(
    time.strftime("%Y-%m-%d %H:%M:%S", gmtime()), "%Y-%m-%d %H:%M:%S"
)
for e in scannedPDFs:
    createdTime = datetime.strptime(
        datetime.fromtimestamp(((os.path.getctime(e)))).strftime("%Y-%m-%d %H:%M:%S"),
        "%Y-%m-%d %H:%M:%S",
    )
    timeDiff = currTime - createdTime
    if timeDiff.total_seconds() / 3600 > 1:
        tbRem.append(e)
if len(tbRem) == 0:
    exit()
for i in tbRem:
    print(str(i) + " will be deleted")

if input("Continue? [(y)/n]: ") == "n":
    exit()
for i in tbRem:
    string = (
        "mv "
        + formatIt(i)
        + " /Users/ibrahim/pdfs/"
        + formatIt(i).replace("/Users/ibrahim/Downloads/", "")
    )  # "mv "+str(i).replace(" ","\ ").replace(")","\)")+" /Users/ibrahim/pdfs/"+str(i).replace(" ","\ ").replace(")","\)").replace("/Users/ibrahim/Downloads/","")
    os.system(string)
exit()
