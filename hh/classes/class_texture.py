from hh.classes.class_base import ClassBase


class ClassTexture(ClassBase):
    def decode(self):
        # 2017.3 and up
        if self.version_str[0] > 2017 \
                or self.version_str[0] == 2017 and self.version_str[1] >= 3:
            self.m_ForcedFallbackFormat = self.ReadInt32()
            self.m_DownscaleFallback = self.ReadBoolean()
            self.AlignStream()
