#!/usr/bin/env bash
# Developer: Jose Arrisola Jr.
# Goal: This script is the initial check for crowdstrike and installation
if [ -x /opt/CrowdStrike ]; then
  echo "CrowdStrike directory exist, please address the service before continuing."
  exit 1
else 
  :
fi
curl -o /tmp/crowdstrikeInstaller.py https://repo.geos.tamu.edu/common-configs/toolbox/crowdstrikeInstaller.py && chmod +x /tmp/crowdstrikeInstaller.py
if [ -x /usr/bin/python3 ]; then
  /usr/bin/python3 /tmp/crowdstrikeInstaller.py
else
  curl -o /tmp/python3Installer.py https://repo.geos.tamu.edu/common-configs/toolbox/python3Installer.py && chmod +x /tmp/python3Installer.py
  /usr/bin/python /tmp/python3Installer.py
  /usr/bin/python3 /tmp/crowdstrikeInstaller.py
fi
