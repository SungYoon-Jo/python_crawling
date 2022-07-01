from msilib.schema import Class
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import csv
from selenium.webdriver.common.by import By


filename = 'hs.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='')
hs = csv.writer(f)

fn = 'page.csv'
fi = open(fn, 'w', encoding='utf-8-sig', newline='')
page = csv.writer(fi)

chrome_options = Options()  
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
from bs4 import BeautifulSoup

# con = int(input("0부터 입력해주세요 : "))
# num = int(input("10단위로 입력해주세요 : "))

con = 0
num = 10


for pg in range(con,num,10):
    if (pg == 0):
        # pluseurl = input('검색어를 터미널에서 입력하세요 : ')
        pluseurl = "피망머니상"
        url = 'https://www.google.com/search?q=intext:%s' %(pluseurl)

    ch = "&start=%d" % (pg)
    churl = url + ch
    driver.get(churl)
    driver.implicitly_wait(5)

    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    # r = soup.select('.tF2Cxc')
    # time.sleep(3)
    # rr = soup.select_one('.tjvcx')
    rr = soup.select('.jtfYYd')
    # r = driver.find_element(By.CLASS_NAME, "srp")
    # print(r)
    # srp, tF2Cxc, NJjxre, jtfYYd, tjvcx
    # writer.writerow(r) 
    # pn = rr[::2]
    for ii in rr:
        tag = []
        tag.append(ii.select_one('.NJjxre').text)
        pn = tag[:]
        # tag = ii.select_one('.NJjxre').text
        # for i in len(tag):
        hs.writerow([pn])

        # pn = tag[::]
        # print(pn)


    # tag.get_text()
    
    # pn = rr[::2]



    # wr.writerow(rr)

    # for i in rr:
    #     for tag in pn:




    #     temp = []

        # if i.select_one('.qzEoUe'):
        #     continue
        # else:
        #     temp.append(i.select_one('.tjvcx').text.find(http)) # text[0] = 0번째만 출력
        # a = temp.append(i.select_one('.tjvcx').text)
        

        # print(a)
        # print(string.split(maxsplit=2))

        # print(temp.split(' '))
        


        # temp.append(i.select_one('.LC20lb MBeuO DKV0Md'))
        # temp.extend(i.select_one('.tjvcx').text)
        # a = i.select('.tjvcx')[0].text
        # temp.append(i.select('.tjvcx').text)
        # print(a)
        # temp = i.select_one('.tjvcx').text
        # print(cu)

        # val = "https" in temp
        
            # print(temp[0])
        # print(val)
        
        # if 

        # temp.append(i.select('.tjvcx'))
        # temp.append(i.a.attrs['href'])
        # temp.append(aaa)

        # html.writerow(temp)

 

# f.close()