import csv

filename = 'ttt.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(f)

writer.writerow("name")

for i in range(3):
    t = []
    t.append("gogo[%d]"% i)
    writer.writerow(t)

# csv 파일로 저장 