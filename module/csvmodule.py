import csv


filename = 'data.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(f)

# 추가 내용 기존 csv파일에 데이터가 있으면 그대로 두고 시작