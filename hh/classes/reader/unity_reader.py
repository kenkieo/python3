import struct


class UnityReader:
    byte_order = "big"
    index = 0
    data = bytearray()

    def AlignStream(self):
        align = len(self.data) % 4
        if align:
            self.ReadBytes(4 - align)

    def ReadBytes(self, count=1):
        data = self.data[self.index:self.index + count]
        self.index += count
        return data

    def ReadInt32(self):
        data = self.ReadBytes(4)
        if self.byte_order == 'big':
            return struct.unpack('>i', data)[0]
        else:
            return struct.unpack('<i', data)[0]

    def ReadShort(self):
        data = self.ReadBytes(4)
        if self.byte_order == 'big':
            return struct.unpack('>h', data)[0]
        else:
            return struct.unpack('<h', data)[0]

    def ReadInt64(self):
        data = self.ReadBytes(4)
        if self.byte_order == 'big':
            return struct.unpack('>l', data)[0]
        else:
            return struct.unpack('<l', data)[0]

    def ReadBoolean(self):
        data = self.ReadBytes()
        return data == 1

    def ReadSingle(self):
        data = self.data[self.index:self.index + 4]
        self.index += 4
        if self.byte_order == 'big':
            return struct.unpack('>f', data)[0]
        else:
            return struct.unpack('<f', data)[0]

    def ReadString(self, length):
        return self.ReadBytes(length)

    def ReadAlignedString(self):
        length = self.ReadInt32()
        value = self.ReadString(length)
        self.AlignStream()
        return value
