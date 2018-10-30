# -*- coding: utf-8 -*-

import log
import time
import datetime


def canGoOn():
    #周几
    day_in_week=time.strftime("%w", time.localtime())
    #print 'day_in_week:'+day_in_week
    log.writelog('day_in_week:'+str(day_in_week))
    #周六周日不发送
    day_in_week=int(day_in_week)
    if day_in_week==6 or day_in_week==0:
        return False

    #20点之后 7点之前不发送
    hour_in_day=time.strftime("%H", time.localtime())
    #print 'hour_in_day:'+hour_in_day
    log.writelog('hour_in_day:'+str(hour_in_day))
    hour_in_day=int(hour_in_day)
    if hour_in_day>20 or hour_in_day<=7:
        return False
    return True

   
def nextWorkDay():
   today=datetime.datetime.now()
   #today=datetime.datetime.strptime('2018-11-2', "%Y-%m-%d")
   day_in_week=int(today.strftime("%w"))
   nextDay=today+datetime.timedelta(days=1)
   day_in_week=int(nextDay.strftime("%w"))
   while day_in_week==0 or day_in_week==6:
        nextDay=nextDay+datetime.timedelta(days=1)
        day_in_week=int(nextDay.strftime("%w"))
   print day_in_week
   return nextDay.strftime("%Y-%m-%d")


if __name__=='__main__':
   print  nextWorkDay()
    #print canGoOn()
