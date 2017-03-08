# coding:utf-8

import requests
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')

S = requests.Session()
userName = 18539007605
password = 159753

log_data = {'_': time.time(), 'password': password, 'callback': 'jQuery17206215443899268148_1470992690258',
            'productType': '01', 'pwdType': '01', 'redirectType': '03', 'req_time': time.time(),
            'redirectURL': 'http://www.10010.com', 'rememberMe': '1', 'userName': userName}

log = S.get('https://uac.10010.com/portal/Service/MallLogin', params=log_data)
no_idea = S.post('http://iservice.10010.com/e3/static/common/l?_=' + str(time.time()))

qiandao_url = 'http://iservice.10010.com/e3/static/transact/signIn/ajax_yy_signIn?_=' + str(time.time())

qiandao = S.post(qiandao_url, data={'_': str(time.time())})
response = qiandao.json()
print response
if response["respCode"] == '0000':
    print response["signDays"]
else:
    print response["respCode"]
    print response["signDays"]

