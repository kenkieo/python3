from .Basic import Basic
from .String_Length_Item import String_Length_Item


class String_Length_Data(Basic):
    def __init__(self):
        self.strings_length_offset = 0
        self.strings_length_content_size = 0
        self.string_length_content_list = None

    def decode(self):
        self.string_length_content_list = [self.decode_item() for i in range(self.strings_length_content_size // 8)]

    @staticmethod
    def decode_item():
        item = String_Length_Item()
        item.decode()
        return item
