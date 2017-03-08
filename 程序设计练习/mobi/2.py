# coding:utf-8

import requests
import sys
import time
import re
import json
import html2text

reload(sys)
sys.setdefaultencoding('utf-8')


sa = open('888.json', 'r').read()
qlist = json.loads(sa)
new =[]
title = []
juan = 1
zong_zhang = 0
wlist = {"第一卷": [], "第二卷": [], "第三卷": [], "第四卷": [], "第五卷": [], "第六卷": [] }
for i in qlist:
    print i["Title"]
    zhang_input = raw_input("总章: ")
    if zhang_input == '':
        zong_zhang += 1
    else:
        zong_zhang = int(zhang_input)
    i["Zong_Zhang"] = zong_zhang

    juan = zong_zhang

    i["Zhang"] = zong_zhang % 12
    if i["Zhang"] == 0:
        i["Juan"] = zong_zhang / 12
        i["Zhang"] = 12
    else:
        i["Juan"] = (zong_zhang / 12) + 1

    print i["Juan"]
    print i["Zhang"]

sw = open('888.json', 'w')
sw.write(json.dumps(wlist))
sw.close()


