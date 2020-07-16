from qiniu_upload.djxyx.djxyx_sql.table_game_info import game_info, GAME_INFO_TABLE, GAME_INFO_COLUMNS
from qiniu_upload.upload_file import upload_file
import os
from hashlib import md5
import requests

md5__ = md5()
BUCKET_NAME = "kaniang"
DOWN_URL_FORMAT = "http://qiniu2.kaniang.com//%s"


def upload_zip():
    for root, dirs, files in os.walk(r"F:\BaiduNetdiskDownload\djxyx"):
        for file in files:
            file_path = os.path.join(root, file)
            md5__.update(file.encode())
            md5_str = md5__.hexdigest()
            key = "djxyx/%s/game.zip" % md5_str
            file_size = os.path.getsize(file_path)
            upload_file(BUCKET_NAME, key, file_path, call_back,
                        md5_str=md5_str, file_size=file_size, name=os.path.splitext(file)[0])


def call_back(bucket_name, key, **kwargs):
    down_url = DOWN_URL_FORMAT % key
    md5_str = kwargs['md5_str']
    file_size = kwargs['file_size']
    name = kwargs['name']
    print(down_url, md5_str, file_size, name)
    game_info.insert_down_url(down_url, md5_str, file_size, name)


zone = "api-z2.qiniu.com"
request_url = "https://%s/sisyphus/fetch" % zone


if __name__ == '__main__':
    upload_zip()
