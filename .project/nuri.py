from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
import time
import pandas as pd



chrome_options = Options()  
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# url = 'https://www.nuricops.org/declaration/webreg/webregWriteView.do'
# driver.get(url)

file = input("실행하게 될 CSV 파일을 입력해주세요 : ")
df = pd.read_csv('./csvdb/' + file + '.csv', sep='\t', names=["href"])



def clickRadio():

    driver.find_element(By.XPATH, """//*[@id="radio1"]""").click()

    print("radio")

def inputUrl():
    for i in df.index:
        inurl = driver.find_element(By.ID, "acuseUrl")
        inurl.clear()
        
        inurl.send_keys(df.loc[i])
        driver.find_element(By.XPATH, """//*[@id="btnUrlCheck"]""").click()
        time.sleep(1)

        Alert(driver).accept()



clickRadio()