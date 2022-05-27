import csv
from bs4 import BeautifulSoup
from selenium import webdriver


url = 'https://www.google.com/search?q=apple'
# url = 'https://www.google.com/search?q=apple&sxsrf=ALiCzsY7E8BvpQSsNObhfh7C2MxlBF6c4Q:1653633076269&ei=NHCQYqqJELear7wPjuuI0A4&start=10&sa=N&ved=2ahUKEwiq8-Wgh__3AhU3zYsBHY41AuoQ8tMDegQIAxA-&biw=932&bih=714&dpr=1.25'
driver = webdriver.Chrome()
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
r = soup.select('.tF2Cxc')  #원하는 class / name을 F12에서 찾기 # select 는 list로 가져온다. #클래스는 앞에 . 점 붙여준다.

# filename = 'test.csv'
# f = open(filename, 'w', encoding='utf-8-sig', newline='')
# writer = csv.writer(f)

# for i in r:
#     temp = []
#     temp.append(i.select_one('.LC20lb.MBeuO.DKV0Md').text)
#     # print(temp)
#     # writer.writerow(temp)

#     temp.append(i.a.attrs['href'])
#     # print(temp)
#     writer.writerow(temp)

# for i in r:
#     print(len(temp))


# 단계 : url 정보는 받아옴
# 안되는거 : 다음 페이지 항목을 못받아옴
# 해결 방안 : 항목을 업데이트 해줌

num = 5

for i in range(num):
    # driver.find_element_by_xpath('//*[@id="xjs"]/table/tbody/tr/td[%s]' %i).click()
    driver.find_element_by_xpath('//*[@id="xjs"]/table/tbody/tr/td[%s]/a' %i).click()
    # print(i)
    # print("r: " + len(r))
    # print("num:" + num)




    # //*[@id="xjs"]/table/tbody/tr/td[2]/a
    # /html/body/div[7]/div/div[10]/div/div[6]/span[1]/table/tbody/tr/td[2]/a









#크롬 드라이버 닫아주기
# driver.close()

# 실행 확인
print("\ngood sccess")