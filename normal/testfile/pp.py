# import urllib.parse import quote_plus
import csv
import requests
import urllib.parse
from bs4 import BeautifulSoup
from selenium import webdriver
import time


baseurl = 'https://www.google.com/search?q='
pluseurl = input('검색어를 터미널에서 입력하세요 : ')
url = baseurl + urllib.parse.quote_plus(pluseurl)

filename = 'test.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(f)

print(url) # https://www.google.com/search?q=입력데이터(pluseurl)

driver = webdriver.Chrome()
driver.get(url)
print(driver)
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
r = soup.select('.tF2Cxc')  #원하는 class / name을 F12에서 찾기 # select 는 list로 가져온다. #클래스는 앞에 . 점 붙여준다.
# r = soup.find('table', attrs={'class':'type_2'}).find('tbody').find_all('tr')
# writer.writerow(r)
# print(r)
# print(type(r)) # <class 'bs4.element.ResultSet'>

for page in range(3,4):
    time.sleep(3)
    for i in r :
    # #     # data = (i.select_one('.LC20lb.MBeuO.DKV0Md').text,i.a.attrs['href'])
    # #     # columns = (i.select_one('.LC20lb.MBeuO.DKV0Md').text,i.a.attrs['href'])
    # #     # columns = i.find_all('.LC20lb.MBeuO.DKV0Md')
    # #     # columns = (i.select_one('.LC20lb.MBeuO.DKV0Md').text,i.a.attrs['href'])
    # #     # columns = i.select.one('.LC20lb.MBeuO.DKV0Md')
    # #     # dt = [column.text() for column in columns[:]]
    #     print(r)
        # writer.writerow(data)

        # print(i.select_one('.LC20lb.MBeuO.DKV0Md').text) #제목 #select one을 사용하면 텍스트를 가져올 수 있다. #클래스에 빈칸은 점으로 바꿔준다.
        # print(i.select('.LC20lb.MBeuO.DKV0Md'))
        # print(i.a.attrs['href'])
        # print(i.a.attrs)
        # print(i.a.attrs['href']) #링크 #a 태그 안에, href 를 속성을 갖는 링크 불루직
        print()
        writer.writerow(i.a.attrs['href'])

    # 다음 페이지 클릭
    # driver.find_element_by_xpath('//*[@id="xjs"]/table/tbody/tr/td[%s]' %page).click()


#크롬 드라이버 닫아주기
driver.close()

# 실행 확인
print("good sccess")