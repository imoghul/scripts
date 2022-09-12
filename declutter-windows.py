#!/usr/bin/python
import sys
import glob
import os.path, shutil
import time
from time import gmtime
from datetime import datetime, date

pathToDownloads = "C:/Users/Ibrahim Moghul/Downloads"
os.chdir(pathToDownloads)


def formatIt(string):
    return str(string)


def sort(doctype, folder=None):
    if folder == None:
        folder = doctype

    files = (glob.glob("*.%s" % doctype.lower())) + (
        glob.glob("*.%s" % doctype.upper())
    )
    detected = []
    tbRem = []
    for f in files:
        if f[0] != "~":  # ((f[25:len(f)])[0:16]=="Scanned Document"):
            detected.append(f)
    currTime = datetime.strptime(
        time.strftime("%Y-%m-%d %H:%M:%S", gmtime()), "%Y-%m-%d %H:%M:%S"
    )
    for e in detected:
        createdTime = datetime.strptime(
            datetime.fromtimestamp(((os.path.getctime(e)))).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "%Y-%m-%d %H:%M:%S",
        )
        timeDiff = currTime - createdTime
        if timeDiff.total_seconds() / 3600 > 1:
            tbRem.append(e)
    if len(tbRem) == 0:
        # print("No %s's to declutter" % doctype)
        return True
    for i in tbRem:
        print(str(i))  # + " will be deleted")

    for i in tbRem:
        string = "mv " + formatIt(i) + " %s/" % folder + formatIt(i)
        try:shutil.move(formatIt(i),"%s/"%folder + formatIt(i))#os.system(string)
        except:continue
    return False


res = [
    sort("pdf"),
    sort("doc"),
    sort("docx", "doc"),
    sort("ppt"),
    sort("pptx", "ppt"),
    sort("txt"),
    sort("HEIC"),
    sort("xlsx"),
    sort("xls", "xlsx"),
    sort("png"),
    sort("jpg"),
    sort("jpeg", "jpg"),
]
val = True
for r in res:
    val &= r
if val:
    print("Already clean!")
exit()
