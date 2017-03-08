# encoding: utf-8

import datetime
import requests
import re
import os
import json
import ConfigParser
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.db import models
from models import DWT
from django.core.context_processors import csrf
from django.http import HttpResponse


# Create your views here.
DOWNLOAD_PATH = "/root/123"


def update(request):
    """
    当前日期若是视频更新日，则从数据库调取各个视频最新的一期日期，如果不符则开始更新，并将最新存入数据库
    :return:
    """

    qqsrx_upday = ([2, 3, 4, 5, 6])  # 锵锵三人行周二至周六更新
    yzp_upday = ([3, 5])  # 圆桌派周三，周五更新
    today_weekday = datetime.datetime.now().weekday()
    today = datetime.datetime.now().strftime('%Y-%m-%d')

    if today_weekday in qqsrx_upday:
        newest = DWT.all().filter(show="QQSRX").reverse()[0]
        newest_date = str(newest.date)
        page = 1
        download_page = "http://dyn.v.ifeng.com/cmpp/video_msg_ipad.js"
        go_on = newest_date != today
        while go_on:
            index_page = "http://v.ifeng.com/vlist/tv/qqsrx/all/0/%s/detail.shtml" % page
            current_page = requests.get(index_page).text
            video_list = BeautifulSoup(current_page, 'lxml').find_all('div', class_='pic')
            for i in video_list:
                try:
                    date = i.find('span', class_="sets").string
                    if date != newest_date:
                        page_url = i.a["href"]
                        video_id = re.findall('\d/(.*?).shtml', page_url)[0]
                        add = DWT(show="QQSRX", title=i.a["title"][1:], date=date, page_url=page_url,
                                  video_url=json.loads(requests.get(download_page, params={'msg': video_id}).text[3:-6])["videoplayurl"])
                        add.save()
                    else:
                        go_on = False
                        break
                except:
                    continue
            page += 1
            if page > 5:
                break

    if today_weekday in yzp_upday:
        newest = DWT.objects.all().filter(show="YZP").reverse()[0]
        newest_date = str(newest.date)
        if newest_date != today:             # 最新的一期的日期与更新日日期不同，检查有无更新。
            main_page = requests.get("http://v.youku.com/v_show/id_XMTc3NDMxMjM2MA==.html").text
            video_list = BeautifulSoup(main_page, "lxml").find_all("div", cseq="1")
            for i in video_list:
                date = "%s-%s-%s" % (i["title"][-8:-4], i["title"][-4:-2], i["title"][-2:])
                if date != newest_date:   # 当前视频不在数据库中，则存入数据库。
                    add = DWT(title=i["title"][:-9], show="YZP", date=date, page_url="http:"+i.a["href"])
                    add.save()
                    downloader("http:"+i.a["href"], i["title"][:-9])
                else:
                    break


def chushihua(request):
    qq_json = json.loads(open('999.json', 'r').read())
    for i in qq_json["videos"]:
        add = DWT(title=i["title"], show="QQSRX", date=i["date"][0], page_url=i["link"], video_url=i["download_link"])
        add.save()

    main_page = requests.get("http://v.youku.com/v_show/id_XMTc3NDMxMjM2MA==.html").text
    # video_list = BeautifulSoup(main_page, "lxml").find_all("div", cseq="1")
    video_list = BeautifulSoup(main_page, "lxml").find_all("div", cseq="1")
    video_list.reverse()
    for i in video_list:
        date = "%s-%s-%s" % (i["title"][-8:-4], i["title"][-4:-2], i["title"][-2:])
        add = DWT(title=i["title"][:-9], show="YZP", date=date, page_url="http:"+i.a["href"])
        add.save()


def downloader(url, name):
    """
    调用 you-get 下载视频并转换为.mp4格式存入视频播放目录
    """
    download_command = "you-get -o %s --format=mp4 -O %s.mp4 %s" % (DOWNLOAD_PATH, name, url)
    print download_command
    os.system(download_command)
    return 0


def file_manager(request):
    now_time = datetime.datetime.now()
    file_list = os.walk(DOWNLOAD_PATH)
    for root, dirs, files in file_list:
        for name in files:
            file_full_path = os.path.join(root, name)
            file_time = datetime.datetime.fromtimestamp(os.path.getctime(file_full_path))
            if (now_time - file_time).seconds > 100:
                os.remove(file_full_path)
        for name in dirs:
            dir_full_path =os.path.join(root, name)
            file_time = datetime.datetime.fromtimestamp(os.path.getctime(dir_full_path))
            if (now_time - file_time).seconds > 100:
                try:
                    os.rmdir(dir_full_path)
                except OSError:
                    pass


def built_rss(douban_id):
    """
    获取豆瓣电影id, 通过 Feed43 提供服务制作 RSS 源
    :param douban_id:
    :return:
    """
    movie_url = "https://movie.douban.com/subject/%s/reviews" % douban_id
    # 将页面传入 BeautifulSoup 处理，找到带有电影名的 div, 处理有输出
    movie_name = "%s影评 (20)" % \
                 BeautifulSoup(requests.get(movie_url).text, 'lxml').find_all('div', class_="subject-title")[0].a.string[2:]

    # Feed43 处理所需参数
    reload_data = {
        "action": "get", "auth": "", "encoding": "utf-8", "name": "douban_movie",
        "url": movie_url}
    search_data = {"action": "search", "name": "douban_movie", "global_pattern": "", "auth": "",
                   "item_pattern": '<h3{*} href="{%}"{*}title-link">{%}</a{*}</h3>{*}'}
    build_data = {
        "action": "build", "auth": "", "feed_description": movie_name,
        "feed_link": movie_url, "feed_title": movie_name, "global_template": "",
        "item_link": "{%1}", "item_template": "", "item_title": "{%2}",
        "merge_items": "0", "name": "douban_movie"}

    up_url = "https://feed43.com/feed.html"
    # 提交给 Feed43 处理生产 RSS
    requests.post(up_url, data=reload_data)
    requests.post(up_url, data=search_data)
    requests.post(up_url, data=build_data)
    send_mobi("fullhttps://feed43.com/douban_movie.xml", username=movie_name)
    return 0


def send_mobi(*rss_urls, **configs):
    """
    根据传入设置生成 kindlereader 配置文件, 并调用 kindlereader 制作并发生电子书
    :param rss_url: 需要发送的 RSS 链接
    :param configs: 可传入其他 kindlereader 设置，或直接在 kindlereader/config_template.ini 中设置
    :return:
    """
    settings = ConfigParser.ConfigParser()
    settings.read("kindlereader/config_template.ini")
    feeds_num = 1
    for feed in rss_urls:
        settings.set("feeds", "feed%s" % feeds_num, feed)
        feeds_num += 1
    if configs:
        for section in settings.sections():
            for option in settings.options(section):
                if option in configs:
                    if option == "username" and section == "mail":
                        # kindlereader 设置项中有两个 username, 懒得判断了，偷下懒...
                        continue
                    settings.set(section, option, configs[option])

    settings.write(open("kindlereader/config.ini", "w"))
    os.system("python kindlereader/kindlereader.py")


def post_lixian(download_url, download_path, header):
    post_url = 'http://pan.baidu.com/rest/2.0/services/cloud_dl?app_id=250528'
    post_data = {'method': 'add_task', 'save_path': download_path, 'type': '3', 'source_url': download_url}
    response_json = requests.post(post_url, data=post_data, headers=header).json()
    try:
        # 下载成功
        if response_json['rapid_download'] == 1:
            return 1
        # 下载中
        elif response_json['rapid_download'] == 0:
            return 1
    except KeyError:
        # 下载链接错误
        if response_json['error_code'] == 36020:
            return 3
        # 下载任务过多
        if response_json['error_code'] == 36022:
            return 4
    # 其他异常
    except:
        return 1


def bd_lixian(request):
    url = request.POST['url']
    path = request.POST['path']
    if path[0] != '/':
        path = '/'+path
    if path[-1] != '/':
        path += '/'
    x = post_lixian(url, request.POST['path'], json.loads(request.POST['header']))
    if x == 1:
        return HttpResponse('OK')
    elif x == 3:
        return HttpResponse(url+'failed')
    elif x == 4:
        return HttpResponse(url)
    else:
        return HttpResponse('OK')




