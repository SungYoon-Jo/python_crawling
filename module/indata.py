import time
import pandas as pd
# from format import *
import format as fm
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


def urldata():
    print(fm.driver.current_url)
    

    file = "data.csv"
    df = pd.read_csv(file, sep='\t', names=["href: "])
    
    aet = list()

    for i in df.index:
        fm.driver.find_element(By.XPATH, """//*[@id="radio1"]""").click()
        print(i)
        inurl = fm.driver.find_element(By.ID, "acuseUrl")
        inurl.clear()
        print(df.loc[i])
        inurl.send_keys(df.loc[i])
        fm.driver.find_element(By.XPATH, """//*[@id="btnUrlCheck"]""").click()
        time.sleep(1)

        aet.append(Alert(fm.driver).text)
        Alert(fm.driver).accept()
        inurl.clear()
        time.sleep(1)

        print(aet[i])
        print()

# 다른 사이트에 있으면 신고 사이트로 와서 확인 후 url이 맞으면 다음 수행
# 6번째 7번째 에서 3,2 번 순으로 라디오 버튼을 클릭함 원인을 모르겠음..