from .Basic import Basic


class String_Content_Data(Basic):
    def __init__(self):
        self.string_content_list = None
        self.string_length_data = None

    def decode(self):
        self.string_content_list = [self.read_string(string_length_item.string_length) for string_length_item in self.string_length_data.string_length_content_list]
