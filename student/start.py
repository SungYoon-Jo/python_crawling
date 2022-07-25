import time
from format import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import keyboard

def urldata():
    curl = driver.current_url
    hand = driver.window_handles
    
    leng = len(hand)+1

    url = 'http://sugang.tu.ac.kr/login/login.aspx'

    if url == curl:
        print("access good")
    elif url != curl:
        url = 'http://sugang.tu.ac.kr/login/login.aspx'
        driver.get(url)
        driver.implicitly_wait(5)
    
    print(leng)

    while True: 
        print("start~")
        if keyboard.is_pressed("q"):
            print("You pressed q")
            break

        for i in range(0,leng):

            if url != curl:
                url = 'http://sugang.tu.ac.kr/login/login.aspx'
                driver.get(url)
                driver.implicitly_wait(5)

            print(i)

            if i == 3:
                i = 0
                continue

            try:
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
                
                time.sleep(0.3)

                last_tab = hand[i]
                # time.sleep(0.5)
                driver.switch_to.window(last_tab)
            except:
                url = 'http://sugang.tu.ac.kr/login/login.aspx'
                driver.get(url)
                driver.implicitly_wait(5)

    print("end good day")
