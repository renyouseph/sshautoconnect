#!/usr/bin/env python3

##### Server Requirements ####################
# Python        # apt-get install python3
# Pip           # apt-get install -y python3-pip
# PrettyTable   # pip3 install PrettyTable
##############################################
#
# Written by Reny Ouseph
# renyouseph@gmail.com +91 9072997607
#
##############################################

import os
import sys
import subprocess
                                                            ######## Add all hosts here
hostname = { 
             "1":['VPS01 - webserver' ,'18.207.161.68'] , 
             "2":['vps02 - dbserver' ,'191.168.43.131'] , 
             "3":['vps03 - appserver' ,'192.168.120.132'], 
             "4":['vps04 - gameserver' ,'192.168.120.133'],
             "5": ["exit", ""] 
            } 



from prettytable import PrettyTable
result = PrettyTable()
result.field_names = ["Number","Server_name","Server_IP"]

for server in hostname.keys():
    servername = hostname[server][0]
    IP = hostname[server][1]
    result.add_row([server,servername,IP])

print("")
#print("Server's List"'\n'"=============")
#print(result)
print(result.get_string(title="Servers List"))

def takeinput(prompt, errorMessage = 'Incorrect number choosed'):
	while True:
            user_input = input(prompt)
            if user_input == "5":                                        ####### Change exit value as per your requirement
                sys.exit()
            if user_input in hostname:
                host_IP = hostname[user_input][1]
                def sshConnect(host_IP,*,USER='root',PORT=22):                        ######## Define SSH port number here
                    conString = 'ssh -p {} {}@{} {}'.format(PORT,USER,host_IP,'-v')
                    return conString
                return sshConnect(host_IP)
            else:
                print(errorMessage, file=sys.stderr)

serverConnect = takeinput('Please enter a number : ')
subprocess.call(serverConnect,shell=True)
