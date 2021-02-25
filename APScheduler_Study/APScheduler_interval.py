# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 10:44
# @Author  : wanghao
# @File    : APScheduler_interval.py
# @Software: PyCharm

import time
from apscheduler.schedulers.blocking import BlockingScheduler

def job(text):
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('{} --- {}'.format(text, t))

scheduler = BlockingScheduler()
# 每隔 1分钟 运行一次 job 方法
scheduler.add_job(job, 'interval', minutes=1, args=['job1'])
# 在 2021-01-20 10:50:00至2021-01-20 10:52:00期间，每隔1分30秒 运行一次 job 方法
scheduler.add_job(job, 'interval', minutes=1, seconds = 30, start_date='2021-01-20 10:50:00', end_date='2021-01-20 10:52:00', args=['job2'])

scheduler.start()

'''
运行结果：
job1 --- 2021-01-20 10:47:32
job1 --- 2021-01-20 10:48:32
job1 --- 2021-01-20 10:49:32
job2 --- 2021-01-20 10:50:00
job1 --- 2021-01-20 10:50:32
job2 --- 2021-01-20 10:51:30
job1 --- 2021-01-20 10:51:32
job1 --- 2021-01-20 10:52:32
...余下省略...
'''