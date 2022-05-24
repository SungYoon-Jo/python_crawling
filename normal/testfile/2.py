import csv
import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=apple'

filename = 'test2.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(f)

# table
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

# rows 가져오기
for page in range(1, 2):
	res = requests.get(url + str(page))
	res.raise_for_status()

	soup = BeautifulSoup(res.text, 'lxml')
	print(soup)
	data_rows
	
	data_rows = soup.find('table', attrs={'class':'type_2'}).find('tbody').find_all('tr')
	print(data_rows)
	# for row in data_rows:
	# 	columns = row.find_all('td')
	# 	# print(columns)
	# 	if len(columns) <= 1: # 의미 없는 데이터는 skip
	# 		continue
	# 	data = [column.get_text().strip() for column in columns[:]]
	# 	# print(data)
	# 	writer.writerow(data)