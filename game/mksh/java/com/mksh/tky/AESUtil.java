package com.mksh.tky;

import android.util.Base64;

import java.security.Provider;
import java.security.Security;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class AESUtil {
    public static byte[] AES128Encode(byte[] bArr, byte[] bArr2) throws Throwable {
        SecretKeySpec secretKeySpec = new SecretKeySpec(bArr, "AES");
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("AES");
        stringBuilder.append("/EC");
        stringBuilder.append("B/PKCS7P");
        stringBuilder.append("adding");
        Cipher cipher = getCipher(stringBuilder.toString(), "BC");
        cipher.init(1, secretKeySpec);
        byte[] bArr3 = new byte[cipher.getOutputSize(bArr2.length)];
        cipher.doFinal(bArr3, cipher.update(bArr2, 0, bArr2.length, bArr3, 0));
        return bArr3;
    }

    public static String AES128Decode(String str, byte[] bArr) throws Throwable {
        return (str == null || bArr == null) ? null : new String(AES128Decode(str.getBytes("UTF-8"), bArr), "UTF-8");
    }

    public static byte[] AES128Decode(byte[] bArr, byte[] bArr2) throws Throwable {
        if (bArr == null || bArr2 == null) {
            return null;
        }
        byte[] bArr3 = new byte[16];
        System.arraycopy(bArr, 0, bArr3, 0, Math.min(bArr.length, 16));
        SecretKeySpec secretKeySpec = new SecretKeySpec(bArr3, "AES");
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("AES");
        stringBuilder.append("/EC");
        stringBuilder.append("B/NoP");
        stringBuilder.append("adding");
        Cipher cipher = getCipher(stringBuilder.toString(), "BC");
        cipher.init(2, secretKeySpec);
        bArr = new byte[cipher.getOutputSize(bArr2.length)];
        cipher.doFinal(bArr, cipher.update(bArr2, 0, bArr2.length, bArr, 0));
        return bArr;
    }

    private static Cipher getCipher(String str, String name) throws Throwable {
        Cipher cipher = null;
        if (!TextUtils.isEmpty(name)) {
            try {
                Provider provider = Security.getProvider(name);
                if (provider != null) {
                    cipher = Cipher.getInstance(str, provider);
                }
            } catch (Throwable unused) {
            }
        }
        return cipher == null ? Cipher.getInstance(str, name) : cipher;
    }

}
