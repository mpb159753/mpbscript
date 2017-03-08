# encoding: utf-8

import urllib
import os
import json
import Queue
import threading


def download_check(url):
    site = urllib.urlopen(url)
    not_finished = True
    while not_finished:
        try:
            meta = site.info()
            not_finished = False
        except:
            pass
    return meta.getheaders("Content-Length")[0]


def downloader(download_dic):
    date = download_dic['date'][-5:]
    name = date+download_dic['name'] + u'.mp4'
    url = download_dic['download_url']
    path = u'D:/视频/锵锵三人行/'+download_dic['date'][:4]+u'/'
    if os.path.exists(path+name):
        if int(os.path.getsize(path+name)) > int(download_dic['file_size'])*0.998:
            return
    print u"正在下载" + name
    urllib.urlretrieve(url, path+name)
    print u'下载成功' + name


class Duoxiancheng(threading.Thread):
    def run(self):
        global qq
        while qq.qsize() > 0:
            download_lesson = qq.get()
            try:
                downloader(download_lesson)
            except:
                print u'%s下载失败，已添加重新下载qqqqqq' % download_lesson["name"]
                qq.put(download_lesson)

if __name__ == '__main__':
    url_list = json.loads(open('666.json', 'r').read())['videos']
    qq = Queue.Queue(maxsize=0)
    for i in url_list:
        qq.put(i)
    dd1 = Duoxiancheng()
    dd2 = Duoxiancheng()
    dd3 = Duoxiancheng()
    dd4 = Duoxiancheng()
    dd5 = Duoxiancheng()
    dd1.start()
    dd2.start()
    dd3.start()
    dd4.start()
    dd5.start()

