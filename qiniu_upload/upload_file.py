# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth, put_file, etag
import requests

# 需要填写你的 Access Key 和 Secret Key
from qiniu.services.storage.bucket import BucketManager

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


def sync_url(url, bucket_name, key):
    print("sync_url", url, bucket_name, key)
    bucket = BucketManager(q)
    ret, info = bucket.fetch(url, bucket_name, key)
    print(info)
    assert ret['key'] == key


if __name__ == "__main__":
    zone = "api-z2.qiniu.com"
    request_url = "https://%s/sisyphus/fetch" % zone
    url = "http://dl3.mgc-games.com/sdkgame/1000880/The king of Archers_pack.zip"
    key = "2204114da4362fd4fb56ccbf3f3c14e9/game.zip"
    sync_url(url, "kaniang", key)
