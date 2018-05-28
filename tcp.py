import struct
from ctypes import *
class tcp(structure):
    _fields_ = [
        ("sPort",c_ubyte, 16)
        ("dPort",c_ubyte,16)
        ("seqNumber",c_ubyte,32)
        ("ackNumber",c_ubyte,32)
        ("offset",c_ubyte,4)
        ("reserved",c_ubyte,4)
        ("tcpFlags",c_ubyte,8)
        ("window",c_ubyte,16)
        ("checksum",c_ubyte,16)
        ("urgentPointer",c_ubyte,16)
        ("tcoOption",c_ubyte,32)
        

        ]
    def __new__(self,socket_buffer=none):
        return self.form_buffer_copy(socket_buffer)

    def __init__(self,socket_buffer=none):
        self srcPort=socket.inet_ntoa(struct.pack("@I",self.src))
        self desPort=socket.inet_ntoa(struct.pack("@I",self.des)/)
