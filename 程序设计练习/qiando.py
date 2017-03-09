# coding:utf-8

import requests
import sys
import time
import re

reload(sys)
sys.setdefaultencoding('utf-8')


def get_header(curl):
    header = {'X-Requested-With': 'XMLHttpRequest'}
    for i in curl[5:-1].split('-H')[1:]:
        key = i.split(':', 1)[0].strip(" '")
        value = i.split(':', 1)[1].strip("' ")
        if key != 'Accept-Encoding':
            header[key] = value
    return header


def liantong(user_name, password):
    user_name = user_name
    password = password
    s = requests.Session()
    now_time = time.time()

    log_data = {'_': now_time, 'password': password, 'callback': 'jQuery17206215443899268148_1470992690258',
                'productType': '01', 'pwdType': '01', 'redirectType': '03', 'req_time': now_time,
                'redirectURL': 'http://www.10010.com', 'rememberMe': '1', 'userName': user_name}

    log_url = 'https://uac.10010.com/portal/Service/MallLogin'
    verify_url = 'http://iservice.10010.com/e3/static/common/l?_=' + str(now_time)
    qiandao_url = 'http://iservice.10010.com/e3/static/transact/signIn/ajax_yy_signIn?_=' + str(now_time)
    try:
        log = s.get(log_url, params=log_data)
        verify = s.post(verify_url)
        qiandao = s.post(qiandao_url, data={'_': str(now_time)})
        result = qiandao.json()
        if result["respCode"] == '0000':
            qiandao_days = str(result["signDays"])
            write_msg = '%s联通签到成功，已连续签到%s天\n' % user_name, qiandao_days
            return write_msg
        else:
            write_msg = '%s联通签到失败\n' % user_name
            return write_msg
    except:
        write_msg = '%s 联通签到失败，未知错误\n' % user_name
        return write_msg


def zimuzu(user_name, password):
    user_name = user_name
    password = password
    s = requests.Session()

    log_data = {'account': user_name, 'password': password, 'remember': '1', 'url_back': 'http://www.zimuzu.tv/'}

    log_url = 'http://www.zimuzu.tv/user/login'
    try:
        log = s.post(log_url, data=log_data)

        result = log.json()

        if result["status"] == 1:
            write_msg = '字幕组签到成功\n'
            return write_msg
        else:
            write_msg = '字幕组签到失败，错误信息: %s\n' % log.text
            return write_msg
    except:
        write_msg = '字幕组签到失败，未知错误\n'
        return write_msg


def musnow():
    pass


def fuliba(user_name, password):
    user_name = user_name
    password = password
    s = requests.Session()

    log_data = {'answer': '', 'fastloginfield': 'username', 'password': password, 'questionid': '0',
                'referer': 'http://www.wndflb.com/forum.php?mobile=1', 'submit': '登录', 'username': user_name}

    log_url = 'http://www.wndflb.com/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LI77F&mobile=yes'

    try:
        log = s.post(log_url, data=log_data).text
        form_hash = re.findall("&formhash=.*&", log)[0][10:-1]
        qiandao_url = 'http://www.wndflb.com/plugin.php?id=fx_checkin:checkin&infloat=yes&handlekey=fx_checkin&inajax=1&ajaxtarget=fwin_content_fx_checkin&formhash=' + \
                      form_hash + "&" + form_hash
        qiandao = s.get(qiandao_url).text
        result = re.findall("<ul> <li>.*?</li></ul>", qiandao)[0][9:-10]
        write_msg = result
        return write_msg
    except:
        write_msg = '福利吧签到失败，未知错误\n'
        return write_msg


def wd(user_name, password):
    user_name = user_name
    password = password
    s = requests.Session()

    header = {}
    get_hash_page = s.get("http://www.kindle10000.com/", headers=header).text
    re_resualt = re.findall(';formhash=.*"', get_hash_page)
    hashs = re_resualt[0][10:-1]
    print hashs
    qiandao_data = {"fastreply": 0, "formhash": hashs, "qdmode": 3, "qdxq": "kx", "todaysay": ""}
    try:
        qiandao_page = s.post("http://www.kindle10000.com/plugin.php?id=dsu_paulsign:sign&operation="
                              "qiandao&infloat=1&sign_as=1&inajax=1", data=qiandao_data, headers=header).text
        print qiandao_page
        qiandao_page = qiandao_page.replace('\r', '')
        qiandao_page = qiandao_page.replace('\n', '')

        resualt = "万读签到成功：%s \n" % re.findall('<div class="c">.*</div>', qiandao_page)
        return resualt
    except:
        resualt = "万读签到失败\n"
        return resualt


def qq(user_name, password):
    user_name = user_name
    password = password
    s = requests.Session()

    header = {'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3', 'Host': 'www.qiangqiang5.com', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Referer': 'http://www.qiangqiang5.com/plugin.php?id=dsu_paulsign:sign', 'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1', 'Connection': 'keep-alive', 'X-Requested-With': 'XMLHttpRequest', 'Cookie': 'nuOC_2132_saltkey=TU3jjs7J; nuOC_2132_lastvisit=1476012142; nuOC_2132_sid=wHXHxt; nuOC_2132_lastact=1476015955%09api.php%09ad; nuOC_2132_pc_size_c=0; _uab_collina=147601574646829427645542; pgv_pvi=9789988720; pgv_info=ssi=s6438447006; CNZZDATA1323561=cnzz_eid%3D1741100750-1476015431-%26ntime%3D1476015431; amvid=027b2ee5aabdcf2f54373464c1c2ca81; nuOC_2132_onlineusernum=1109; nuOC_2132_pvi=419973707; nuOC_2132_si=s858783017; nuOC_2132_mobile=no; _umdata=65F7F3A2F63DF0201C21B6741A6B9A7DD756241FF13DCC45BF3F67C3438DAAF529DDB03E5F53A4BFE62425030B14FF7C1399F1893F327F09CD185FA9D5341394624B36E9E710C4060C1FFDCC4FFCF32624DBB7FBFA18CE13520A279793AE54172B7C1A16032C74D0; nuOC_2132_ulastactivity=7d81T1DC9Srjj6BQNJz8CA2ZZmNCJJNl6%2BzeAvk3LawrRXh9yH5j; nuOC_2132_auth=b290SJ%2BXJISIvJabb4J3so%2BC5TIKGKNi3K4kNbfssvC%2Bpc2kgInMxalg7lgQiDdNFR887B6iksvTOYCoCrdNMcNZXw; nuOC_2132_lastcheckfeed=82254%7C1476015918; nuOC_2132_lip=222.55.206.8%2C1475986139; nuOC_2132_security_cookiereport=4c4c94pHtlThhUPuCcTYslftMXGdXAPYIouSsl7C14z85XMaKw0O; nuOC_2132_connect_is_bind=0; nuOC_2132_nofavfid=1; nuOC_2132_sendmail=1; nuOC_2132_noticeTitle=1; tjpctrl=1476017739652; nuOC_2132_ignore_notice=1', 'Upgrade-Insecure-Requests': '1', 'Content-Type': "application/x-www-form-urlencoded' --data 'formhash=8c5a35dc&qdxq=kx&qdmode=2&todaysay=&fastreply="}
    get_hash_page = s.get("http://www.qiangqiang5.com", headers=header).text

    re_resualt = re.findall(';formhash=.*"', get_hash_page)
    hashs = re_resualt[0][10:-1]
    print hashs
    qiandao_data = {"fastreply": 0, "formhash": "8c5a35dc", "qdmode": 2, "qdxq": "kx", "todaysay": ""}
    url_data = {"id": "dsu_paulsign:sign", "operation": "qiandao", "infloat": "1", "inajax": 1}
    try:
        qiandao_page = requests.post("http://www.qiangqiang5.com/plugin.php?"
                                     "id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1", data=qiandao_data,
                                     headers=header).text
        print qiandao_page
        qiandao_page = qiandao_page.replace('\r', '')
        qiandao_page = qiandao_page.replace('\n', '')

        resualt = "抢抢签到成功：%s \n" % re.findall('<div class="c">.*</div>', qiandao_page)
        return resualt
    except:
        resualt = "抢抢签到失败\n"
        return resualt


def main():
    save_file = open('log.log', 'a')
    output = '\n======================\n======================\n'


    output += wd(11, 22)
    save_file.write(output)
    save_file.close()
