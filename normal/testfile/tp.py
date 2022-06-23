import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
import time
import urllib.parse
import webbrowser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'https://www.nuricops.org/declaration/webreg/webregWriteView.do'
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)
wait = WebDriverWait(driver,5)
da = Alert(driver)
da.text


# 그냥 실행 확인
print("\ngood sccess")

