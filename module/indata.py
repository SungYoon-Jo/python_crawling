import time
import pandas as pd
from format import *
import csvmodule as cm
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# 로그인확인도 해야함


def urldata():
    curl = driver.current_url
    url = 'https://www.nuricops.org/declaration/webreg/webregWriteView.do'

    if url == curl:
        print("access good")
    elif url != curl:
        url = 'https://www.nuricops.org/declaration/webreg/webregWriteView.do'
        driver.get(url)
        driver.implicitly_wait(5)

    file = input("실행하게 될 CSV 파일을 입력해주세요 : ")
    
    df = pd.read_csv('./csvdb/' + file + '.csv', sep='\t', names=["href"])

    db = ["youtube", "twitter", "facebook", "tistory", "tumblr"]

    at = []
    gab = []
    mb = []
    href = df['href']

    print(file)
    print(len(df))

    cu = 0
    for i in df.index:
        print("check number : ", i)
        driver.find_element(By.XPATH, """//*[@id="radio1"]""").click()

        inurl = driver.find_element(By.ID, "acuseUrl")
        inurl.clear()

        inurl.send_keys(df.loc[i])
        driver.find_element(By.XPATH, """//*[@id="btnUrlCheck"]""").click()
        time.sleep(1)

        at.append(Alert(driver).text)
        Alert(driver).accept()  # ALERT 확인 누르기

        # if '가능한' in at[i]:
        #     gab.append("GOOD")
        # else:
        #     gab.append("BAD")

        # for y in range(len(db)):
        #     if db[y] in href[i]:
        #         mb.append("member")
        #         cu += 1

        # if cu == 0:
        #     mb.append("not member")
        # elif cu == 1:
        #     cu -= 1

        # print(cu)
        # print(len(mb))
        # print(mb)

        # 문제가 있음 검증까지는 가능하나 특정 위치에 맞춰서 구별 문자열을 넣어야함 -> member가 나오면 +1을 더함.. -> 검증이 안됨..

        inurl.clear()
        time.sleep(1)

    dataf = pd.DataFrame(cm.writer, columns=['URL'])
    dataf['GAB TEXT'] = at
    dataf['GOOD AND BAD'] = gab
    dataf['member'] = mb
    dataf.to_csv('./csvdb/end check/' + file + '.csv', index=True, encoding="utf-8-sig")

    print("end good day")


# 6번째 에서 3,2 번 순으로 라디오 버튼을 클릭함 원인을 모르겠음.. -> url에 트위터가 찍혀 있어서 바뀌였던거

# 추가 기능 1 = 트위터, 페이스북, 유튜브, 인스타 등 거르기 -> db를 만들어서 db안에 있는지 확인 후 -> 추가 기능 2로 db만들어서 만들기

# 추가 기능 2 = 사용 가능한 url 또는 이미 사용 중인 url 찾아서 분류 하기 -> 하고 있는중 -> 생각해보니까 굳이 할 필요가 없는게 엑셀이라 어차피 나눌수 있음 alert text로

# 어느페이지에서 나온 소스인지 페이지 번호 넣기
