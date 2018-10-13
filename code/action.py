# -*- coding: utf-8 -*-

import requests
import info 
import log
import json

url_head="https://oapi.dingtalk.com/robot/send"


def action(access_token,content):
    url=url_head+'?access_token='+access_token
    json_content=json.loads(content)
    response=requests.post(url,json=json_content)


    log.writelog(str(response.status_code)+'--->'+response.text)






try:
    access_token,content=info.getLocalConfig()
    action(access_token,content)
except ValueError as identifier:
    log.writelog()



