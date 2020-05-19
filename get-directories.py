#!/usr/bin/python
#Created by: Jose Arrisola Jr.
#Objective: Python script to list out active directories and list their size.
#Notes:
import os
import sys
from datetime import datetime
#Declare a directory to search in, default is /home directory
VAR_searchDirectory = "/stor/home/research"
VAR_searchDirectory = "/home"
#Declare List's
x = []
y = []
z = []
#Definition for checking Root USer
def getRootUser():
    stream = os.popen('echo $USER')
    output = stream.read()
    if "root" in output:
        pass
    else:
        print ("PLEASE RUN SCRIPT AS ROOT")
        sys.exit()
# Function to convert
def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
    # return string
    return str1
def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size
#Definition to generate a lits by most recent activity per file
def generateDirectoryList():
    os.chdir(VAR_searchDirectory)
    VAR_dirList = os.listdir(".")
    for name in VAR_dirList:
        i = 0
        #x.append(name)
        #Access Time
        at = (os.stat(name).st_atime)
        at_format = datetime.utcfromtimestamp(at).strftime('%Y-%m-%d')
        #print(datetime.utcfromtimestamp(at).strftime('%Y-%m-%d'))
        #Modify Time
        mt = (os.stat(name).st_mtime)
        #print(datetime.utcfromtimestamp(mt).strftime('%Y-%m-%d'))
        mt_format = datetime.utcfromtimestamp(mt).strftime('%Y-%m-%d')
        #Change Time
        ct = (os.stat(name).st_ctime)
        #print(datetime.utcfromtimestamp(ct).strftime('%Y-%m-%d'))
        ct_format = datetime.utcfromtimestamp(ct).strftime('%Y-%m-%d')
        if  mt >= ct and mt >= at :
                #print(mt_format," (mt) is greater than or equal to (ct) ",ct_format)
                recent = mt_format
        elif ct >= mt and ct >= at :
                #print(ct_format," (ct) is greater than (mt) ",mt_format)
                recent = ct_format
        else:
                recent = at_format
        x.append((name+',',recent))
        y.append(x)
    return y
#Definition to print list into something more bash friendly
def bashprint(arr):
     i = 0
     for d in range(len(arr)):
        print(listToString(arr[i][d]))
        i = i + 1
###BEGIN SCRIPT###
getRootUser()
z = generateDirectoryList()
#z.sort()
bashprint(z)
###END SCRIPT####
