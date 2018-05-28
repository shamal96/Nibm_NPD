import struct
from ctypes import *
class ip(structure):
    _fields_ = [
        ("version",c_ubyte, 4)
        ("ihl",c_ubyte,4)
        ("tos",c_ubyte)
        ("totLenth",c_ubyte,16)
        ("id",c_ubyte,16)
        ("ipFlags",c_ubyte,3)
        ("fragOffset",c_ubyte,13)
        ("ttl",c_ubyte,8)
        ("hChecksum",c_ubyte,)
        ("sAddress",c_ubyte,32)
        ("dAddress",c_ubyte,32)
        ("totLenth",c_ubyte,)

        ]
    def __new__(self,socket_buffer=none):
        return self.form_buffer_copy(socket_buffer)

    def __init__(self,socket_buffer=none):
        self srcAddress=socket.inet_ntoa(struct.pack("@I",self.src))
        self desAddress=socket.inet_ntoa(struct.pack("@I",self.des))
