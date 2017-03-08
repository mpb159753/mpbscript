# coding:utf-8

import requests
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')

S = requests.Session()

url = 'http://www.wndflb.com/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LI77F&mobile=yes'
log_data = {'answer': '', 'fastloginfield': 'username', 'password': 'flb.MPB159753', 'questionid': '0',
            'referer': 'http://www.wndflb.com/forum.php?mobile=1', 'submit': '登录', 'username': '看我72遍'}

log = S.post(url, data=log_data)
index = S.get('http://www.wndflb.com/forum.php?mobile=1')
print index.text

