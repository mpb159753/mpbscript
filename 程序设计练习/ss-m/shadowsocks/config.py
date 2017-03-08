import logging

# Config
MYSQL_HOST = '23.83.254.187'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASS = 'mpb159753'
MYSQL_DB = 'ss'

MANAGE_PASS = 'mpb159753'
# if you want manage in other server you should set this value to global ip
MANAGE_BIND_IP = '127.0.0.1'
#make sure this port is idle
MANAGE_PORT = 5666

PANEL_VERSION = 'V3'
# V2 or V3. V2 not support API
API_URL = 'https://mpb.arukascloud.io'
API_PASS = 'mupass'
NODE_ID = '1'
CHECKTIME = 1
SYNCTIME = 6000

# BIND IP
# if you want bind ipv4 and ipv6 '[::]'
# if you want bind all of ipv4 if '0.0.0.0'
# if you want bind all of if only '4.4.4.4'
SS_BIND_IP = '0.0.0.0'
SS_METHOD = 'aes-256-cfb'

# LOG CONFIG
LOG_ENABLE = False
LOG_LEVEL = logging.DEBUG
LOG_FILE = '/var/log/shadowsocks.log'

