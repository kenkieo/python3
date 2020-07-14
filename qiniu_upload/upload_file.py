# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth, put_file, etag

# 需要填写你的 Access Key 和 Secret Key
access_key = 'O98cyLYXwSzsky-PYfERQPqYXtSGNtGQIayHNRi-'
secret_key = 'OZctQQS4P-YLMcpwAmOW6nKwWn-XlwffPbUj6FyC'
# 构建鉴权对象
q = Auth(access_key, secret_key)


def upload_file(bucket_name, key, local_path, callback, **kwargs):
    token = q.upload_token(bucket_name, key, 3600)
    localfile = local_path
    ret, info = put_file(token, key, localfile)
    print(ret, info)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)
    if callback:
        callback(bucket_name, key, **kwargs)


# http://qiniu2.kaniang.com//djxyx/a.jpg
# http://qiniu2.kaniang.com//djxyx/b.png
if __name__ == "__main__":
    upload_file("kaniang",
                "djxyx/b.png",
                r"F:\android\MyApplication\app\src\main\res\mipmap-xxxhdpi\\ic_launcher.png",
                None)
