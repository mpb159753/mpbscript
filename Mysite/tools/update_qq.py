# encoding: utf-8

import requests
import re
import json
import os
import datetime
from bs4 import BeautifulSoup
import ConfigParser


def test():
    page = 1
    download_page = "http://dyn.v.ifeng.com/cmpp/video_msg_ipad.js"
    go_on = True
    while go_on:
        index_page = "http://v.ifeng.com/vlist/tv/qqsrx/all/0/%s/detail.shtml" % page
        current_page = requests.get(index_page).text
        video_list = BeautifulSoup(current_page, 'lxml').find_all('div', class_='pic')
        for i in video_list:
            try:
                date = i.find('span', class_="sets").string
                if True:
                    print i.find('span', class_="sets").string
                    page_url = i.a["href"]
                    video_id = re.findall('\d/(.*?).shtml', page_url)[0]
                    print json.loads(requests.get(download_page, params={'msg': video_id}).text[3:-6])["videoplayurl"]
                    print i.a["title"][1:]
                else:
                    go_on = False
                    break
            except:
                continue
        page += 1
        if page > 2:
            break

def chushihua():
    # qq_json = json.loads(open('999.json', 'r').read())
    # for i in qq_json["videos"]:
    #     print i["date"][0]
    #     print i["link"]
    #     print i["download_link"]
    #     print i["title"]

    main_page = requests.get("http://v.youku.com/v_show/id_XMTc3NDMxMjM2MA==.html").text

    # video_list = BeautifulSoup(main_page, "lxml").find_all("div", cseq="1")
    video_list = BeautifulSoup(main_page, "lxml").find_all("div", cseq="1")
    video_list.reverse()

    for i in video_list:
        date = "%s-%s-%s" % (i["title"][-8:-4], i["title"][-4:-2], i["title"][-2:])
        print date
        print i["title"][:-9]
        print "http:"+i.a["href"]
        # add = DWT(title=i["title"][:-9], show="YZP", date=date, page_url="http:"+i.a["href"])
        # add.save()


def file_manager():
    now_time = datetime.datetime.now()
    file_list = os.walk("/root/123")
    for root, dirs, files in file_list:
        for name in files:
            file_full_path = os.path.join(root, name)
            file_time = datetime.datetime.fromtimestamp(os.path.getctime(file_full_path))
            if (now_time - file_time).seconds > 100:
                os.remove(file_full_path)
                print file_full_path
        for name in dirs:
            dir_full_path =os.path.join(root, name)
            file_time = datetime.datetime.fromtimestamp(os.path.getctime(dir_full_path))
            if (now_time - file_time).seconds > 100:
                try:
                    os.rmdir(dir_full_path)
                    print dir_full_path
                except OSError:
                    pass


def update():
    """
    当前日期若是视频更新日，则从数据库调取各个视频最新的一期日期，如果不符则开始更新，并将最新存入数据库
    :return:
    """

    qqsrx_upday = ([2, 3, 4, 5, 6])  # 锵锵三人行周二至周六更新
    yzp_upday = ([3, 5])  # 圆桌派周三，周五更新
    today_weekday = datetime.datetime.now().weekday()
    today = datetime.datetime.now().strftime('%Y-%m-%d')

    if today_weekday in yzp_upday:
        main_page = requests.get("http://v.youku.com/v_show/id_XMjQ4MzI5MjUwNA==.html").text
        video_list = BeautifulSoup(main_page, "lxml").find_all("li", class_="item")
        for i in video_list:
            if u"[完整版]" == i["title"][:5]:
                date = "%s-%s-%s" % (i["title"][-8:-4], i["title"][-4:-2], i["title"][-2:])

                print "http:"+i.a["href"]


update()