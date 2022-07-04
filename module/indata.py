import time
import pandas as pd
from format import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


def urldata():
    driver.find_element(By.XPATH, """//*[@id="radio1"]""").click()
    # driver.find_element(By.ID, "redio1").click()

    file = "test.csv"
    df = pd.read_csv(file, sep='\t', names=["href"])
    aet = list()

    for i in df.index:
        print(i)
        inurl = driver.find_element(By.ID, "acuseUrl")
        inurl.send_keys(df.loc[i])
        print(inurl.send_keys(df.loc[i]))
        driver.find_element(By.XPATH, """//*[@id="btnUrlCheck"]""").click()
        # btnUrlCheck
        time.sleep(2)

        aet.append(Alert(driver).text)
        Alert(driver).accept()
        inurl.clear()

        print(aet[i])
        print()
