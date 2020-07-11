BASE64_ENCODE_MAP = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "+", "/"
]
BASE64_DECODE_MAP = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25,
    "a": 26, "b": 27, "c": 28, "d": 29, "e": 30, "f": 31, "g": 32, "h": 33, "i": 34, "j": 35, "k": 36, "l": 37, "m": 38, "n": 39, "o": 40, "p": 41, "q": 42, "r": 43, "s": 44, "t": 45, "u": 46, "v": 47, "w": 48, "x": 49, "y": 50, "z": 51,
    "0": 52, "1": 53, "2": 54, "3": 55, "4": 56, "5": 57, "6": 58, "7": 59, "8": 60, "9": 61,
    "+": 62, "/": 63
}
ENCODE_ALIGN = 3
DECODE_ALIGN = 4


# 01000001 | 01100010 | 01000111
#    A     |    b     |    G
# b 010000 | 010110 | 001001 | 000111
#    A >> 2 | (A << 4 | b >> 4) | (b << 2  | G >> 6) | G & 0b00111111
# b 00010000 | 00010110 | 00001001 | 00000111
#      Q     |     W    |    J     |    H
# 第一位右移2
# (第一位左移4 | 第二位右移4) & 0b00111111
# (第二位左移2 | 第三位右移6)  & 0b00111111
# 第三位 & 0b00111111
def encoding(data):
    if isinstance(data, str):
        data = data.encode()
    data = bytearray(data)
    total = len(data)
    align = total % ENCODE_ALIGN  # 3字节对齐
    if align:
        data.extend(b'\x00' * (ENCODE_ALIGN - align))
        total += ENCODE_ALIGN - align
    ls = []
    for index in range(0, total, ENCODE_ALIGN):
        x, y, z = data[index], data[index + 1], data[index + 2]
        ls.append(BASE64_ENCODE_MAP[x >> 2 & 0b00111111])
        ls.append(BASE64_ENCODE_MAP[(x << 4 | y >> 4) & 0b00111111])
        ls.append(BASE64_ENCODE_MAP[(y << 2 | z >> 6) & 0b00111111])
        ls.append(BASE64_ENCODE_MAP[z & 0b00111111])
    if align == 2:
        ls[-1] = "="
    elif align == 1:
        ls[-1] = "="
        ls[-2] = "="
    return "".join(ls)


# b 00010000 | 00010110 | 00001001 | 00000111
#      Q     |     W    |    J     |    H
#    (Q << 2 | W >> 6) | (W << 4 | J >> 2) | (J << 6 |　Ｈ)
#  01000001 01100010
# (第一位左移2 | 第二位右移4)
# (第二位左移4 | 第二位右移2)
# (第三位左移6 | 第四位)
# 01000001 | 01100010 | 01000111
#    A     |    b     |    G
# b 010000 | 010110 | 001001 | 000111
def decode(data):
    if isinstance(data, str):
        data = data.encode()
    data = bytearray(data)
    total = len(data)
    result = bytearray()
    for index in range(0, total, DECODE_ALIGN):  # 4字节对齐
        try:
            a = BASE64_DECODE_MAP[chr(data[index])]  # 查找位置
            b = BASE64_DECODE_MAP[chr(data[index + 1])]
            result.append((a << 2 & 0xFF) | b >> 4)
            c = BASE64_DECODE_MAP[chr(data[index + 2])]
            result.append((b << 4 & 0xFF) | c >> 2)
            d = BASE64_DECODE_MAP[chr(data[index + 3])]
            result.append((c << 6 & 0xFF) | d)
        except BaseException as e:
            print(e)
    return bytes(result)


if __name__ == '__main__':
    string = "AB"
    result = encoding(string)
    sss = "6Iux6K+t44CB5pel6K+t44CB6Z+p6K+t44CB5rOV6K+t44CB5b636K+t44CB5L+E6K+t44CB6KW/54+t54mZ6K+t44CB6JGh6JCE54mZ6K+t44CB6LaK5Y2X6K+t44CB5Y2w5bC86K+t"
    print(result)
    print(decode(result).decode())
