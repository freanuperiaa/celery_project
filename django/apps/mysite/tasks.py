from celery import shared_task
from selenium import webdriver


@shared_task
def scrape_site(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.close()