# -*- coding: utf-8 -*-

import requests
import info 
import log
import json
import schedule#pip install schedule
import time
# encoding=utf8 
import sys

reload(sys) 
sys.setdefaultencoding('utf8')

url_head="https://oapi.dingtalk.com/robot/send"


def action(access_token,content):
    
    url=url_head+'?access_token='+access_token
    json_content=json.loads(content)
    response=requests.post(url,json=json_content)


    log.writelog(str(response.status_code)+'--->'+response.text)




try:
    access_token,content=info.getLocalConfig()
    #schedule.every().day.at("18:00").do(action,access_token,content)
    #schedule.every().day.at("18:30").do(action,access_token,content)
    schedule.every(5).seconds.do(action,access_token,content)

    while True:
        schedule.run_pending()
        time.sleep(1)
except ValueError as identifier:
    log.writelog()



