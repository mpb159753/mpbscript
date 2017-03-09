# coding:utf-8

import requests
import sys
import json
import time

reload(sys)
sys.setdefaultencoding('utf-8')

headers = {}

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




