import struct
from ctypes import *
class ipv6(structure):
    _fields_ = [
        ("version",c_ubyte, 4)
        ("trafficClass",c_ubyte,)
        ("flowLbl",c_ubyte,20)
        ("payloadLenth",c_ubyte,16)
        ("nxtHeader",c_ubyte,)
        ("sIp",c_ubyte,128)
        ("dIp",c_ubyte,128)
         
        ]
    def __new__(self,socket_buffer=none):
        return self.form_buffer_copy(socket_buffer)

    def __init__(self,socket_buffer=none):
        self srcIP=socket.inet_ntoa(struct.pack("@I",self.src))
        self des=socket.inet_ntoa(struct.pack("@I",self.des)/)
