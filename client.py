host = "127.0.0.1"
port=4444               # Sets the variable port to 4444
 
from socket import *             # Imports socket module
 
s=socket(AF_INET, SOCK_STREAM)
s.connect((host,port))          # Connect to server address
 
msg=s.recv(1024)            # Receives data upto 1024 bytes and stores in variables msg
 
print ("Message from server : " + msg.strip().decode('ascii'))
 
s.close()   