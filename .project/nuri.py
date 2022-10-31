from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
# import csvmodule as cm
import csv 
from PIL import Image
import cv2



chrome_options = Options()  
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# driver = webdriver.Chrome(ChromeDriverManager().install())


# url = 'https://www.nuricops.org/declaration/webreg/webregWriteView.do'
# driver.get(url)

# file = input("실행하게 될 CSV 파일을 입력해주세요 : ")
file = "file"
df = pd.read_csv('./csvdb/' + file + '.csv', sep='\t', names=["href"])
# im = pd.read_csv('./img/' + file + '.png', sep=' \t', names=["href"])
# im = pd.read('./img/' + 'img.png')
# img = Image.open("./img/img.png")
# img = cv2.imread("./img/img.png")
# print(img)

filename = "file"
ff = open('./csvdb/' + filename + '.csv', 'r', encoding='utf-8-sig', newline='')
writer = csv.reader(ff)



def clickRadio():

    driver.find_element(By.XPATH, """//*[@id="radio2"]""").click()

    print("radio")

def inputUrl():
    
    print("input")
    
    alert = []
    
    for i in df.index:
        
        driver.find_element(By.XPATH, """//*[@id="radio4"]""").click()
        
        print(i)
        
        inurl = driver.find_element(By.ID, "acuseUrl")
        inurl.clear()
        
        inurl.send_keys(df.loc[i])
        driver.find_element(By.XPATH, """//*[@id="btnUrlCheck"]""").click()
        time.sleep(1)

        
        alert.append(Alert(driver).text)
        Alert(driver).accept()
        
        inurl.clear()
        
        # driver.find_element(By.CSS_SELECTOR,"input[type='file']").send_keys(img)
        driver.find_element(By.CSS_SELECTOR,"input[type='file']").send_keys(r"C:\Users\whtjd\Documents\GitHub\python\.project\img\img.png")
        # driver.find_element_by_css_selector("input[type='file']").send_keys(r"C:\Users\user-pc\Desktop\img.PNG")
        # driver.find_element_by_css_selector("input[type='file']").send_keys(r"C:\Users\whtjd\Documents\GitHub\python\.project\img\img.png")
        
        time.sleep(1)


    

    dataf = pd.DataFrame(writer, columns=['URL'])
    dataf['GAB TEXT'] = alert
    dataf.to_csv('./csvdb/end check/' + file + '.csv', index=True, encoding="utf-8-sig")

clickRadio()
inputUrl()