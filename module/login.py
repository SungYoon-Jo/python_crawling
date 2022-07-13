from format import *
from selenium.webdriver.common.by import By
import format as fm

def add():
    curl = 'https://www.nuricops.org/declaration/webreg/webregWriteView.do'

    url = 'https://www.nuricops.org/index.do'
    driver.get(url)
    driver.implicitly_wait(5)


    try:
        driver.find_element(By.ID, "memberId")
        login = driver.find_element(By.ID, "memberId")
        myid = input('아이디를 입력해주세요 : ')
        login.send_keys(myid)
        mypw = input('패스워드를 입력해주세요 : ')
        login = driver.find_element(By.ID, "memberPw")
        login.send_keys(mypw)
        driver.find_element(By.XPATH, """//*[@id="btnMemberloginCheck"]""").click()
        driver.implicitly_wait(5)

        driver.get(curl)
        print(fm.driver.current_url)

    except:    
        driver.get(curl)
        print(fm.driver.current_url)