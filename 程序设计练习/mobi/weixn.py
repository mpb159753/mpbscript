# coding:utf-8

import requests
import sys
import time
import re
import json
import html2text

reload(sys)
sys.setdefaultencoding('utf-8')


def loader(url):
    result = requests.get(url).text
    result = result.replace('\n', '')
    result = result.replace('\r', '')
    passage = re.findall('<div class="rich_media_content ".*?</div>', result)[0]
    return passage

sa = open('3.json', 'r').read()
qlist = json.loads(sa)
jlist = qlist["other"]
new = []
last = ''
summ = "# Summary\n\n"
hula = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
n = 1

last_juan = ''
for i in jlist:
    full = "# "
    # 获取正文
    e = i["app_msg_ext_info"]["content_url"].replace("amp;", '')
    w = loader(e)
    # w = ''
    markdown = html2text.html2text(w)
    markdown = markdown.replace('\n\n', "\n")
    # 获取标题
    print i["app_msg_ext_info"]["title"]
    title = i["app_msg_ext_info"]["title"]
    # try:
    #     juan = re.findall(u"第.*?卷", title)[0]
    #     title = title.replace(juan, '')
    #     zhang = re.findall(u"第.*?章", title)[0]
    #
    # except:
    #     ju = raw_input("输入卷名：")
    #     juan = "第%s卷" % ju
    #     zha = raw_input("输入章名：")
    #     zhang = "第%s章" % zha
    #     if juan == '':
    #         juan = last_juan
    #     else:
    #         last_juan = juan
    # title = juan + zhang
    # # 保存文件
    # z = raw_input("章：")
    # j = raw_input("卷：")
    # if j == '':
    #     j = last
    # else:
    #     last = j
    try:
        juan = re.findall(u"第.*?卷", title)[0]
        title = title.replace(juan, '')
        zhang = re.findall(u"第.*?章", title)[0]

        title = juan + zhang
        # 保存文件
        z = raw_input("章：")
        j = raw_input("卷：")

        if j == '':
            j = last
        else:
            last = j
    except:

        j = '7'
        z = str(n)
        n += 1

    full = full + title + '\n\n' + markdown
    file_name = j + '/' + z + '.md'
    #
    # 添加到列表
    hula[int(j)].append({'num': int(z), "file_name": file_name, "title": title})
    wee = open(file_name, 'w')
    wee.write(full)
    wee.close()

print hula
for i in hula:
    hula[i].sort()
    for gg in hula[i]:
        summ += '    * [%s](%s)\n' % (gg["title"], gg["file_name"])
print summ
qwww = open('summ2.md', 'w')
qwww.write(summ)
qwww.close()
