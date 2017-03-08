# coding:utf-8

import requests
import sys
import json


reload(sys)
sys.setdefaultencoding('utf-8')

USER_NAME = 'mpb159753@outlook.com'
USER_TOKEN = '0c5badb70b5ba17577dbafc9999eb6c7'

zone_url = "https://api.luadns.com/v1/zones/"

# zone = requests.get(zone_url, auth=requests.auth.HTTPBasicAuth(USER_NAME, USER_TOKEN),
#                     headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
url_id = 39286

data = {"name": 'mpbo.tk', "type": 'TXT', "content": "q.mpbo.tk", "zone_id": 39286, "ttl": 600}
# re_list = requests.get(zone_url+str(url_id), auth=requests.auth.HTTPBasicAuth(USER_NAME, USER_TOKEN),
#                        headers={'Content-Type': 'application/json', 'Accept': 'application/json'}).json()
# print re_list
create_url = "https://api.luadns.com/v1/zones/39286/records"
create_result = requests.post(create_url, data=data, auth=requests.auth.HTTPBasicAuth(USER_NAME, USER_TOKEN),
                              headers={'Content-Type': 'application/json', 'Accept': 'application/json'}
                              ).json()
print create_result



