'''
schedule-定时任务
'''
import schedule
import time
import threading   #内置的多线程模块

def job1():
    print("I'm working... in job1  start")
    time.sleep(5)
    print("I'm working... in job1  end")
def job2():
    print("I'm working... in job2")
def run_threaded(job):
     job_thread = threading.Thread(target=job)
     job_thread.start()
schedule.every(10).seconds.do(run_threaded,job1)
schedule.every(10).seconds.do(run_threaded,job2)

while True:
    schedule.run_pending()
    time.sleep(1)

