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
    name = date+download_dic['title'] + u'.mp4'
    print u"正在下载" + name
    url = download_dic['download_link']
    path = u'D:/视频/锵锵三人行/20'+download_dic['date'][:2]+u'/'
    if os.path.exists(path+name):
        if int(os.path.getsize(path+name)) == int(download_check(url)):
            return 1
    urllib.urlretrieve(url, path+name)
    return u'可能完成了'


class Duoxiancheng(threading.Thread):
    def run(self):
        global qq
        while qq.qsize() > 0:
            download_lesson = qq.get()
            try:
                download_msg = downloader(download_lesson)
                if download_msg == 1:
                    download_lesson['check_times'] += 1
                else:
                    print u'%s下载成功' % download_lesson["title"]
            except:
                print u'%s下载未成功，已添加重新下载' % download_lesson["title"]
                qq.put(download_lesson)

if __name__ == '__main__':
    url_list = json.loads(open('123.json', 'r').read())['videos']
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





