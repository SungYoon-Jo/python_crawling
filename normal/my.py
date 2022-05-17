from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get('https://scolkg.com/')
driver.implicitly_wait(time_to_wait=5)
element = driver.find_element_by_xpath('//*[@id="app_coinboard"]/div[2]/table/tbody/tr[8]/td[6]').text
driver.quit()# import urllib.parse import quote_plus

import urllib.parse
from bs4 import BeautifulSoup
from selenium import webdriver
import time

baseurl = 'https://www.google.com/search?q='
pluseurl = input('검색어를 터미널에서 입력하세요 : ')
url = baseurl + urllib.parse.quote_plus(pluseurl)

  
print(url)

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)

r = soup.select('.tF2Cxc')  #원하는 class / name을 F12에서 찾기 # select 는 list로 가져온다. #클래스는 앞에 . 점 붙여준다.

print(type(r))

for i in r :  
    print(i.select_one('.LC20lb.MBeuO.DKV0Md').text) #제목 #select one을 사용하면 텍스트를 가져올 수 있다. #클래스에 빈칸은 점으로 바꿔준다.
    print(i.a.attrs['href']) #링크 #a 태그 안에, href 를 속성을 갖는 링크 불루직
    print()
# if (driver.close() == 1):
#     print('good2')

driver.find_element_by_css_selector('#main_pack > div.paging > a.next').click()

#크롬 드라이버 닫아주기
#driver.close()
