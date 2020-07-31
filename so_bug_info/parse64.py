import os

so_path = r"E:\game_plugin\game\xzys\build\outputs\apk\debug\libmod.so"
so_path = r"C:\Users\kenki\Documents\AndroidStudio\DeviceExplorer\xiaomi-redmi_7-fa0dbb5\data\data\com.kenkieo.app\plugin_0\data\com.lion.market\user\app_e_qq_com_plugin_c6370ecf7438999ba1a2ebb0ba0326fb\libturingau.3f9dd580.so"
so_path = r"H:\VA\com.glu.flc2_3.0.3\lib\armeabi-v7a\libunity.so"
so_path = r"E:\mm\h5youxi\H5Test\build\intermediates\transforms\mergeJniLibs\debug\0\lib\arm64-v8a\libmod.so"
so_path = r"E:\mm\android_2020\hook_test\so\arm64-v8a\libfixArt.so"
so_path = r"H:\aa\libart64.so"


def parse_64_so():
    addr2line_64 = r'D:\work\IDE\android-ndk-r16b-windows-x86_64\android-ndk-r16b\toolchains\aarch64-linux-android-4.9\prebuilt\windows-x86_64\bin\aarch64-linux-android-addr2line.exe'
    cmd = [addr2line_64, "-C", "-f", "-e", so_path, "00000000003c60fc"]
    b = os.popen(' '.join(cmd))
    text2 = b.read()
    print(text2)
    b.close()


parse_64_so()
