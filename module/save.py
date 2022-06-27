import format as fm
import csvmodule as cm
from bs4 import BeautifulSoup


def search():
    
    con = int(input("0부터 입력해주세요 : "))
    num = int(input("10단위로 입력해주세요 : "))

    for pg in range(con,num,10):
        if (pg == 0):
            pluseurl = input('검색어를 터미널에서 입력하세요 : ')
            url = 'https://www.google.com/search?q=%s' %(pluseurl)

        ch = "&start=%d" % (pg)
        churl = url + ch
        fm.driver.get(churl)
        fm.driver.implicitly_wait(5)

        html = fm.driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        r = soup.select('.tF2Cxc')

        for i in r:
            temp = []
            temp.append(i.a.attrs['href'])
            # temp.append(i.select_one('.LC20lb.MBeuO.DKV0Md').text)
            cm.writer.writerow(temp)

    cm.f.close()