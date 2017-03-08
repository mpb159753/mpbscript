# encoding: utf-8
import requests
import re
import json
import urllib
from lxml import etree


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


def url_finder(html):
    url_list = []
    links_ul = html.xpath('/html/body/div[3]/div[2]/div[4]/div[@class="vlistbox picstyle01"]/ul')
    download_url = 'http://dyn.v.ifeng.com/cmpp/video_msg_ipad.js'

    for li in links_ul:
        divs = li.xpath('li/div[@class="pic"]')
        for div in divs:
            qwer = True
            xx = div.xpath('a')[0].attrib
            link = xx['href']
            title = xx['title']
            date = div.xpath('span/text()')
            video_id = re.findall('\d/(.*?).shtml', link)[0]
            print video_id
            while qwer:
                try:
                    download_link = json.loads(requests.get(download_url, params={'msg': video_id}).text[3:-4])["videoplayurl"]
                    qwer = False
                    file_size = download_check(download_link)
                except:
                    pass
            url_list.append({'link': link, 'name': title, 'date': date, 'download_link': download_link, 'file_size': file_size})
    return url_list

all_list = []
for i in range(1, 31):
    url = 'http://v.ifeng.com/vlist/tv/qqsrx/all/0/%s/detail.shtml' % i
    page_html = etree.HTML(requests.get(url).text)
    all_list += url_finder(page_html)
    print str(i)+'OK'

qq = {'videos': all_list}
save_file = open('888.json', 'w')
save_file.write(json.dumps(qq))
save_file.close()





