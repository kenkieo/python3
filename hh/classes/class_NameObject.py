from hh.classes.class_base import ClassBase


class NameObject(ClassBase):
    name = ''

    def decode(self):
        self.name = self.ReadAlignedString()
