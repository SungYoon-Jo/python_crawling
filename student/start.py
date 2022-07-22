import time
from format import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# 로그인확인도 해야함


def urldata():
    curl = driver.current_url
    url = 'http://sugang.tu.ac.kr/login/login.aspx'

    if url == curl:
        print("access good")
    elif url != curl:
        url = 'http://sugang.tu.ac.kr/login/login.aspx'
        driver.get(url)
        driver.implicitly_wait(5)
    
    i = 0
    while i < 10: 
        print("check number : ", i)

        try:
            print("try")
            driver.find_element(By.NAME, "user_id")

            login = driver.find_element(By.NAME, "user_id")
            # myid = input('아이디를 입력해주세요 : ')
            myid = "18110140"
            login.send_keys(myid)

            # mypw = input('패스워드를 입력해주세요 : ')
            mypw = "18whtjd!@"
            login = driver.find_element(By.NAME, "password")
            login.send_keys(mypw)

            driver.find_element(By.XPATH, """//*[@id="WebForm1"]/table/tbody/tr[2]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/img""").click()
            
            time.sleep(1)

            driver.get(curl)
            print(driver.current_url)
            # Alert(driver).accept()

        except:
            print("except")
            driver.get(curl)
            print(driver.current_url)
            # Alert(driver).accept()

        i += 1

        if (i == 3):
            break

        # time.sleep(1)

    print("end good day")
