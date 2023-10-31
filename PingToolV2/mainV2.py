import os
import sys
import datetime
import shutil
import subprocess
import asyncio

# ping each ip in ipList
with open(input("Ip list file path --> : ")) as file:
    ipList = file.read()
    print(ipList)
    ipList = ipList.splitlines()  # create a list() obj ["ip","ip","ip"...]
    print(ipList)
    print("--Executing autoping script-- \n")

# check if outputFile in directory, if so delete it
sourceFolder = os.getcwd()
print(sourceFolder)

# define file name
# --define current hour
date = datetime.date.today()
currenDate = date.strftime("%d_%m_%Y")
# --define current date
time = datetime.datetime.now()
currentTime = time.strftime("%H-%M-%S")
fileName = f"ip_output_{currenDate}_{currentTime}.txt"

# ping 2 times each ip
for ip in ipList:
    response = os.popen(f"ping -n 2 -w 1 {ip}").read()

    # save output in ip_output.txt file
    if ("Risposta da" or "Reply from") in response:
        print(response)
        f = open(fileName, "a")
        f.write(str(ip) + " is up" + "\n")
        f.close()
    else:
        print(response)
        f = open(fileName, "a")
        f.write(str(ip) + " is down " + "\n")
        f.close()

# create Output folder
for root, dirs, file in os.walk(sourceFolder):
    if os.path.exists("Ping_Output"):
        break
    elif "Ping_Output" not in dirs:
        os.mkdir("Ping_Output")
    else:
        pass

# renamed file path
file = f"Ping_Output\\{fileName}"

fileAbsPath = os.path.abspath(fileName)
# move output.txt to Output folder
shutil.move(fileName, "Ping_Output")

# close the program and display txt output
subprocess.Popen([file], shell=True)
