from selenium.webdriver.common.alert import Alert
from selenium import webdriver
import time

url = 'https://itgo.kr/index.asp'
driver = webdriver.Chrome()
driver.get(url)

time.sleep(5)
print(1)

driver.find_element_by_xpath("""//*[@id="form1"]/button""").click()

time.sleep(3)

print(Alert(driver).text) # 경고창 텍스트 얻음

# alert 창 텍스트 받아오는거 가능 근데 경로를 잘 설정 해주어야함