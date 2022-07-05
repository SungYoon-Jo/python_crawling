import csv

d = input("기존 데이터를 그대로 사용 하겠습니까? y or n : ")

if d == "y":
    filename = 'data.csv'
    f = open(filename, 'r', encoding='utf-8-sig', newline='')
    writer = csv.reader(f)
    
    fn = 'pdata.csv'
    ff = open(fn, 'r', encoding='utf-8-sig', newline='')
    pd = csv.reader(ff)

elif d == "n":
    filename = 'data.csv'
    f = open(filename, 'w', encoding='utf-8-sig', newline='')
    writer = csv.writer(f)

    fn = 'pdata.csv'
    ff = open(fn, 'w', encoding='utf-8-sig', newline='')
    pd = csv.writer(ff)