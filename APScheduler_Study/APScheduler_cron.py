# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 10:52
# @Author  : wanghao
# @File    : APScheduler_cron.py
# @Software: PyCharm
import time, os
from apscheduler.schedulers.blocking import BlockingScheduler


def test():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(t)
    print('aaa')


def job(text):
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('{} --- {}'.format(text, t))
    os.system('chcp 65001')  # 加上这个在控制台输出不乱码
    os.system('taskkill /F /IM Python.exe')


if __name__ == '__main__':
    scheduler = BlockingScheduler()

    # 每天12点执行
    scheduler.add_job(test, 'cron', hour='14')
    # 每天12点03分执行
    scheduler.add_job(job, 'cron', hour='14', minute='03', args=['job2'])

    # # 在每天11点，每隔 1分钟 运行一次 job 方法
    # scheduler.add_job(job, 'cron', hour=11, minute='*/1', args=['job1'])
    # # 在每天11和12点的15分，运行一次 job 方法
    # scheduler.add_job(job, 'cron', hour='11-12', minute='15', args=['job2'])

    scheduler.start()

'''
运行结果：
job1 --- 2021-01-20 11:08:00
job1 --- 2021-01-20 11:09:00
job1 --- 2021-01-20 11:10:00
job2 --- 2021-01-20 11:10:00
job1 --- 2021-01-20 11:11:00
...余下省略...
'''
