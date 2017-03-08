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
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; MX4 Pro Build/LMY48W) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.124 Mobile Safari/537.36; unicom{version:android@5.0,desmobile:15565307605}',
    'Referer': 'http://m.client.10010.com/mobileService/lightCandlesFlow/lightCandlesMain.htm',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,en-US;q=0.8',
    'Cookie': 'req_mobile=15565307605; clientid=98|0; JSESSIONID=2BJyYl8TpwnfN41zvqvt3GCQ4PpKnFDJdL'
              'X2dpbyncjvC5fZ7C9H!842952170; c_mobile=15565307605; c_sfbm=234g_00; mobileService=KTy'
              'VYl8TGSVNClSz9GYcrndrTFnvnDzdvcVNBxvhSJPBsLlLQ8k0!-1321509310; cw_mutual=6ff66a046d4'
              'cb9a67af6f2af5f74c3219bd8879340040c6928cc2a54434fa8dfadeda18edacafc209cc78984223664f0'
              '194b78f2c38df1dec578c530be75b495; route=23c92c32fb62d6a8c0767d732f99d205; a_token=eyJ'
              '0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJleHAiOjE0ODM2Njc5MDcsInRva2VuIjp7ImxvZ2luVXNlciI'
              '6IjE1NTY1MzA3NjA1IiwicmFuZG9tU3RyIjoieWhsUTBhcmIxNDgzMDYzMTA3ODA5In0sImlhdCI6MTQ4MzA2'
              'MzEwN30.KN8mpzI-3n4zcS5cZcknZxwnkG9SnxMDVFKd1xIR8hqRrrSlcydisluM6FhVbBFx-kCsL1xzZ_N37Y'
              'mXsSA0UA; req_serial=16071212435610826936; SigninApp=QTQsYK0FJk9Xv3JLcKHBNp1y3JgT2jy5x'
              'FvJRPhGn0JF8yx2DvJ7!-950270145; u_type=01; u_account=15565307605; req_wheel=ssss; wo_f'
              'amily=2; c_id=87363461a93b201af477e87021ea5e998febcd250b43d2a52ab908c3c0c3aa5b; c_vers'
              'ion=android@5.0; t3_token=815552ce052842949275cdabc9214966; c_stroe_version=android@5.'
              '0; mallcity=76|110; gipgeo=76|765; CaptchaCode=zXijqC3DUK6YGB5a3M6Z8obWBUgyJ742ge84LcK'
              'Raac=; MUT_V=android%405.0; _n3fa_cid=8778ae7692474fbfb77eb02465fc1062; _n3fa_ext=ft=1'
              '476183021; _n3fa_lvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1481274315,1481421542,148211353'
              '3,1483062940; _n3fa_lpvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1483062940; WT_FPC=id=2811b1'
              '97f3d170bc6441483062941902:lv=1483062941930:ss=1483062941902; SHOP_PROV_CITY=; city=07'
              '6|110; MUT_S=android5.1.1; c_sfbm=234g_00}'
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


