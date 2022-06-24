from tkinter.messagebox import NO, YES
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)

db = np.array([
    "https://www.apple.com/kr/",
    "https://namu.wiki/w/Apple",
    "https://twitter.com/apple",
    "https://www.instagram.com/apple/?hl=ko"
])


for i in range(2):
    # print("b : ", db[i])
    q = input('url을 입력 하셨나요? YES or NO :')
    if q == YES:
        print("good")
    elif q == NO:
        url = 'https://www.nuricops.org/index.do'
        driver.get(url)

# C:\Program Files\Google\Chrome\Application -> 경로
# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTEMP" -> 명령어
# 따로 실행가능 대신 cmd로 따로 크롬을 따로 켜주고 실행 해야함

# url값이 0 이면 실행하고 0이 아닐시 if 뒤부터 실행인데
# 문제점 : url을 계속 none으로 초기화함 한번만 초기화 해야함
