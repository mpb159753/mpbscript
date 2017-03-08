# coding:utf-8

import requests
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def get_cookie():
    header = {}
    print(u'请输入Cookie：')
    cookie = 'curl "https://pan.baidu.com/disk/home" -H "DNT: 1" -H "Accept-Encoding: gzip, deflate, sdch, br" -H "Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.6" -H "Upgrade-Insecure-Requests: 1" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H "Referer: http://pan.baidu.com/disk/home" -H "Cookie: BAIDUID=2A888ED37B8A638BA5165FF33BDE82A3:FG=1; PANWEB=1; BDUSS=5qQ3JBWm5nNXR4Tlo5bEJTZmlUbW05RWgwZEx3cGxXeEs3TWhGRklPV1hDTE5YQVFBQUFBJCQAAAAAAAAAAAEAAABVq-YPbXBiMTU5NzUzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJd7i1eXe4tXMH; STOKEN=dd5d940ada16ce8bc9380bf234d9359e36f7aa840f05e486cfa618cad309f1f1; SCRC=b9ca565e60109b0c3a40414b2aa46cdd; BDCLND=cL6vB83YwqaLmZasBKEPc5vTiu"%"2FWFJaMVErYO"%"2Fyg"%"2BW8"%"3D; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1469415817,1469454889,1469550344,1469703200; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1469703600; cflag=15"%"3A3; PANPSC=1733632798303732735"%"3aprhVfOyoCTxhyMAwSelRMRCSssaghBXhcN9WOUyshde5e2NAaU"%"2b52Uq7xbIsIsvh5ikVo1HCevH4AUkUtbwXcOdYF3eht4VhbrSBGunWpIA7LpLTMOoLpf32zHoQ61GQDoflxwdfFOW7FYLShvT4JaAoIkwriKoeHjyg"%"2bX"%"2fmtybc7UdTFzwHh8XjOKj6f4ZfdzGMsemg9Ml3MYyx6aD0yQ"%"3d"%"3d" -H "Connection: keep-alive" -H "Cache-Control: max-age=0" --compressed'
    # cookie = raw_input('')
    for i in cookie[5:-1].split('-H')[1:]:
        key = i.split(':', 1)[0].strip(' "')
        value = i.split(':', 1)[1].strip('" ')
        if key != 'Accept-Encoding':
            header[key] = value
    return header


def worker():
    post_url = 'http://pan.baidu.com/rest/2.0/services/cloud_dl?app_id=250528'
    url_list = []
    print (u'请确认已将下载链接保存至1.log中，按回车继续')
    raw_input('')
    header = get_cookie()
    print (u'请输入下载目录：')
    download_path = u'/新下载/12/'
    qwe = raw_input('')

    save_file = open('1.txt', 'r', 'utf-8').readlines()

    while True:
        try:
            print 'sss'
            save_file = open('1.txt', 'r', 'utf-8').readlines()
            print 'asdf'
            for i in save_file:
                print i
                url_list.append(i)
            break
        except:
            print (u'没有找到‘1.txt’，请重试！')
            raw_input('')

    while True:
        try:
            header['Cookie']
            break
        except:
            print u'地址输入错误，没有获取到Cookie，'
            header = get_cookie()

    for url in url_list:
        post_data = {'method': 'add_task', 'save_path': download_path, 'type': '3', 'source_url': url}

        response = requests.post(post_url, headers=header, data=post_data).json()
        print post_data
        print response
        if response['rapid_download'] == 1:
            print u'下载成功'

print u'MPB百度云批量离线下载工具'
print(u'百度也跟着搞非会员就限速，都是迅雷开的头！')
print u"""
使用步骤：
       1：打开本exe同文件夹下自动生成的“1.log”(不能自己新建，会出错)，将需下载的链接保存进去，每行一个，关闭保存
       2：用Chrome浏览器，登陆自己的百度云，并在网盘根目录按F12打开开发人员模式
       3：点击Network选项卡
       4：刷新页面
       5：在Network选项卡下的‘home’行右键，点击Copy as cURL(cmd)
       6：在输入cookie时黏贴cURL并回车
       7：输入保存至百度云的目录，并用“/”分隔，如：“/新下载/电影/”
       8：等就好了~

"""
q = open('1.log','w')
q.close()
worker()
raw_input(u'已全部提交至离线下载，按回车退出')


