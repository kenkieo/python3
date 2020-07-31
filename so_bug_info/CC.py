s = list()
key = "l1l1l1l1"
length = len(key)
print(length ** length)
for i in range(length ** length):
    result = ""
    for j in range(length):
        result = result + key[(i // (length ** (length - j))) % length]
    if result in s: continue
    s.append(result)
for i in s:
    print('#define XXXX %s' % i)
