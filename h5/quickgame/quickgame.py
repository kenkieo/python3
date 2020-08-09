import requests
import time

# versionCode: '120001'
# versionName: 1.2.1
response = requests.get("https://config.quickgame.top/check.json",
                        params={
                            "version": "1.2.1",
                            "t": int(time.time()) * 1000,
                        }
                        )
print(response.content.decode())
