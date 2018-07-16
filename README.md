# sshautoconnect
Python script to connect ssh automatically or user defined

## Feature List:
* If username and port are not passed, python takes the default arguments for username='root' and port=22 <br />
* If we missed to pass any of the keyword parameters, it taking the missing parameter by itself.

### Usage:
```
[root@server]# python3 sshconnect.py host 
[root@server]# python3 sshconnect.py host username port
or
[root@server]# python3 sshconnect.py host username 
or
[root@server]# python3 sshconnect.py host port 
````
