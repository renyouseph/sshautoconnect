# sshautoconnect
Python script to connect ssh automatically or user defined

# Feature List:
. If username and port are not passed, python takes the default arguments for username='root' and port=22
. If we pass either username or port, It takes the missing argument automatically.

# Format:
python3 sshconnect.py host \n
python3 sshconnect.py host username port
or
python3 sshconnect.py host username 
or 
python3 sshconnect.py host port
