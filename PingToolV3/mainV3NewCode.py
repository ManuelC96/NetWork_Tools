# -----------------------------------------------------------
# Script to ping multiple ip at once ///////////////////////|
# -----------------------------------------------------------
import os
import sys
import datetime
import subprocess
import shutil
from pathlib import Path
from pathlib import PurePath


# Emoji
emj = {"1": "\U0001f600", "2": "\U0001F609", "3": "\U0001FAE1", "4": "\U0001F60E"}

# program tex messagges
print(f"PING TOOL {emj['2']}")
print("")

# get working directory
sourceFolder = os.getcwd()

# get os env user name
userName = os.getenv("USERNAME")

# output file location
# desktoFile = f"C:\\Users\\{userName}\\Desktop\\"
desktop = PurePath("Desktop\\")

# ping each ip in ipList
with open(str(desktop) + input("Ip list filename --> : ") + ".txt") as file:
    print("")
    ipList = file.read()
    ipList = ipList.splitlines()  # create a list() obj ["ip","ip","ip"...]
    print("Executing...")

# define file name
# --define current hour
date = datetime.date.today()
currenDate = date.strftime("%d_%m_%Y")
# --define current date
time = datetime.datetime.now()
currentTime = time.strftime("%H-%M-%S")
fileNameUp = f"ip_UP_{currenDate}_{currentTime}.txt"
fileNameDown = f"ip_DOWN_{currenDate}_{currentTime}.txt"

# ping 2 times each ip
for ip in ipList:
    response = os.popen(f"ping -n 2 -w 1 {ip}").read()

    # save output in ip_output.txt file
    if ("Risposta da" or "Reply from") in response:
        print(response)
        f = open(fileNameUp, "a")
        f.write(str(ip) + " is up" + "\n")
        f.close()
    else:
        print(response)
        f = open(fileNameDown, "a")
        f.write(str(ip) + " is down " + "\n")
        f.close()


# desktop folder path
# desktoFolder = f"C:\\Users\\{userName}\\Desktop\\Ping_Output"


# -----------------------------------------------------------
# |/////////////////////////////////////////////////////////|
# -----------------------------------------------------------
# Exit from current working env, to desktop
# ----change working directory
os.chdir(desktoFile)

# ----create Output folder in desktop
for item in desktop.iterdir():
    if item == "Ping_Output":
        pass

else:
    os.mkdir("Ping_Output")
# -----------------------------------------------------------
# |/////////////////////////////////////////////////////////|
# -----------------------------------------------------------

# return to mainV3.py working env
# ----change working directory
os.chdir(sourceFolder)

# get path to desktop file
file = f"C:\\Users\\{userName}\\Desktop\\{fileName}"

# move output.txt to Output folder in desktop
desktoFolder = Path("Ping_Output")
shutil.move(fileName, desktoFolder)

# file new path
fileNewPath = f"C:\\Users\\{userName}\\Desktop\\Ping_Output\\{fileName}"

# close the program and display txt output
subprocess.Popen([fileNewPath], shell=True)
os.kill(os.fork(), signal.SIGSTOP)
