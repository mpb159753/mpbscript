# encoding: utf-8

import urllib
import urllib2


def post(url, data, cookie):
    req = urllib2.Request(url)
    data = urllib.urlencode(data)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    opener.addheaders.append(('Cookie', cookie))
    response = opener.open(req, data)
    return response.read()

post_data = {'method': 'add_task', 'save_path': '/新下载1/quanyou/5/', 'type': '3',
             'source_url': 'ed2k://|file|%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%'
                           '88%86%E7%82%B8.The.Big.Bang.Theory.S08E04.%E4'
                           '%B8%AD%E8%8B%B1%E5%AD%97%E5%B9%95.HDTVrip.102'
                           '4X576.mkv|222981341|63f01b30868e7f88b7d049932'
                           '430e643|h=3biotgcs4por3hrdolo4yijxla3hcdcw|/'}

Cookie = 'BAIDUID=E08067AAA24984930D3848BE9676C57A:FG=1; BIDUPSID=E08067AA' \
         'A24984930D3848BE9676C57A; PSTM=1443593968; _ga=GA1.2.1910329758.' \
         '1443782957; PANWEB=1; Hm_lvt_773fea2ac036979ebb5fcc768d8beb67=14' \
         '44572185; Hm_lpvt_773fea2ac036979ebb5fcc768d8beb67=1444572215; H' \
         'm_lvt_b181fb73f90936ebd334d457c848c8b5=1444572185; Hm_lpvt_b181f' \
         'b73f90936ebd334d457c848c8b5=1444572185; BDUSS=m9lckRhZkdSZjBYdEx' \
         'HRHRTT092OEs0RXNKQlV2WjFINmZFZTdWNjFTTXMtVUZXQVFBQUFBJCQAAAAAAAAA' \
         'AAEAAAAfk9AJbXBiMTU5NzUzbXBiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' \
         'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACxsGlYsbBpWY; PANPSC=100516155619' \
         '83411943%3AZjFd1PuLJ%2BDEc7wM7XUs1K4kal94c2KmWSvoWyJQmQIgPDrUUY6f' \
         'dBOAD5r1J1nbE8dh9S620TQLwD3j4VwNg5oy4Bw8GCUdjRT8o6c2oTqP8XxTJKWpu' \
         'LSjlJEoQsPI61cZVbIYFu9b%2BQxikh4DRQ%3D%3D; Hm_lvt_adf736c22cd6bcc' \
         '36a1d27e5af30949e=1444572215; Hm_lpvt_adf736c22cd6bcc36a1d27e5af30' \
         '949e=1444572215; cflag=65141%3A3'
url = 'http://pan.baidu.com/rest/2.0/services/cloud_dl?app_id=250528'

print post(url, post_data, Cookie)

