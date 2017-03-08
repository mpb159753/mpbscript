# coding:utf-8

import requests
import sys
import json
import re
import top.api
import time


reload(sys)
sys.setdefaultencoding('utf-8')


def send_msg(number, text, way, code):
    appkey = 23287812
    secret = "dce59b35c0d47b9c058931b86d217262"

    if way == "call":
        req = top.api.AlibabaAliqinFcVoiceNumSinglecallRequest()
        req.set_app_info(top.appinfo(appkey, secret))

        req.extend = ""
        req.called_num = number
        req.called_show_num = "051482043272"
        req.voice_code = code
        try:
            resp = req.getResponse()
            print (resp)
        except Exception, e:
            print (e)
    elif way == "call_msg":
        req = top.api.AlibabaAliqinFcTtsNumSinglecallRequest()
        req.set_app_info(top.appinfo(appkey, secret))

        req.extend = ""
        req.tts_param = text
        req.called_num = number
        req.called_show_num = "051482043272"
        req.tts_code = code
        try:
            resp = req.getResponse()
            print (resp)
        except Exception, e:
            print (e)
    elif way == "text":
        req = top.api.AlibabaAliqinFcSmsNumSendRequest()
        req.set_app_info(top.appinfo(appkey, secret))

        req.extend = ""
        req.sms_type = "normal"
        req.sms_free_sign_name = "MPB最帅~"
        req.sms_param = json.dumps(text)
        req.rec_num = number
        req.sms_template_code = code
        try:
            resp = req.getResponse()
            print (resp)
        except Exception, e:
            print (e)


def amazon(name, lowest, original, url):
    headers = {'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3', 'Host': 'www.amazon.com',
               'Accept': 'text/html,*/*', 'Referer': 'https://www.amazon.com/gp/product/B00AVSEVG0/',
               'Connection': 'keep-alive', 'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'}
    price_page = requests.get(url, headers=headers)
    q = price_page.text.replace('\n', '')
    q = q.replace('\\n', '')
    q = q.replace('\\r', '')
    w = re.findall('<span id="priceblock_ourprice".*?span', q)

    price = re.findall(">.*?<", w[0])[0][1:-1]

    text = price
    ss = float(price[1:])

    # log = open("/home/wwwroot/default/1.html", "a")
    if ss < original:
        write_log = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " " + name + '降低了$' + str(original-ss) + '当前价格' + text
    elif ss > original:
        write_log = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " " + name + '升高了$' + str(ss-original) + '当前价格' + text
    else:
        write_log = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " " + name + ' ' + text

    # log.write("<h2>" + write_log + "</h2>")
    # log.close()
    print text
    if ss < lowest:
        print "send_msg"
        send_msg(15565307605, {"time": name, "statue": text}, 'text', "SMS_27140001")
        return ss
    else:
        return ss

# tem = open("/home/wwwroot/default/1.html", "w")
# tem.close()

goods = [{'name': 'Osprey Radial 34', "want_price": 70, "original_price":  179.00, "latest_price": 179.00,
          "url": 'https://www.amazon.com/gp/product/B019TSRYXY/ref=ox_sc_sfl_title_2?ie=UTF8&psc=1&smid=ATVPDKIKX0DER'},
         {'name': 'Osprey Farpoint 40', "want_price": 70, "original_price":  127.13, "latest_price": 179.00,
          "url": 'https://www.amazon.com/gp/product/B014EBM3KA/ref=ox_sc_sfl_title_1?ie=UTF8&psc=1&smid=ATVPDKIKX0DER'},
         {'name': 'Jack Wolfskin 阿尔卑斯', "want_price": 25, "original_price":  83.37,  "latest_price": 179.00,
          "url": 'https://www.amazon.com/gp/product/B019FIFSS6/ref=ox_sc_act_title_1?ie=UTF8&psc=1&smid=ATVPDKIKX0DER'},
         ]
# amazon_list = open('amazon_list.txt', 'r')
# goods = json.loads(amazon_list.read())
# amazon_list.close()
total = 0
for i in goods:
    price = amazon(i['name'], i["want_price"], i["original_price"], i["url"])
    i["want_price"] = price - 0.5
amazon_list = open('amazon_list.txt', 'w')
amazon_list.write(json.dumps(goods))
amazon_list.close()
# tem = open("/home/wwwroot/default/1.html", "a")
# tem.write("<h2>总价： " + str(total) + "</h2>")
# tem.close()
