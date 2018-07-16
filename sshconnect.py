### Requirements ####
# apt-get install python3
# apt-get install openssh-server
###

import os
import subprocess
import sys

IHOST = sys.argv[1]
IUSER = 'root'
IPORT = 22

if len(sys.argv) == 4:
    IUSER = sys.argv[2]
    IPORT = sys.argv[3]
if len(sys.argv) == 3:
    if sys.argv[2].isdigit():
        IPORT = sys.argv[2]
    else:
        IUSER = sys.argv[2]

def sshConnect(HOST,*,USER='root',PORT=22):
  conString = 'ssh -p {} {}@{} {}'.format(PORT,USER,HOST,'-v')
  return conString

command = sshConnect(IHOST,USER=IUSER,PORT=IPORT)
subprocess.call(command,shell=True)
