# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 10:38
# @Author  : wanghao
# @File    : APScheduler_date.py
# @Software: PyCharm

from datetime import datetime
from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler

def job(text):
    print(text)

scheduler = BlockingScheduler()
# 在 2021-1-20 运行一次 job 方法
scheduler.add_job(job, 'date', run_date=date(2021, 1, 20), args=['text1'])
# 在 2021-1-20 10:42:00 运行一次 job 方法
scheduler.add_job(job, 'date', run_date=datetime(2021, 1, 20, 10, 42, 0), args=['text2'])
# 在 2021-1-20 10:43:00 运行一次 job 方法
scheduler.add_job(job, 'date', run_date='2021-1-20 10:43:00', args=['text3'])

scheduler.start()