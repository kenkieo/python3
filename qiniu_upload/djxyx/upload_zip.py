from qiniu_upload.djxyx.djxyx_sql import query_versionInfo
from qiniu_upload.djxyx.djxyx_sql import query_GameInfo2VersionInfo
from qiniu_upload.djxyx.djxyx_sql import queryGameInfo
from qiniu_upload.djxyx.djxyx_sql import insert_data2Qiniu
from qiniu_upload.djxyx.djxyx_sql import query_data2Qiniu
from qiniu_upload.upload_file import sync_url

BUCKET_NAME = "kaniang"
DOWN_URL_FORMAT = "http://qiniu2.kaniang.com//%s"


# def upload_zip():
#     for root, dirs, files in os.walk(r"F:\BaiduNetdiskDownload\djxyx"):
#         for file in files:
#             file_path = os.path.join(root, file)
#             md5__.update(file.encode())
#             md5_str = md5__.hexdigest()
#             key = "djxyx/%s/game.zip" % md5_str
#             file_size = os.path.getsize(file_path)
#             upload_file(BUCKET_NAME, key, file_path, call_back,
#                         md5_str=md5_str, file_size=file_size, name=os.path.splitext(file)[0])
#
#
# def call_back(bucket_name, key, **kwargs):
#     down_url = DOWN_URL_FORMAT % key
#     md5_str = kwargs['md5_str']
#     file_size = kwargs['file_size']
#     name = kwargs['name']
#     print(down_url, md5_str, file_size, name)
#

def sync_djxyx():
    versionList = query_versionInfo()
    for versionInfo in versionList:
        if query_data2Qiniu(versionInfo.id):
            continue
        gameInfo2VersionInfo = query_GameInfo2VersionInfo(versionInfo.id)
        if gameInfo2VersionInfo:
            gameInfo = queryGameInfo(gameInfo2VersionInfo.gameId)
            if gameInfo:
                key = "%s/icon.png" % gameInfo.md5
                icon = "http://qiniu2.kaniang.com/%s" % key
                try:
                    sync_url(gameInfo.icon, BUCKET_NAME, key)
                except:
                    icon = ""
                key = "%s/game.zip" % gameInfo.md5
                url = "http://qiniu2.kaniang.com/%s" % key
                try:
                    sync_url(versionInfo.url, BUCKET_NAME, "%s/game.zip" % gameInfo.md5)
                except:
                    url = ""
                insert_data2Qiniu(versionInfo.id, url, icon)


if __name__ == '__main__':
    sync_djxyx()
