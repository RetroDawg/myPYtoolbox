# Developer: Jose Arrisola Jr.
# Goal: This script will install the crowdstike package

# Import Libraries
import subprocess
from subprocess import Popen, PIPE
from glob import glob
from shlex import split
import urllib.request
import sys
import os
import re

# "MY" Customer ID
var_CID = '941077C3CE5C44C4BDF4EB3D3C1CE22F-AE'

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
    #elif ("ubuntu" in id) and ("20.04" in version):
    #    runUbuntu20_04()
    else:
        print("Failed to detect Operating System")

def runCentOS7():
    print("Detected CentOS7 running runCentOS7()")
    url = 'https://repo.geos.tamu.edu/common-configs/toolbox/source/sensor-download/CentOS7/falcon-sensor-5.31.0-9606.el7.x86_64.rpm'
    urllib.request.urlretrieve(url, '/tmp/falcon-sensor-5.31.0-9606.el7.x86_64.rpm')
    try:
        stream = os.popen('/usr/bin/yum install -y /tmp/falcon-sensor-5.31.0-9606.el8.x86_64.rpm')
        output = stream.read()
        
        stream = os.popen('/opt/CrowdStrike/falconctl -s --cid=941077C3CE5C44C4BDF4EB3D3C1CE22F-AE')
        output = stream.read()

        stream = os.popen('/usr/sbin/service falcon-sensor start')
        output = stream.read()

        stream = os.popen('/usr/bin/ps -e')
        output = stream.read()
        if "falcon-sensor" in output:
            print("Falcon Strike Service is now running, please check console to verify.")
        else:
            print("Sensor not runnning, exiting")
            quit()
    except subprocess.TimeoutExpired as err:
        result = err
        print(result)

def runCentOS8():
    print("Detected CentOS8 running runCentOS8()")
    url = 'https://repo.geos.tamu.edu/common-configs/toolbox/source/sensor-download/CentOS8/falcon-sensor-5.31.0-9606.el8.x86_64.rpm'
    urllib.request.urlretrieve(url, '/tmp/falcon-sensor-5.31.0-9606.el8.x86_64.rpm')
    
    try:
        stream = os.popen('/usr/bin/dnf install -y /tmp/falcon-sensor-5.31.0-9606.el8.x86_64.rpm')
        output = stream.read()
        
        stream = os.popen('/opt/CrowdStrike/falconctl -s --cid=941077C3CE5C44C4BDF4EB3D3C1CE22F-AE')
        output = stream.read()

        stream = os.popen('/bin/systemctl start falcon-sensor')
        output = stream.read()

        stream = os.popen('/usr/bin/ps -e')
        output = stream.read()
        if "falcon-sensor" in output:
            print("Falcon Strike Service is now running, please check console to verify.")
        else:
            print("Sensor not runnning, exiting")
            quit()
    except subprocess.TimeoutExpired as err:
        result = err

def runUbuntu18_04():
    print("Detected Ubuntu 18.04 running runUbuntu18_04()")
    url = 'https://repo.geos.tamu.edu/common-configs/toolbox/source/sensor-download/Ubuntu14-16-18/falcon-sensor_5.31.0-9606_amd64.deb'
    urllib.request.urlretrieve(url, '/tmp/falcon-sensor_5.31.0-9606_amd64.deb')
    try:
        stream = os.popen('/usr/bin/dpkg -i -y /tmp/falcon-sensor_5.31.0-9606_amd64.deb')
        output = stream.read()

        stream = os.popen('/opt/CrowdStrike/falconctl -s --cid=941077C3CE5C44C4BDF4EB3D3C1CE22F-AE')
        output = stream.read()

        stream = os.popen('/usr/sbin/service  falcon-sensor start')
        output = stream.read()

        stream = os.popen('/bin/ps -e')
        output = stream.read()
        if "falcon-sensor" in output:
            print("Falcon Strike Service is now running, please check console to verify.")
        else:
            print("Sensor not runnning, exiting")
            quit()
    except subprocess.TimeoutExpired as err:
        result = err

def runUbuntu20_04():
    print("Detected Ubuntu 20.04 running runUbuntu20_04()")
    url = 'https://repo.geos.tamu.edu/common-configs/toolbox/source/sensor-download/Ubuntu14-16-18/falcon-sensor_5.31.0-9606_amd64.deb'
    try:
        stream = os.popen('/usr/bin/dpkg -i -y /tmp/falcon-sensor_5.31.0-9606_amd64.deb')
        output = stream.read()

        stream = os.popen('/opt/CrowdStrike/falconctl -s --cid=941077C3CE5C44C4BDF4EB3D3C1CE22F-AE')
        output = stream.read()

        stream = os.popen('/usr/sbin/service  falcon-sensor start')
        output = stream.read()
        
        stream = os.popen('/usr/bin/ps -e')
        output = stream.read()
        if "falcon-sensor" in output:
            print("Falcon Strike Service is now running, please check console to verify.")
        else:
            print("Sensor not runnning, exiting")
            quit()
    except subprocess.TimeoutExpired as err:
        result = err

#####START SCRIPT#####
getRootUser()
id = getOperatingSystem_ID()
version = getOperatingSystem_VERSION()
executeCommands(id,version)
#####END SCRIPT#####
