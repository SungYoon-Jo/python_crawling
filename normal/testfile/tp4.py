from selenium import webdriver

# 다운받은 chromedriver의 위치를 지정해준다.

url = 'https://www.nuricops.org/index.do'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(5)

login = driver.find_element_by_id("memberId")
login.send_keys("")
login = driver.find_element_by_id("memberPw")
login.send_keys("")
driver.find_element_by_xpath("""//*[@id="btnMemberloginCheck"]""").click()
driver.implicitly_wait(5)

url = 'https://www.nuricops.org/declaration/webreg/webregWriteView.do'
driver.get(url)

driver.find_element_by_xpath("""//*[@id="radio1"]""").click()











# 누리캅스 로그인 후 신고하기 누르고 라디오 1번(사이트) 체크까지 완료
# 추가적으로 기존에 받아온 csv파일에 있는 데이터 삽입 후 중복 체크 까지 해야함