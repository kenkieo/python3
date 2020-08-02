class Basic:
    read_f = None
    write_f = None
    json_result = None

    def read_int_32(self):
        return int.from_bytes(self.read_f.read(4), byteorder='little')

    def write_int_32(self, value):
        self.write_f.write(int(value).to_bytes(4, byteorder='little'))

    def read_string(self, length):
        return self.read_f.read(length).decode()

    def write_string(self, length):
        return self.read_f.read(length).decode()

    def decode(self):
        pass

    def seek(self, offset, is_read=True):
        if is_read:
            self.read_f.seek(offset)
        else:
            self.write_f.seek(offset)

    def tell(self):
        return self.read_f.tell()

    def encode(self):
        pass

    def close(self):
        if self.read_f:
            self.read_f.close()
        if self.write_f:
            self.write_f.close()

    @staticmethod
    def align_4(value: bytearray, align=4):
        value_length = len(value)
        sub = value_length % align
        if sub != 0:
            value.extend(b'\x00' * (4 - sub))
