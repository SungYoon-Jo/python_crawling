import time
import pandas as pd
from format import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert



def urldata():
    driver.find_element(By.XPATH, """//*[@id="radio1"]""").click()

    file = "google.csv"
    df = pd.read_csv(file, sep='\t', names=["href"])

    aet = list()

    for i in df.index:
        print(i)
        inurl = driver.find_element(By.ID, "acuseUrl")
        inurl.send_keys(df.loc[i])
        driver.find_element(By.XPATH, """//*[@id="btnUrlCheck"]""").click()
        time.sleep(2)

        aet.append(Alert(driver).text)
        Alert(driver).accept()
        time.sleep(2)
        inurl.clear()

        print(aet[i])
        print()
