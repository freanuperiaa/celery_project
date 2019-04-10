import time

from celery import Celery
from selenium import webdriver


app = Celery('scrape', broker='pyamqp://guest@localhost//', backend='rpc://')
@app.task
def scrape(urls):
    for url in urls:
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(1)
        print('successfully opened page.')
        driver.quit()

@app.task
def do_something(x):
    for itr in range(x):
        print('going', itr, 'times!')

@app.task
def raise_by_self(x):
        num = x
        for itr in range(x):
            num *= x
        return num

