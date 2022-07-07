import csv

d = input("기존 데이터를 그대로 사용 하겠습니까? y or n : ")

if d == "y":
    filename = '1.data.csv'
    f = open(filename, 'r', encoding='utf-8-sig', newline='')
    writer = csv.reader(f)
    # 정제 데이터
    
    fn = '2.pdata.csv'
    ff = open(fn, 'r', encoding='utf-8-sig', newline='')
    pd = csv.reader(ff)
    # 원시 데이터

elif d == "n":
    filename = '1.data.csv'
    f = open(filename, 'w', encoding='utf-8-sig', newline='')
    writer = csv.writer(f)
    # 정제 데이터
    
    fn = '2.pdata.csv'
    ff = open(fn, 'w', encoding='utf-8-sig', newline='')
    pd = csv.writer(ff)
    # 원시 데이터






# 사용 안함

    # filn = 'godata.csv'
    # gof = open(filn, 'r', encoding='utf-8-sig', newline='')
    # gd = csv.reader(gof)
    # 신고 가능 데이터