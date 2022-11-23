import os
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
os.environ['PATH'] += r";C:\chromedriver"
driver = webdriver.Chrome(options=options)
