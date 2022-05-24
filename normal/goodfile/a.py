import csv
import ssl
import tempfile
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

context = ssl._create_unverified_context()

search = input("검색어를 입력하세요 : ")
url = 'https://m.search.naver.com/search.naver?where=m_view&sm=mtb_jum&query=%'
newUrl = url + quote_plus(search)

html = urlopen(newUrl, context=context).read()
soup = BeautifulSoup(html,'html.parser')

total = soup.select('.api_txt_lines.total_tit')
searchList = []

for i in total :
    temp = []
    temp.append(i.text)
    temp.append(i.attrs['href'])
    searchList.append(temp)

f = open(f'{search}.csv','w',encoding='utf-8',newline='')
csvWriter = csv.writer(f)

for i in searchList:
    csvWriter.writerow(i)
    csv

f.close()
print("완료 !")