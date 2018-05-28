import struct
from ctypes import *
class udp(structure):
    _fields_ = [
        ("sPort",c_ubyte, 16)
        ("dPort",c_ubyte,16)
        ("Lenth",c_ubyte,16)
        ("chechsum",c_ubyte,16)
        
        ]
    def __new__(self,socket_buffer=none):
        return self.form_buffer_copy(socket_buffer)

    def __init__(self,socket_buffer=none):
        self srcPort=socket.inet_ntoa(struct.pack("@I",self.src))
        self desPort=socket.inet_ntoa(struct.pack("@I",self.des)/)
