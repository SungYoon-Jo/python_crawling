from format import *
from selenium.webdriver.common.by import By


def add():
    url = 'https://www.nuricops.org/index.do'
    driver.get(url)
    driver.implicitly_wait(5)

    c = driver.find_element(By.ID, "frmLogin").is_displayed()

    if c == True:
        print("good")
    elif c== "":
        print("not")

    # if driver.find_element(By.ID, "frmLogin"):
    #     print("b")
    #     login = driver.find_element(By.ID, "memberId")
    #     myid = input('아이디를 입력해주세요 : ')
    #     login.send_keys(myid)
    #     mypw = input('패스워드를 입력해주세요 : ')
    #     login = driver.find_element(By.ID, "memberPw")
    #     login.send_keys(mypw)
    #     driver.find_element(By.XPATH, """//*[@id="btnMemberloginCheck"]""").click()
    #     driver.implicitly_wait(5)

    # url = 'https://www.nuricops.org/declaration/webreg/webregWriteView.do'
    # driver.get(url)