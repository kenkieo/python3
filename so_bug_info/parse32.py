import os

so_path = r"E:\cc_work\gam_emu\cc_vritual2\VirtualApp\virtual_lib\build\intermediates\transforms\stripDebugSymbol\debug\0\lib\armeabi-v7a\libv++.so"
so_path = r'E:\mm\android_2020\hook_test\build\intermediates\transforms\stripDebugSymbol\debug\0\lib\armeabi-v7a\libmod.so'

def parse_32_so():
    addr2line_32 = r'D:\work\IDE\android-ndk-r16b-windows-x86_64\android-ndk-r16b\toolchains\arm-linux-androideabi-4.9\prebuilt\windows-x86_64\bin\arm-linux-androideabi-addr2line.exe'
    cmd = [addr2line_32, "-C", "-f", "-e", so_path, "00007df5"]
    b = os.popen(' '.join(cmd))
    text2 = b.read()
    # datadiv_decode2718463688705622909
    # datadiv_decode2718463688705622909
    # datadiv_decode2718463688705622909
    print(text2)
    b.close()


parse_32_so()
