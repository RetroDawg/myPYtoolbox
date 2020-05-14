# Developer: Jose Arrisola Jr.
# Goal: This script will install the crowdstike package

# Import Libraries
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
        stream = os.popen('cat /etc/*-release | grep -w "ID="')
        id = stream.read()
    except subprocess.TimeoutExpired as err:
        stream = err
        print(stream)
    return id

#Definition for getting OS VERSION
def getOperatingSystem_VERSION():
    try:
        stream = os.popen('cat /etc/*-release | grep -w "VERSION="')
        version = stream.read()
    except subprocess.TimeoutExpired as err:
        stream = err
        print(stream)
    return version

def executeCommands(id,version):
    if ("centos" in id) and ("7" in version):
        runCentOS7python3Installer()
    elif ("centos" in id) and ("8" in version):
        runCentOS8python3Installer()
    elif ("ubuntu" in id) and ("18.04" in version):
        runUbuntu18_04python3Installer()
    elif ("ubuntu" in id) and ("20.04" in version):
        runUbuntu20_04python3Installer()
    else:
        print("Failed to detect Operating System")

def runCentOS7python3Installer():
    print("Detected CentOS7 running runCentOS7python3Installer")
    try:
        stream = os.popen('/usr/bin/yum install -y python3')
        output = stream.read()

    except subprocess.TimeoutExpired as err:
        stream = err
        print(stream)

def runCentOS8python3Installer():
    print("Detected CentOS8 running runCentOS8python3Installer")
    try:
        stream = os.popen('/usr/bin/dnf install -y python3')
        output = stream.read()        
    
    except subprocess.TimeoutExpired as err:
        stream = err
        print(stream)

def runUbuntu18_04python3Installer():
    print("Detected Ubuntu 18.04 running runUbuntu18_04python3Installer()")
    try:
        stream = os.popen('apt-get -f -y install python3')
        output = stream.read()

    except subprocess.TimeoutExpired as err:
        stream = err
        print(stream)

def runUbuntu20_04python3Installer():
    print("Detected Ubuntu 20.04 running runUbuntu20_04python3Installer()")
    try:
        stream = os.popen('apt-get -f -y install python3')
        output = stream.read()

    except subprocess.TimeoutExpired as err:
        stream = err
        print(stream)

#####START SCRIPT#####
getRootUser()
id = getOperatingSystem_ID()
version = getOperatingSystem_VERSION()
executeCommands(id,version)
#####END SCRIPT#####
