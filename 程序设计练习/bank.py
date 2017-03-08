# coding:utf-8

import requests
import sys
import json
import time

reload(sys)
sys.setdefaultencoding('utf-8')

headers = {'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3', 'Host': 'bank.wo.cn', 'Accept': 'application/json', 'Referer': 'http://bank.wo.cn/jx/person', 'Connection': 'keep-alive', 'X-Requested-With': 'XMLHttpRequest', 'Cookie': '__c=FXOX; __i=1vbqNAGIXabHUtSZVHt5Y/Apsl2EQnTj; __u=15565307605; __t=1475645883771; __f="{"total":4084006.62,"used":144146}"', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0'}


def share():
    output = "\n"
    # 微信分享
    wechat = requests.get("http://bank.wo.cn/jx/share?type=weichat", headers=headers).json()
    output += "微信分享: %s \n" % wechat["message"]
    # 微博分享
    weibo = requests.get("http://bank.wo.cn/jx/share?type=weibo", headers=headers).json()
    output += "微博分享: %s \n" % weibo["message"]
    qiandao = requests.post("http://bank.wo.cn/jx/signIn", headers=headers).json()
    output += "签到：%s \n" % qiandao["message"]
    s = open("game.log", "a")
    s.write(output)
    s.close()


def game():
    output = "\n"
    n = int(requests.get("http://bank.wo.cn/jx/game/getAvailableGameNum", headers=headers).json()["message"])
    zong = n
    while n > 0:
        n -= 1
        resualt = requests.get("http://bank.wo.cn/jx/game/play?type=running", headers=headers).json()
        if str(resualt["data"]["win"]) == "true":
            output += "中奖了：\n" % str(resualt["data"]["prizeName"])
    s = open("game.log", "a")
    s.write(output)
    s.write("共抽奖 %s 次\n" % zong)
    s.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    s.close()

share()
game()




