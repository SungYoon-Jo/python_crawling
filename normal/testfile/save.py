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
        url = 'https://www.google.com/search?q=%s' %(pluseurl)

    ch = "&start=%d" % (pg)
    churl = url + ch
    driver.get(churl)
    driver.implicitly_wait(5)

    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    # r = soup.select('.tF2Cxc')
    # time.sleep(3)
    # rr = soup.select_one('.tjvcx')
    rr = soup.select('.NJjxre')
    a = []
    t = []
    hs.writerow(rr)
    for i in rr:
        # a.append(i.select_one('.tjvcx').text)
        a = i.select_one('.tjvcx').text
        # print(a[0])
        # a.find
        # print(a.split(' '))
        # print(a.rsplit(' '))
        # print(a.rstrip(' '))
        # print(a)
        print(a)

        if ' ' in a:
            continue
        print(a)
        print()


        page.writerow(a)
        # 하나씩 받아드려서 뒤에 문장 제거가 안됨
    # for ii in a:
    #     if ' ' in ii:
    #         if 'https' in ii:
    #             print(ii)
    #         t.append(ii)

    # print(t[0])

    # page.writerow(a)











    # r = soup.find("https")
    # r = driver.find_element(By.CLASS_NAME, "srp")
    # print(r)
    # srp, tF2Cxc, NJjxre, jtfYYd, tjvcx
    # page.writerow(soup) 
    # pn = rr[::2]
    # tag = []
    # temp = []

    # math = 0
    # for ii in rr:
        

    #     tag.append(ii.select_one('.NJjxre').text)

    #     if 'https' in ii:
    #         math += 1
    #         print(math)
    #         temp.append(tag)
    #         print(temp)

    # cu = len(tag)
    # page.writerow(temp)
    # hs.writerow(tag)
    # for i in range(cu):
        # print(i, tag[i])
        # hs.writerow(tag[i])
        # print(len(tag[-1]))
    
    # for iii in tag:
    #     if ' ' in iii:
    #         temp.append(iii)
    # print(temp)
    # 

    
    
# ›



        

        # tag.extend(ii.select_one('.NJjxre').text)
        # pn = tag[:]
        # print(len(tag[0]))
        # a = tag[0][:]
        # print(len(tag[2]))
        # for cu in tag[0]:
            # print(len(cu[0]))
            # print(len(tag[0]))



            # temp = []
            # temp.append(cu[0])

            # hs.writerow(temp)
            # if tag[0][cu] == ' ':
            #     continue
            # print(tag[0][cu])




        # tag = ii.select_one('.NJjxre').text
        # for i in len(tag):
        # hs.writerow(tag)
        # pn = tag[::]


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