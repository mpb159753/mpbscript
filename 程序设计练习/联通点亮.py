# coding:utf-8

import requests
import sys
import json
import time

reload(sys)
sys.setdefaultencoding('utf-8')

header = {
    'Host': 'm.client.10010.com', 'Proxy-Connection': 'keep-alive', 'Content-Length': '0',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'http://m.client.10010.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; MX4 Pro Build/LMY48W) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.124 Mobile Safari/537.36; unicom{version:android@5.0,desmobile:}',
    'Referer': 'http://m.client.10010.com/mobileService/lightCandlesFlow/lightCandlesMain.htm',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,en-US;q=0.8',
    'Cookie': ''
}
url = 'http://m.client.10010.com/mobileService/lightCandlesFlow/businessTransact/lightCandlesSubmit.htm'
go_on = True
while go_on:
    result = requests.post(url, headers=header)
    try:
        if result.json()['count'] % 100 == 0:
            print '成功'
            go_on = False
        else:
            print result.json()['count']
            time.sleep(0.7)
    except:
        time.sleep(20.0)


