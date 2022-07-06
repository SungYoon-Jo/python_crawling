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
            # inurl, intitle, intext 등 구글 검색을 사용 가능하지만 로봇 확인에 걸림

        ch = "&start=%d" % (pg)
        churl = url + ch
        fm.driver.get(churl)
        fm.driver.implicitly_wait(5)

        html = fm.driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        page = soup.select('.NJjxre')
        ppage = soup.select('.tF2Cxc')

        temp = []
        arr = []
        pt = []

        for i in ppage:
            pt = i.a.attrs['href']

            cm.pd.writerow(pt.split(','))
        
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