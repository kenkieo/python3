string = """
{"code":200,"msg":"成功","data":{"gameCenterType":2,"gameCenterVersion":"1.0.8","gameCenterID":0,"gameCenterData":[{"id":115629003,"name":"游戏分类","min_name":"","compact":8,"styleCode":"category","showmore":1,"icon":"http:\/\/dl3.mgc-games.com\/access\/upload\/20190925\/5d8adada6c26b.png","bg_pic":"","coins":100,"color_start":"","color_end":"","showtitle":1,"coins_icon":"http:\/\/dl3.mgc-games.com\/access\/upload\/44jinbi.png","highrewardcoin":0,"rewardcoefficient":1,"rankList":[],"gameList":[],"signList":[],"categoryList":[{"id":55717,"name":"休闲游戏","icon":"http:\/\/dl3.mgc-games.com\/access\/upload\/20190923\/5d881a91d9a98.png"},{"id":55721,"name":"益智游戏","icon":"http:\/\/dl3.mgc-games.com\/access\/upload\/20190923\/5d881afea8343.png"},{"id":55718,"name":"角色扮演","icon":"http:\/\/dl3.mgc-games.com\/access\/upload\/20190923\/5d881ac766d2c.png"},{"id":55714,"name":"创意游戏","icon":"http:\/\/dl3.mgc-games.com\/access\/upload\/20190923\/5d881a4e1949a.png"},{"id":55720,"name":"解谜游戏","icon":"http:\/\/dl3.mgc-games.com\/access\/upload\/20190923\/5d887f1a002c2.png"},{"id":55719,"name":"策略游戏","icon":"http:\/\/dl3.mgc-games.com\/access\/upload\/20190923\/5d887f0ec9229.png"},{"id":55716,"name":"最新上架","icon":"http:\/\/dl3.mgc-games.com\/access\/upload\/20190923\/5d881a873b0c0.png"},{"id":55715,"name":"朋友热玩","icon":"http:\/\/dl3.mgc-games.com\/access\/upload\/20190923\/5d881a7d66343.png"},{"id":55724,"name":"竞技游戏","icon":"http:\/\/dl3.mgc-games.com\/access\/upload\/20190925\/5d8ae1bfd5870.png"},{"id":55728,"name":"模拟养成","icon":"http:\/\/dl3.mgc-games.com\/access\/upload\/20190925\/5d8ae1fb78e51.png"},{"id":55725,"name":"跑酷游戏","icon":"http:\/\/dl3.mgc-games.com\/access\/upload\/20190925\/5d8ae23a50ba6.png"},{"id":55723,"name":"棋牌游戏","icon":"http:\/\/dl3.mgc-games.com\/access\/upload\/20190925\/5d8ae15a76909.png"},{"id":55730,"name":"放置游戏","icon":"http:\/\/dl3.mgc-games.com\/access\/upload\/20190925\/5d8ae20e71f60.png"},{"id":55727,"name":"射击游戏","icon":"http:\/\/dl3.mgc-games.com\/access\/upload\/20190925\/5d8ae217b2df7.png"},{"id":55729,"name":"体育游戏","icon":"http:\/\/dl3.mgc-games.com\/access\/upload\/20190925\/5d8ae20693b69.png"},{"id":55726,"name":"赛车游戏","icon":"http:\/\/dl3.mgc-games.com\/access\/upload\/20190925\/5d8ae22ca918b.png"}]}],"myGamePosition":3}}
"""

from urllib import request
import json
from qiniu_upload.djxyx.djxyx_sql import session
from qiniu_upload.djxyx.djxyx_sql import CategoryInfo


def parse_category():
    json_result = json.loads(string)
    data = json_result["data"]
    gameCenterData = data["gameCenterData"]
    for gameCenterItem in gameCenterData:
        categoryList = gameCenterItem["categoryList"]
        for category_item in categoryList:
            request_category_item_game(category_item)


def request_category_item_game(category_item):
    id = category_item["id"]
    name = category_item["name"]
    category = CategoryInfo()
    category.id = id
    category.name = name
    session.add(category)
    session.commit()


def request_category_item_game_page(lid, page):
    url = "http://search.mgc-games.com:8711/api/v7/charge/more?" \
          "lid=%d" \
          "&offset=10" \
          "&open_token=0023a78e02fb489528a99b7f9cb39ec" \
          "&page=%d" \
          "&tid=115629003" \
          "&agentgame=" \
          "&app_id=1000830" \
          "&channel_id=1000830" \
          "&client_id=334" \
          "&device_md5=313934D21A7D1BBDF3A0615C348691DC" \
          "&framework_version=3.1.7" \
          "&from=11" \
          "&leto_version=android_v3.8.5" \
          "&packagename=com.djxyx.ht01" \
          "&timestamp=0" \
          "&user_token=dFTpZ0xQMjDUNxy2bOm2lnoAYKWs0u37Y9nARSh5MkjehostaRDEN9kyNymItBwEZ2jkAxO0O0OK" % \
          (
              lid, page
          )
    response = request.urlopen(url)
    content = response.read().decode()
    json_result = json.loads(content)
    data = json_result.get("data")
    if data:
        for game_item in data:
            id = game_item["id"]
            name = game_item["name"]
            icon = game_item["icon"]
            packageurl = game_item["packageurl"]
            version = game_item["version"]
            deviceOrientation = game_item["portrait"]
            tags = game_item["tags"]
            publicity = game_item["publicity"]


if __name__ == "__main__":
    parse_category()
    # request_category_item_game_page(55714, 1)

# GET http://search.mgc-games.com:8711/api/v7/charge/more
# ?lid=55714
# &offset=10
# &open_token=0023a78e02fb489528a99b7f9cb39ec&page=1&tid=115629003&agentgame=&app_id=1000830&channel_id=1000830&client_id=334&device_md5=313934D21A7D1BBDF3A0615C348691DC&framework_version=3.1.7&from=11&leto_version=android_v3.8.5&packagename=com.djxyx.ht01&timestamp=0&user_token=dFTpZ0xQMjDUNxy2bOm2lnoAYKWs0u37Y9nARSh5MkjehostaRDEN9kyNymItBwEZ2jkAxO0O0OK HTTP/1.1
# Accept-Encoding: identity
# User-Agent: Dalvik/2.1.0 (Linux; U; Android 9; Redmi 7 MIUI/V10.3.2.0.PFLCNXM)
# Host: search.mgc-games.com:8711
# Connection: Keep-Alive
# GET http://search.mgc-games.com:8711/api/v7/charge/more?lid=55717&offset=10&open_token=0023a78e02fb489528a99b7f9cb39ec&page=2&tid=115629003&agentgame=&app_id=1000830&channel_id=1000830&client_id=334&device_md5=313934D21A7D1BBDF3A0615C348691DC&framework_version=3.1.7&from=11&leto_version=android_v3.8.5&packagename=com.djxyx.ht01&timestamp=0&user_token=dFTpZ0xQMjDUNxy2bOm2lnoAYKWs0u37Y9nARSh5MkjehostaRDEN9kyNymItBwEZ2jkAxO0O0OK HTTP/1.1
# Accept-Encoding: identity
# User-Agent: Dalvik/2.1.0 (Linux; U; Android 9; Redmi 7 MIUI/V10.3.2.0.PFLCNXM)
# Host: search.mgc-games.com:8711
# Connection: Keep-Alive
