import os
import sys
import datetime
import shutil
import subprocess

# # ping each ip in ipList
# with open("ip_list.txt") as file:
#     ipList = file.read()
#     print(ipList)
#     ipList = ipList.splitlines()  # create a list() obj ["ip","ip","ip"...]
#     print(ipList)
#     print("--Executing autoping script-- \n")

# # check if outputFile in directory, if so delete it
# sourceFolder = sys.path[0]
# print(sourceFolder)

# for root, dir, file in os.walk(sourceFolder):
#     print(file)
#     if "ip_output.txt" in file:
#         print(file.index("ip_output.txt"))
#         index = file.index("ip_output.txt")
#         os.remove("ip_output.txt")

# # ping 2 times each ip
# for ip in ipList:
#     response = os.popen(f"ping -n 2 -w 1 {ip}").read()

#     # save output in ip_output.txt file
#     if ("Risposta da" or "Reply from") in response:
#         print(response)
#         f = open("ip_output.txt", "a")
#         f.write(str(ip) + " is up" + "\n")
#         f.close()
#     else:
#         print(response)
#         f = open("ip_output.txt", "a")
#         f.write(str(ip) + " is down " + "\n")
#         f.close()

# # create Output folder
# for root, dir, file in os.walk(sourceFolder):
#     if os.path.exists("Output"):
#         pass
#     else:
#         os.mkdir("Output")

# # rename file ip_output.txt
# for root, dir, file in os.walk(sourceFolder):
#     if "ip_output.txt" in file:  # rename output.txt
#         print(file.index("ip_output.txt"))
#         index = file.index("ip_output.txt")
#         now = datetime.datetime.now()
#         currentTime = now.strftime("%H-%M-%S")
#         fileName = f"ip_output_{datetime.date.today()}_{currentTime}.txt"
#         os.rename("ip_output.txt", fileName)
#         shutil.move(fileName, "Output")  # move output.txt to Output folder

# # open renamed file to desktop and close program with async func
# file = f"Output\\{fileName}"
# with open(os.system(file)) as f:
#    if f:
#         os._exit(0)


subprocess.Popen(["echo", "hello"], shell=True)
