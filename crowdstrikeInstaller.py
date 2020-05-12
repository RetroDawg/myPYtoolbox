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


#Definition for getting OS ID
def getOperatingSystem_ID():
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
            id = i
        else:
            continue
    return id
#Definition for getting OS VERSION
def getOperatingSystem_VERSION():
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
        if re.match(r'VERSION=',i):
            version = i
        else:
            continue
    return version

def executeCommands(id,version):
    if ("centos" in id) and ("7" in version):
        runCentOS7()
    elif ("centos" in id) and ("8" in version):
        runCentOS8()
    elif ("ubuntu" in id) and ("18.04" in version):
        runUbuntu18_04()
    elif ("ubuntu" in id) and ("20.04" in version):
        runUbuntu20_04()
    else:
        print("Failed to detect Operating System")

def runCentOS7():
    print("Detected CentOS7 running runCentOS7()")

def runCentOS8():
    print("Detected CentOS8 running runCentOS8()")

def runUbuntu18_04():
    print("Detected Ubuntu 18.04 running runUbuntu18_04()")

def runUbuntu20_04():
    print("Detected Ubuntu 20.04 running runUbuntu20_04()")

#####START SCRIPT#####
getRootUser()
id = getOperatingSystem_ID()
version = getOperatingSystem_VERSION()
executeCommands(id,version)
#####END SCRIPT#####
