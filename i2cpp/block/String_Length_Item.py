from .Basic import Basic


class String_Length_Item(Basic):
    def __init__(self):
        self.string_length = 0
        self.string_offset = 0

    def decode(self):
        self.string_length = self.read_int_32()
        self.string_offset = self.read_int_32()
        self.offset = self.tell()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '%10d -- %10d --- %10d \n' % (self.string_length, self.string_offset, self.offset)
