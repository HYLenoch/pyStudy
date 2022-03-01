# 爬虫门外汉

import requests

url = "https://c.it211.com.cn/aid21091008am/aid21091008am-250.ts"
headers = {"Referer": "https://tts.tmooc.cn/",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}

req = requests.get(url=url, headers=headers)

print(req)
print(req.text)
