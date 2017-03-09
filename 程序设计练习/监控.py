# coding:utf-8

import requests
import sys
import json
import re
import top.api
import time
import datetime


reload(sys)
sys.setdefaultencoding('utf-8')


def send_msg(number, text, way, code):
    appkey = 
    secret = ""

    if way == "call":
        req = top.api.AlibabaAliqinFcVoiceNumSinglecallRequest()
        req.set_app_info(top.appinfo(appkey, secret))

        req.extend = ""
        req.called_num = number
        req.called_show_num = "051482043272"
        req.voice_code = code
        try:
            resp = req.getResponse()
            print (resp)
        except Exception, e:
            print (e)
    elif way == "call_msg":
        req = top.api.AlibabaAliqinFcTtsNumSinglecallRequest()
        req.set_app_info(top.appinfo(appkey, secret))

        req.extend = ""
        req.tts_param = text
        req.called_num = number
        req.called_show_num = "051482043272"
        req.tts_code = code
        try:
            resp = req.getResponse()
            print (resp)
        except Exception, e:
            print (e)
    elif way == "text":
        req = top.api.AlibabaAliqinFcSmsNumSendRequest()
        req.set_app_info(top.appinfo(appkey, secret))

        req.extend = ""
        req.sms_type = "normal"
        req.sms_free_sign_name = "MPB最帅~"
        req.sms_param = json.dumps(text)
        req.rec_num = number
        req.sms_template_code = code
        try:
            resp = req.getResponse()
            print (resp)
        except Exception, e:
            print (e)


def monitor():
    headers = {'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/54.0.2840.99 Safari/537.36', 'DNT': '1', 'Connection': "keep-alive",
               'X-Requested-With': 'XMLHttpRequest',
               'Cache-Control': 'max-age=0',
               'Cookie': 'acw_tc=AQAAACIVc1KJhwEAgHQ1cwXaDB0udU2b; ASP.NET_SessionId=0rk3ltfylfvdc445p'
                         'jp0tgvn; SESSION_COOKIE=member.transrush.com1; _gat=1; SiteCode=CN; SiteName='
                         'j1m183L1H00160N110Q2Z1z1L0n2I0T2; Marketing=http://www.transrush.com/; '
                         'Hm_lvt_5f97b18de3423180375703d5f0196b0c=1479179209,1479298063,1479372144,'
                         '1479442370; Hm_lpvt_5f97b18de3423180375703d5f0196b0c=1479444232; User:::'
                         'UserID=1163U3R1Z0x3Q3V1V0K1c1c1f210h0w1; User::UserID=1163U3R1Z0x3Q3V1V0K1c'
                         '1c1f210h0w1; User::UserCode=K2s281d2b2m3Y080v1l3j354c3S0z0v0; User::EMail=n2'
                         'T1k1f2P0F1d1J2r14350m2I1Q1p2M0T1I2r1e2u140t2k2S2H2w2T0o164e3j3; User::TUserID'
                         '=506355; User::TrueName=; User::UserType=y3S202N153F3x0Z0T2L0Q2U1F001n0D3; Us'
                         'er::Mobile=i2R3A1y2P3I3q0R3J0E3x3t2g393z1f1; EbayVCode=R482; _ga=GA1.2.428973'
                         '941.1478873882; Hm_lvt_ed6795fe183849e7beff63e703c250c2=1479354181,1479372141'
                         ',1479441806,1479442690; Hm_lpvt_ed6795fe183849e7beff63e703c250c2=1479444370; '
                         'Hm_lvt_c45fc15bb15965f8169ad0707f8f0934=1479179209,1479298065,1479372144,1479'
                         '442370; Hm_lpvt_c45fc15bb15965f8169ad0707f8f0934=1479444370',
               'Upgrade-Insecure-Requests': '1'}

    s = requests.get("http://member.transrush.com/Transport/LogisticsTransferTrace.aspx?code="
                     "DD161118375041&vcode=&source=undefined", headers=headers)
    response = s.text
    response = response.replace("\r\n", '')
    track_list = re.findall("class='track-list  current'>.*?</div></div></div></div>", response)[0]

    ctime = re.findall("class='track-of-time'.*?</div></div><div", track_list)[0][27:-16]
    text = re.findall("class='track-text'>.*?</div></div>", track_list)[0][19:-12]
    print ctime
    print text
    log = open("/home/wwwroot/default/1.html", "w")
    x = datetime.datetime.now() - datetime.timedelta(hours=14)
    log.write("<h2>" + x.strftime("%Y-%m-%d %H:%M:%S") + str(x.weekday()+1) + "</h2>\n")
    log.write("<h2>" + ctime + " " + text + "</h2>")
    log.close()
    old_text = open("1.log", 'r').read()

    if text == old_text:
        return
    else:
        print "send_msg"
        old_text = open("1.log", "w")
        old_text.write(text)
        old_text.close()
        return


def check():
    # old = {u"IsGiftbag": None, u"GiftbagCosts": None, u'SplitBoxPriceStr': None, u'HasTariffImage': 0, u'DestCountry': 6, u'IsShowSF': False, u'IsSFSend': False, u'IsFreightRear': True, u'IsSplit': False, u'PhotographCosts': u'0.00', u'DeclarePriceCurrencyCode': u'\u7f8e\u91d1', u'SplitBoxNumStr': None, u'AddValueInsurance': u'0.00', u'IsShowPhoto': True, u'AddValueFirm': u'0.00', u'TotalFreight': u'125.00', u'IsPhotograph': False, u'OperateAmount': u'0.00', u'StoreageTimeOut': 0, u'InsurePriceID': 0,  u'AttachParam': None, u'Ismerger': False, u'IsAlreadySplit': False, u'CurrencyId': 1, u'TransportLogistics': [{u'Step': 1, u'StateName': u'\u5df2\u5165\u5e93', u'HappenTime': u'2016-11-18'}, {u'Step': 2, u'StateName': u'\u5f85\u652f\u4ed8', u'HappenTime': u'1900-01-01'}], u'IsCarryPort': 0, u'OrderAddress': {u'AddressID': 0, u'UserID': None, u'TrueName': None, u'PostCode': None, u'Email': None, u'UpdateUser': 0, u'UpdateTime': None, u'AreaIDPath': None, u'TransportFormMstID': None, u'IDCard': None, u'DeleteTime': None, u'TransportFromDtlID': 3382884, u'AreaID': None, u'Mobile': None, u'Verification': None, u'AreaNamePath': None, u'IDCardFile': None, u'OSDeliveryCode': None, u'DefaultFlag': None, u'TransportOrderCode': None, u'DeleteUser': None, u'Tel': None, u'IDCardID': None, u'IDCardFileOther': None, u'ChangedMappingProperties': {}, u'ChangedProperties': {}, u'CreateUser': None, u'CreateTime': None, u'AddressInfo': None}, u'OrderState': u'\u8fd0\u8d39\u5f85\u4ed8\u6b3e', u'HasInsure': False, u'ProductChannelCode': u'QIYINGHM', u'OrderNo': u'DD161118375041', u'IsShowCheck': True, u'TariffPrice': u'0.00', u'IsShowMerger': False, u'IsClaimRush': False, u'Remark': u'', u'TariffPayFlag': 0, u'_hasTariffImage': 0,  u'DeclaredPrice': u'116.99', u'AddValueInsured': u'0.00', u'CurrencyCode': u'\u4eba\u6c11\u5e01', u'IsPay': False, u'IsIdCard': False, u'TotalTariff': u'0.00', u'AddValueMerger': u'0.00', u'Costs': u'125.00', u'Addservice': u'', u'IsTariffPayFlag': 0, u'SFSendPriceStr': u'0.00', u'AddValueInventory': u'0.00', u'WarehouseID': 2, u'TotalCosts': u'112.50', u'ProductList': [{u'ProductPrice': u'36.50', u'ProductNumber': 2, u'CurrencyId': 2, u'CatagoryName': u'\u80cc\u5305', u'CurrencyCode': u'USD', u'CurrencySign': u'', u'ProductName': u'Jack Wolfskin Alpine Trail Rucksack', u'TransportFromMstId': 3598678, u'CurrencyName': u'\u7f8e\u91d1'}, {u'ProductPrice': u'43.99', u'ProductNumber': 1, u'CurrencyId': 2, u'CatagoryName': u'\u80cc\u5305', u'CurrencyCode': u'USD', u'CurrencySign': u'', u'ProductName': u'Jack Wolfskin Highland Trail Rucksack', u'TransportFromMstId': 3598678, u'CurrencyName': u'\u7f8e\u91d1'}], u'Weight': u'6.5', u'ProductChannelID': 37, u'CanBeCancel': 0, u'ShowCarryButton': 0, u'AddServiceShowType': 1, u'IsShowSolidify': True, u'AddValueWarehouseRental': u'0.00', u'AddValueTaxBill': u'0.00',  u'IsRushProduct': False, u'IsDetain': False,  u'Id': 3382884, u'WarehouseOperateMode': u'   '}
    old = {u'IsAbnormalPackage': False, u'OrderTypeFlag': 3, u'IndemnityFlag': 0, u'PayFlag': 0,}
    headers = {'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/54.0.2840.99 Safari/537.36', 'DNT': '1', 'Connection': "keep-alive",
               'X-Requested-With': 'XMLHttpRequest',
               'Cache-Control': 'max-age=0',
               'Cookie': 'acw_tc=AQAAACIVc1KJhwEAgHQ1cwXaDB0udU2b; ASP.NET_SessionId=0rk3ltfylfvdc445p'
                         'jp0tgvn; SESSION_COOKIE=member.transrush.com1; _gat=1; SiteCode=CN; SiteName='
                         'j1m183L1H00160N110Q2Z1z1L0n2I0T2; Marketing=http://www.transrush.com/; '
                         'Hm_lvt_5f97b18de3423180375703d5f0196b0c=1479179209,1479298063,1479372144,'
                         '1479442370; Hm_lpvt_5f97b18de3423180375703d5f0196b0c=1479444232; User:::'
                         'UserID=1163U3R1Z0x3Q3V1V0K1c1c1f210h0w1; User::UserID=1163U3R1Z0x3Q3V1V0K1c'
                         '1c1f210h0w1; User::UserCode=K2s281d2b2m3Y080v1l3j354c3S0z0v0; User::EMail=n2'
                         'T1k1f2P0F1d1J2r14350m2I1Q1p2M0T1I2r1e2u140t2k2S2H2w2T0o164e3j3; User::TUserID'
                         '=506355; User::TrueName=; User::UserType=y3S202N153F3x0Z0T2L0Q2U1F001n0D3; Us'
                         'er::Mobile=i2R3A1y2P3I3q0R3J0E3x3t2g393z1f1; EbayVCode=R482; _ga=GA1.2.428973'
                         '941.1478873882; Hm_lvt_ed6795fe183849e7beff63e703c250c2=1479354181,1479372141'
                         ',1479441806,1479442690; Hm_lpvt_ed6795fe183849e7beff63e703c250c2=1479444370; '
                         'Hm_lvt_c45fc15bb15965f8169ad0707f8f0934=1479179209,1479298065,1479372144,1479'
                         '442370; Hm_lpvt_c45fc15bb15965f8169ad0707f8f0934=1479444370',
               'Upgrade-Insecure-Requests': '1'}
    s = requests.get("http://member.transrush.com/ajax/AjaxTransportInfo.aspx?actionType=6&orderno="
                     "DD161118375041&ordertypeflag=3&time=1479553334001", headers=headers).json()
    # log = open("/home/wwwroot/default/1.html", "a")

    difference = ''
    for i in s:
        try:
            if s[i] != old[i]:
                difference = i
                break
        except:
            difference = i
            break
    if difference:
        print 'xx'
   


def amazon():
    headers = {'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3', 'Host': 'www.amazon.com', 'Accept': 'text/html,*/*', 'Referer': 'https://www.amazon.com/gp/product/B00AVSEVG0/', 'Connection': 'keep-alive', 'X-Requested-With': 'XMLHttpRequest', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'}
    price_page = requests.get("https://www.amazon.com/gp/twister/ajaxv2?sid=156-3541988-7027603&ptd=OUTDOOR_RECREATION_PRODUCT&sCac=1&twisterView=glance&pgid=sports_display_on_website&rid=C7VHAJDHENVSXAA16SXY&dStr=size_name%2Ccolor_name&auiAjax=1&json=1&dpxAjaxFlag=1&isUDPFlag=1&ee=2&nodeID=3375251&parentAsin=B00DUO6W46&enPre=1&storeID=sporting-goods&psc=1&asinList=B00AVSEVG0&isFlushing=2&dpEnvironment=hardlines&id=B00AVSEVG0&mType=full", headers=headers)
    q = price_page.text.replace('\n', '')
    q = q.replace('\\n', '')
    q = q.replace('\\r', '')
    w = re.findall('priceblock_ourprice\\\\".*?span', q)
    print w[0]
    price = re.findall(">.*?<", w[0])[0][1:-1]
    ss = float(price[1:])
    text = price
    old_text = 90
    if ss < old_text:
        return 0
    else:
        print "send_msg"
        return 0



amazon_result = 10
while amazon_result:
    try:
        amazon_result = amazon()
    except:
        print 'again'
        amazon_result -= 1

# monitor()
# check()
# amazon_result = 1
# while amazon_result:
#     try:
#         amazon_result = amazon()
#     except:
#         pass
# amazon()


# print time.strftime("%m-%d %H:%M", time.localtime()-50400.0)
