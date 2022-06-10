import csv
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import urllib.parse

# selenium 안에 webdriver를 사용하기 위해서 웹 사이트를 띄운다
driver = webdriver.Chrome()

# csv파일로 저장 할수 있도록 한다. 이름, 파일 데이터 형태, 저장 순으로 초기화 해준다.
filename = 'google.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(f)

con = 0
num = 30

# con = 0 부터 num 30까지 10씩 증가하며 반복
for pg in range(con,num,10):
    time.sleep(4)
    print(pg)
    # url = "https://www.google.com/search?q=apple&ei=CKmVYveQMpqJoAS7xbuQAg&start=%d&sa=N&ved=2ahUKEwj3tIuUgon4AhWaBIgKHbviDiIQ8tMDegQIAxA9&biw=1036&bih=666&dpr=1.25"% pg
    if (pg == 0):
        pluseurl = input('검색어를 터미널에서 입력하세요 : ')
        url = 'https://www.google.com/search?q=%s' %(pluseurl)

    ch = "&start=%d" % (pg)
    churl = url + ch

    driver.get(churl)
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    r = soup.select('.tF2Cxc') 
    for i in r:
        temp = []
        temp.append(i.select_one('.LC20lb.MBeuO.DKV0Md').text)
        temp.append(i.a.attrs['href'])
        writer.writerow(temp)

#크롬 드라이버 닫아주기
driver.close()

# 그냥 실행 확인
print("\ngood sccess")


# 추가 기능 동적 url, next page, click url and inside url 캡처



# 참고 자료

# for i in r:
#     temp = []
#     temp.append(i.select_one('.LC20lb.MBeuO.DKV0Md').text)
#     # print(temp)
#     writer.writerow(temp)

#     temp.append(i.a.attrs['href'])
#     # print(temp)
#     writer.writerow(temp)

# for i in r:
#     print(len(temp))