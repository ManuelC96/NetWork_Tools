# -----------------------------------------------------------
# Script to ping multiple ip at once ///////////////////////|
# -----------------------------------------------------------
import os
import sys
import datetime
import subprocess
from pathlib import Path
import shutil


# Emoji
emj = {
    "1": "\U0001f600",
    "2": "\U0001F609",
    "3": "\U0001FAE1",
    "4": "\U0001F60E",
    "crossMark": "\U0000274C",
    "checkMark": "\U00002705",
}

# program tex messagges
print(f"PING TOOL {emj['2']}")
print("")

# get working directory
sourceFolder = os.getcwd()

# get os env user name
userName = os.getenv("USERNAME")

# output file location
desktoFile = f"C:\\Users\\{userName}\\Desktop\\"


# ping each ip in ipList
with open(desktoFile + input(r"Ip list filename --> : ") + ".txt") as file:
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
fileName = f"ip_output_{currenDate}_{currentTime}.txt"

# choose number of ping
n = input("choose number of ping, n = ")
# ping 2 times each ip
for ip in ipList:
    response = os.popen(f"ping -n {n} -w 1 {ip}").read()
    print(response)

    stats = None
    # save output in ip_output.txt file
    if "Reply" in str(response):
        f = open(fileName, "a")
        f.write(str(ip) + " --> Up" + "\n")
        f.write(str(response[int(response.find("Packets")) :]))
        f.write("\n")
        f.close()

    elif "Risposta" in str(response):
        f = open(fileName, "a")
        f.write(str(ip) + " --> Up" + "\n")
        f.write(str(response[int(response.find("Pacchetti")) :]))
        f.write("\n")
        f.close()

    else:
        f = open(fileName, "a")
        f.write(str(ip) + " --> Down " + "\n")
        f.write("\n")
        f.close()


# desktop folder path
desktoFolder = f"C:\\Users\\{userName}\\Desktop\\Ping_Output"

# -----------------------------------------------------------
# |/////////////////////////////////////////////////////////|
# -----------------------------------------------------------
# Exit from current working env, to desktop
# ----change working directory
os.chdir(desktoFile)

# ----create Output folder in desktop
if os.path.isdir(desktoFolder):
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
shutil.move(fileName, desktoFolder)

# file new path
fileNewPath = f"C:\\Users\\{userName}\\Desktop\\Ping_Output\\{fileName}"

# close the program and display txt output
subprocess.Popen([fileNewPath], shell=True)
