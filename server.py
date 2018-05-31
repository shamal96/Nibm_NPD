#host="127.0.0.1"                # Set the server address to variable host
host="127.168.2.75"                # Set the server address to variable host
port=4446                   # Sets the variable port to 4444

from socket import *                # Imports socket module
s=socket(AF_INET, SOCK_STREAM)
s.bind((host,port))                 # Binds the socket. Note that the input to 
                                            # the bind function is a tuple
s.listen(1)                         # Sets socket to listening state with a  queue
                                            # of 1 connection
print ("Listening for connections.. ")
q,addr=s.accept()               # Accepts incoming request from client and returns
                                            # socket and address to variables q and addr
data=input("Enter data to be send:  ")  # Data to be send is stored in variable data from
                                            # user
q.sendall(data.encode('utf-8'))                        # Sends data to client
s.close()
