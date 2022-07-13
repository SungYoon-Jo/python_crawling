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
        hs.writerow(pt.split(','))
    
    for i in page:
        temp = i.select_one('.tjvcx').text
        
        if ' ' in temp:
            arr = temp.split()
            # print(arr[0])
        else:
            arr = temp.split()
            # print(arr)
        # print()
        
        writer.writerow(arr[0].split(','))

ff.close()
f.close()
print("good")


    # id ofr