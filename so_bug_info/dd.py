LIBART = "libart.so"
_ZN3art3JNI16CallObjectMethodE = "_ZN3art3JNI16CallObjectMethodE"
_ZN3art3JNI17CallObjectMethodA = "_ZN3art3JNI17CallObjectMethodA"
_ZN3art3JNI17CallObjectMethodV = "_ZN3art3JNI17CallObjectMethodV"
_ZN3art3JNI22CallStaticObjectMethodE = "_ZN3art3JNI22CallStaticObjectMethodE"
_ZN3art3JNI23CallStaticObjectMethodA = "_ZN3art3JNI23CallStaticObjectMethodA"
_ZN3art3JNI23CallStaticObjectMethodV = "_ZN3art3JNI23CallStaticObjectMethodV"
CheckJNI16CallObjectMethodE = "CheckJNI16CallObjectMethodE"
CheckJNI17CallObjectMethodAEP = "CheckJNI17CallObjectMethodAEP"
CheckJNI17CallObjectMethodVEP = "CheckJNI17CallObjectMethodVEP"
CheckJNI22CallStaticObjectMethodEP = "CheckJNI22CallStaticObjectMethodEP"
CheckJNI23CallStaticObjectMethodAEP = "CheckJNI23CallStaticObjectMethodAEP"
CheckJNI23CallStaticObjectMethodVEP = "CheckJNI23CallStaticObjectMethodVEP"
_ZN3art3JNI11GetMethodID = "_ZN3art3JNI11GetMethodID"
_ZN3art3JNI17GetStaticMethodID = "_ZN3art3JNI17GetStaticMethodID"
SYSTEM_PATH = "/system"
TYPE_I = ")I"
TYPE_Z = ")Z"
TYPE_B = ")B"
TYPE_C = ")C"
TYPE_S = ")S"
TYPE_J = ")J"
TYPE_F = ")F"
TYPE_D = ")D"
TYPE_V = ")V"
FLOAT_CLS = "java/lang/Float"
METHOD_INIT = "<init>"
RESULT_F = "(F)V"
DOUBLE_CLS = "java/lang/Double"
RESULT_D = "(D)V"
LIB_64 = "lib64"

s = {}
s["LIBART"] = LIBART
s["_ZN3art3JNI16CallObjectMethodE"] = _ZN3art3JNI16CallObjectMethodE
s["_ZN3art3JNI17CallObjectMethodA"] = _ZN3art3JNI17CallObjectMethodA
s["_ZN3art3JNI17CallObjectMethodV"] = _ZN3art3JNI17CallObjectMethodV
s["_ZN3art3JNI22CallStaticObjectMethodE"] = _ZN3art3JNI22CallStaticObjectMethodE
s["_ZN3art3JNI23CallStaticObjectMethodA"] = _ZN3art3JNI23CallStaticObjectMethodA
s["_ZN3art3JNI23CallStaticObjectMethodV"] = _ZN3art3JNI23CallStaticObjectMethodV
s["CheckJNI16CallObjectMethodE"] = CheckJNI16CallObjectMethodE
s["CheckJNI17CallObjectMethodAEP"] = CheckJNI17CallObjectMethodAEP
s["CheckJNI17CallObjectMethodVEP"] = CheckJNI17CallObjectMethodVEP
s["CheckJNI22CallStaticObjectMethodEP"] = CheckJNI22CallStaticObjectMethodEP
s["CheckJNI23CallStaticObjectMethodAEP"] = CheckJNI23CallStaticObjectMethodAEP
s["CheckJNI23CallStaticObjectMethodVEP"] = CheckJNI23CallStaticObjectMethodVEP
s["_ZN3art3JNI11GetMethodID"] = _ZN3art3JNI11GetMethodID
s["_ZN3art3JNI17GetStaticMethodID"] = _ZN3art3JNI17GetStaticMethodID
s["SYSTEM_PATH"] = SYSTEM_PATH
s["TYPE_I"] = TYPE_I
s["TYPE_Z"] = TYPE_Z
s["TYPE_B"] = TYPE_B
s["TYPE_C"] = TYPE_C
s["TYPE_S"] = TYPE_S
s["TYPE_J"] = TYPE_J
s["TYPE_F"] = TYPE_F
s["TYPE_D"] = TYPE_D
s["TYPE_V"] = TYPE_V
s["FLOAT_CLS"] = FLOAT_CLS
s["METHOD_INIT"] = METHOD_INIT
s["RESULT_F"] = RESULT_F
s["DOUBLE_CLS"] = DOUBLE_CLS
s["RESULT_D"] = RESULT_D
s["LIB_64"] = LIB_64
a = set(''.join(list(s.values())))
a.add("\\0")
print(a)
for ch in list(a):
    if ch == '\\0':
        for key, value in s.items():
            print("%s[%d]=" % (key, len(value)), end=' ')
        print("'\\0';")
        continue
    for key, value in s.items():
        v_length = len(value)
        index = 0
        while True:
            index = value.find(ch, index, v_length)
            if index == -1: break
            print("%s[%d]=" % (key, index), end=' ')
            index += 1
    print("'%s';" % ch)

for key, value in s.items():
    print('ALOGE("%s====>%s", %s);' % (key, "%s", key))
