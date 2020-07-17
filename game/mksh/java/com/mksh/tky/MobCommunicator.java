package com.mksh.tky;

import java.io.BufferedOutputStream;
import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;
import java.math.BigInteger;
import java.util.HashMap;
import java.util.Random;
import java.util.zip.GZIPOutputStream;

import android.util.Base64;

public final class MobCommunicator implements PublicMemberKeeper {
	private Random a = new Random();
	private BigInteger b;
	private BigInteger c;
	private MobRSA d;

	public static class Callback<T> implements PublicMemberKeeper {
		public void onResultError(Throwable th) {
		}

		public void onResultOk(T t) {
		}
	}

	public static class NetworkError extends Exception implements PublicMemberKeeper {
		private static final long serialVersionUID = -8447657431687664787L;

		public NetworkError(String str) {
			super(str);
		}
	}

	public MobCommunicator(int i, String str, String str2) {
//		a 1024
//		b d008219b14c84872559aaf9e69d1348175289c186912da64b2393bab376bb0d6b471220cb29cbc9875b148b593eb9d7c4c359549a1aff22f6de9d18d22f0b6cb
//		c 1f228b2b8fbb7317674db20bab1d4b0f0ddb3e1f3a93177f1821c026ffd7c6b782be720a308ab69bf6c631c3c0c4d68bf9d92ddaaf712a032d591ba1c296df13332a23e37b281e5fd9b93ab016dd3efc5de45e264ed692ac63ac40013f507cd272b7aeeb85be9fe2f31f11b8c55d904b5331932c70c7cf3f2b05cb802f6b89a7
		this.d = new MobRSA(i);
		this.b = new BigInteger(str, 16);
		this.c = new BigInteger(str2, 16);
	}

	public void requestSynchronized(boolean z, HashMap<String, String> hashMap, String str, String str2, boolean z2)
			throws Throwable {
		byte[] a = a();
		String a2 = a(a, str, z2);
	}

	private byte[] a(byte[] bArr) throws Throwable {
		ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
		BufferedOutputStream bufferedOutputStream = new BufferedOutputStream(
				new GZIPOutputStream(byteArrayOutputStream));
		bufferedOutputStream.write(bArr);
		bufferedOutputStream.flush();
		bufferedOutputStream.close();
		return byteArrayOutputStream.toByteArray();
	}

	private byte[] a() throws Throwable {
		ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
		DataOutputStream dataOutputStream = new DataOutputStream(byteArrayOutputStream);
		this.a.setSeed(System.currentTimeMillis());
		dataOutputStream.writeLong(this.a.nextLong());
		dataOutputStream.writeLong(this.a.nextLong());
		dataOutputStream.flush();
		dataOutputStream.close();
		return byteArrayOutputStream.toByteArray();
	}

	private String a(byte[] bArr, String str, boolean z) throws Throwable {
		byte[] bytes = str.getBytes("utf-8");
		if (z) {
			bytes = a(bytes);
		}
		ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
		DataOutputStream dataOutputStream = new DataOutputStream(byteArrayOutputStream);
		byte[] encode = this.d.encode(bArr, this.b, this.c);
		dataOutputStream.writeInt(encode.length);
		dataOutputStream.write(encode);
		bArr = AESUtil.AES128Encode(bArr, bytes);
		dataOutputStream.writeInt(bArr.length);
		dataOutputStream.write(bArr);
		dataOutputStream.flush();
		dataOutputStream.close();
		return Base64.encodeToString(byteArrayOutputStream.toByteArray(), 2);
	}
}