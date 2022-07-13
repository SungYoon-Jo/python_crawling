from format import *
import csvmodule as cm
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

def search():
    
    con = int(input("0부터 입력해주세요 : "))
    num = int(input("10단위로 입력해주세요 : "))

    for pg in range(con,num,10):
        if (pg == 0):
            # pluseurl = input('검색어를 터미널에서 입력하세요 : ')
            url = 'https://www.google.com/search?q=%s' %(cm.filename)
            # inurl, intitle, intext 등 구글 검색을 사용 가능하지만 로봇 확인에 걸림

        ch = "&start=%d" % (pg)
        churl = url + ch
        driver.get(churl)
        driver.implicitly_wait(5)

        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        page = soup.select('.NJjxre')
        ppage = soup.select('.tF2Cxc')

        temp = []
        arr = []
        pt = []

        for i in ppage:
            pt = i.a.attrs['href']
            # cm.pd.writerow(pt.split(','))

            try:
                print("so")
                # driver.find_element(By.ID, "ofr")
                driver.find_element(By.XPATH, """//*[@id="ofr"]/i/a""").click()
                # //*[@id="ofr"]/i/a
            except:
                print("good")
        


        
        for i in page:
            temp = i.select_one('.tjvcx').text
            
            if ' ' in temp:
                arr = temp.split()
                # print(arr[0])
            else:
                arr = temp.split()
                # print(arr)
            # print()
            
            cm.writer.writerow(arr[0].split(','))
    
    cm.ff.close()
    cm.f.close()
    print("good")

