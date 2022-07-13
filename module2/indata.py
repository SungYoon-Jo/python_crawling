import time
import pandas as pd
from format import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

def urldata():
    curl = driver.current_url
    url = 'https://www.nuricops.org/declaration/webreg/webregWriteView.do'

    if url == curl:
        print("access good")
    elif url != curl:
        url = 'https://www.nuricops.org/declaration/webreg/webregWriteView.do'
        driver.get(url)
        driver.implicitly_wait(5)

    file = input("실행하게 될 CSV 파일을 입력해주세요 : ")
    
    df = pd.read_csv('./db/' + file + '.csv', sep='\t', names=["href"])

    at = []

    print(file)
    print(len(df))

    for i in df.index:
        print("check number : ", i)

        inurl = driver.find_element(By.ID, "acuseUrl")
        inurl.clear()

        inurl.send_keys(df.loc[i])
        driver.find_element(By.XPATH, """//*[@id="btnUrlCheck"]""").click()
        time.sleep(1)
        
        at.append(Alert(driver).text)
        Alert(driver).accept()  # ALERT 확인 누르기

        driver.find_element(By.XPATH, """//*[@id="btnCaputreOpen"]""").click()

        time.sleep(1)


    print("end good day")
