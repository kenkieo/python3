from pygame import overlay

from hh.classes.class_NameObject import NameObject
from hh.classes.class_base import ClassBase, Hex2FloatLitte, Hex2FloatBig
from hh.classes.class_kerningValues import ClassKerningValue
from hh.classes.class_pptr import PPtr


class ClassFont(NameObject):
    def decode(self):
        super().decode()
        if not self.version_str: return
        if self.version_str[0] == 5 and self.version_str[1] >= 5 or self.version_str[0] > 5:
            self.m_LineSpacing = self.ReadSingle()
            self.m_DefaultMaterial = self.readPPtr()
            self.m_FontSize = self.ReadSingle()
            self.m_Texture = self.readPPtr()
            self.m_AsciiStartOffset = self.ReadInt32()
            self.m_Tracking = self.ReadSingle()
            self.m_CharacterSpacing = self.ReadInt32()
            self.m_CharacterPadding = self.ReadInt32()
            self.m_ConvertCase = self.ReadInt32()
            self.m_CharacterRects_size = self.ReadInt32()
            for i in range(self.m_CharacterRects_size):
                self.index += 44
            self.m_KerningValues_size = self.ReadInt32()
            self.ClassKerningValueList = ()
            for i in range(self.m_KerningValues_size):
                ckv = ClassKerningValue()
                ckv.char_1 = self.ReadShort()
                ckv.char_2 = self.ReadShort()
                ckv.padding = self.ReadSingle()
            self.m_PixelScale = self.ReadSingle()
            self.m_FontData_size = self.ReadInt32()
            self.m_FontData = self.ReadBytes(self.m_FontData_size)
            self.m_Ascent = self.ReadSingle()
            self.m_Descent = self.ReadSingle()
            self.m_DefaultStyle = self.ReadSingle()
            self.mAscent = self.ReadSingle()
            self.m_FontNames_length = self.ReadInt32()
            self.m_FontNames = [self.ReadAlignedString() for i in range(self.m_FontNames_length)]
            self.m_FallBackFonts = self.ReadInt32()



if __name__ == '__main__':
    import os
    os.path.join(r"F:\游戏\com.seenax.HideAndSeek\Data", )
