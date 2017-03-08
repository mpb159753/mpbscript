# coding:utf-8

import requests
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

url = "https://movie.douban.com/subject/" + str(sys.argv[1]) + "/reviews"

reload_data = {
    "action": "get", "auth": "", "encoding": "utf-8", "name": "douban_movie",
    "url": url}
search_data = {"action": "search", "name": "douban_movie", "global_pattern": "",  "auth": "",
               "item_pattern": '<h3{*} href="{%}"{*}title-link">{%}</a{*}</h3>{*}'}
build_data = {
    "action": "build", "auth": "", "feed_description": "豆瓣影评 (20)",
    "feed_link": url, "feed_title": "豆瓣影评 (20)","global_template": "",
    "item_link": "{%1}", "item_template": "", "item_title": "{%2}",
    "merge_items": "0", "name": "douban_movie"}

up_url = "https://feed43.com/feed.html"

reload_url = requests.post(up_url, data=reload_data).text
search_url = requests.post(up_url, data=search_data)
build_url = requests.post(up_url, data=build_data).text
print url
print build_url
