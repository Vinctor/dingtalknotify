# -*- coding: utf-8 -*-

import json
import log


def getLocalConfig():
    try:
        with open('local.json','r') as f:
            info = json.load(f)
            return info
    except Exception as e:
        log.writelog()
        raise e
   
   

