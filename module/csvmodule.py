import csv 

d = input("기존 데이터를 그대로 사용 하겠습니까? y or n : ")

if d == "y":
    filename = input('어떤 파일을 READ 하시겠습니까? : ')

    f = open('./csvdb/' + filename + '.csv', 'r', encoding='utf-8-sig', newline='')
    writer = csv.reader(f)
    # 정제 데이터
    
    fn = '1.pdata.csv'
    ff = open(fn, 'r', encoding='utf-8-sig', newline='')
    pd = csv.reader(ff)
    # 원시 데이터

elif d == "n":
    filename = input('검색어는 무엇입니까? : ')

    f = open('./csvdb/' + filename + '.csv', 'w', encoding='utf-8-sig', newline='')
    writer = csv.writer(f)
    # 정제 데이터
    
    fn = '1.pdata.csv'
    ff = open(fn, 'w', encoding='utf-8-sig', newline='')
    pd = csv.writer(ff)
    # 원시 데이터



# 사용 안함

    # filn = 'godata.csv'
    # gof = open(filn, 'r', encoding='utf-8-sig', newline='')
    # gd = csv.reader(gof)
    # 신고 가능 데이터