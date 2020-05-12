# Developer: Jose Arrisola Jr.
# Goal: This script will install the crowdstike package

# Import Libraries
#from subprocess import Popen, PIPE
import subprocess
from subprocess import Popen, PIPE
from glob import glob
from shlex import split
import sys
import os
import re

#Definition for checking Root User
def getRootUser():
    stream = os.popen('echo $USER')
    output = stream.read()
    if "root" in output:
        pass
    else:
        print ("PLEASE RUN SCRIPT WITH SUDO PRIVILEDGES")
        sys.exit()

def runCentOS7():
    print("In runCentOS7()")

def runCentOS8():
    print("In runCentOS8()")

def runUbuntu18_04():
    print("In runUbuntu18_04()")

def runUbuntu20_04():
    print("In runUbuntu20_04()")

#Definition for getting OS release
def getOperatingSystem():
    #pipe1 = subprocess.Popen(split("/usr/bin/cat /etc/*-release"), stdout=PIPE) 
    try:
        pipe1 = subprocess.run(
        ["cat"] + glob("/etc/*-release"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True)
    except subprocess.TimeoutExpired as err:
        pipe1 = err
    result = pipe1.stdout.splitlines()
    for i in result:
        if re.match(r'ID=', i):
            print(i)
            name = i
        elif re.match(r'VERSION=',i):
            print(i)
            version_id = i
        else:
            continue
    if ("centos" in name) and ("7" in version_id):
        runCentOS7()
    elif ("centos" in name) and ("8" in version_id):
        runCentOS8()
    elif ("ubuntu" in name) and ("18.04" in version_id):
        runUbuntu18_04()
    elif ("ubuntu" in name) and ("20.04" in version_id):
        runUbuntu20_04()
    else:
        print("Failed to detect Operating System")

#####START SCRIPT#####
getRootUser()
getOperatingSystem()
#####END SCRIPT#####
