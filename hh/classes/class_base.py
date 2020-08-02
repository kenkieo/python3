import struct

from hh.classes.class_pptr import PPtr
from hh.classes.reader.unity_reader import UnityReader


class ClassBase(UnityReader):
    version = None
    version_str = None

    def decode(self):
        pass


    def readPPtr(self):
        pptr = PPtr()
        pptr.m_FileID = self.ReadInt32()
        if self.version < 14:
            pptr.m_PathID = self.ReadInt32()
        else:
            pptr.m_PathID = self.ReadInt64()
        return pptr


def Hex2FloatLitte(hex_value):
    return struct.unpack('<f', hex_value)[0]


def Hex2FloatBig(hex_value):
    return struct.unpack('>f', hex_value)[0]
