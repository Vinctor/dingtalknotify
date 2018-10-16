# -*- coding: utf-8 -*-

import datetime
import os
import traceback

log_dir='log'

#记录日志
def writelog(msg=None):
    if msg==None:
         msg=traceback.format_exc()
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    
    now_time = datetime.datetime.now()
    now_time_string=now_time.strftime('%Y-%m-%d %H:%M:%S')
    file_name=now_time.strftime('%Y-%m-%d')
    file_path=os.path.join(log_dir,file_name)
    result=now_time_string+'--'+msg+'\n'
    with open(file_path,'a') as f:
        f.write(result)

#记录当前进程PID
def logPID():
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    now_time = datetime.datetime.now()
    now_time_string=now_time.strftime('%Y-%m-%d %H:%M:%S')
    file_path=os.path.join(log_dir,'pids')
    pid=os.getpid()
    result=now_time_string+':-'+str(pid)+'\n'
    with open(file_path,'a') as f:
        f.write(result)
