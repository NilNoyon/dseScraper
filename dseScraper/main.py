import schedule
import time
import os

print('Scheduler initialised')
schedule.every(5).minutes.do(lambda: os.system('scrapy crawl dse_spider'))
print('Next job is set to run at: ' + str(schedule.next_run()))

while True:
    schedule.run_pending()
    time.sleep(1)