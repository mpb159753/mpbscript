# encoding: gbk

import urllib
import urllib2
import json


def post(url, data, header):
    req = urllib2.Request(url)
    data = urllib.urlencode(data)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    for key in header:
        opener.addheaders.append((key, header[key]))
    response = opener.open(req, data)
    return response.read()


def get_cookie():
    header = {}
    print(u'������Cookie��')
    cookie = 'curl "http://pan.baidu.com/disk/home?errno=0^&errmsg=Auth^%^20Login^%^20Sucess^&stoken=a520d0d66e0a4d107255cffb259fd5e06cde607ae98910897882fcbe764c076fc3aef9286efbe33a5d0b264a99fde5a81db27b2a172a4c40320bfd3db9690ec2359d34bee1dc^&bduss=d0ff4d20f82e511a554f1d235c72c046a2cf2e53bb2db0aef801bf5ea031c88c4083397fdde062b65cd397a0b740356764489a5002d58c2bca4c5f5152891f1789d94fa1c068556dd656007e83417d686789e962064ab1bd4cc411a223bd969c7de6c87ee0586265009c92602f499e6c4d0c9ab3f229d65d3b93898c8604a7a118296f615171bf8a57eca49948ae150eceff66a908a68f9a063b7f4be689810a4e8d924b2528046eef8d908c64c15b5c65583d631552f701e0360abb0ed7d28feede529dfd0a^&ssnerror=0" -H "DNT: 1" -H "Accept-Encoding: gzip, deflate, sdch" -H "Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.6" -H "Upgrade-Insecure-Requests: 1" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H "Referer: http://pan.baidu.com/disk/home?errno=0^&errmsg=Auth^%^20Login^%^20Sucess^&stoken=ad48b00042942f761a724fdd71f04c04704960e6335244f8cd968db986fc0479f5bd250544ae2ac4862f555672a91836051b4377a5ddadc3a411e46e68c864554314b4bdb377^&bduss=908e02023d799150d25977b61cdd990ee66fb4c8442ece2a4d1069153171625b9a44bcd63e00b62cb5a6de5bd70b8200a38b488b225dfbee5adc54ab9db49e7219704f4ca47426c4aa3cdf5b2a4344b004059ede48b1d46f5571e42a186fa0587e406b9cfd160975a5864cc436885bbd9dbf64e5e072f54c166a3b88a943364ab66c4d0c9ab3f229d65d3b93898c8604a7a118296f615171bf8a57eca49948ae150eceff66a908a68f9a063b7f4be689810a4e8be33b3d052d5be09b9b9468d8011d65028e19^&ssnerror=0" -H "Cookie: BAIDUID=6DF16D589E24E3F413D11BA712475DCC:FG=1; PANWEB=1; BDUSS=0ZyYTBtRk1XaXBkUzNBbXFOOE1YaFdZfk9QUkVjYjJrNzdjUzQxfnRwVTV4SWxZSVFBQUFBJCQAAAAAAAAAAAEAAAAfk9AJbXBiMTU5NzUzbXBiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADk3Ylg5N2JYQ; STOKEN=be667bc0be103208e145f77a1e2e169edf9ca7009bce714e82a7330bc29e5817; SCRC=de134492b0dd5825c7a1efb1176fde6e; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1482831200; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1482831677; cflag=15^%^3A3; PANPSC=1222468698746027802^%^3AZjFd1PuLJ^%^2BDEc7wM7XUs1K4kal94c2KmWSvoWyJQmQIgPDrUUY6fdBOAD5r1J1nb5sHqiUF3JV5SqW49skH^%^2BdJoy4Bw8GCUdjRT8o6c2oTqP8XxTJKWpuLSjlJEoQsPIEvWkXgeKQGwqDpteEQOYNudYF3eht4Vh^%^2Fxo4W2iFshg^%^3D" -H "Connection: keep-alive" -H "Cache-Control: max-age=0" --compressed'
    # cookie = raw_input(u'')
    for i in cookie[5:-1].split('-H')[1:]:
        key = i.split(':', 1)[0].strip(' "')
        value = i.split(':', 1)[1].strip('" ')
        if key != 'Accept-Encoding':
            header[key] = value
    return header


def worker():
    post_url = 'http://pan.baidu.com/rest/2.0/services/cloud_dl?app_id=250528'
    url_list = []
    print (u'��ȷ���ѽ��������ӱ�����111.txt�У����س�����')
    raw_input('')
    header = get_cookie()
    print (u'����������Ŀ¼��')
    download_path = '/111/'

    while True:
        try:
            print 'sss'
            save_file = open('111.txt', 'r').readlines()
            print 'asdf'
            for i in save_file:
                print i
                url_list.append(i)
            break
        except:
            print (u'û���ҵ���111.txt���������ԣ�')
            raw_input(u'')

    while True:
        try:
            header['Cookie']
            break
        except:
            print u'��ַ�������û�л�ȡ��Cookie��'
            header = get_cookie()

    for url in url_list:
        post_data = {'method': 'add_task', 'save_path': download_path, 'type': '3', 'source_url': url}
        response = json.loads(post(post_url, post_data, header))
        if response['rapid_download'] == 1:
            print u'���سɹ�'

print u'MPB�ٶ��������������ع���'
print(u'�ٶ�Ҳ���Ÿ�ǻ�Ա�����٣�����Ѹ�׿���ͷ��')
print u"""
ʹ�ò��裺
       1���ڱ�exeͬ�ļ����½�����111.txt��(û���Ҿ�����ô��)���������ص����ӱ����ȥ��ÿ��һ�����رձ���
       2����Chrome���������½�Լ��İٶ��ƣ��������̸�Ŀ¼��F12�򿪿�����Աģʽ
       3�����Networkѡ�
       4��ˢ��ҳ��
       5����Networkѡ��µġ�home�����Ҽ������Copy as cURL(cmd)
       6��������cookieʱ���cURL���س�
       7�����뱣�����ٶ��Ƶ�Ŀ¼�����á�/���ָ����磺��/������/��Ӱ/��
       8���Ⱦͺ���~

"""
worker()
# raw_input(u'��ȫ���ύ���������أ����س��˳�')


