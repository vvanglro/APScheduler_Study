# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 14:18
# @Author  : wanghao
# @File    : APScheduler_scheduled_job.py
# @Software: PyCharm

import time
from apscheduler.schedulers.blocking import BlockingScheduler

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', seconds=5) #运行后间隔5秒执行
def job1():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('job1 --- {}'.format(t))

@scheduler.scheduled_job('cron', second='*/7')  #运行后立马执行一次 然后在7秒间隔执行一次
def job2():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('job2 --- {}'.format(t))

scheduler.start()

'''
运行结果
2021-01-20 14:21:27
job2 --- 2021-01-20 14:21:28
job1 --- 2021-01-20 14:21:32
job2 --- 2021-01-20 14:21:35
job1 --- 2021-01-20 14:21:37
job2 --- 2021-01-20 14:21:42
job1 --- 2021-01-20 14:21:42
job1 --- 2021-01-20 14:21:47
job2 --- 2021-01-20 14:21:49
...余下省略...
'''