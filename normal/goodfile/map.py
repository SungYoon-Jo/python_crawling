from selenium import webdriver
import time

#1. 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")
#2. 네이버 지도 접속하기
driver.get("https://v4.map.naver.com/")

# !!)네이버 지도 업데이트로 추
driver.find_elements_by_css_selector("button.btn_close")[1].click()

#3. 검색창에 검색어 입력하기 // 검색창: input#search-input
search_box = driver.find_element_by_css_selector("input#search-input")
search_box.send_keys("오골계")
#4. 검색버튼 누르기 // 검색버튼: button.spm
search_button = driver.find_element_by_css_selector("button.spm")
search_button.click()
#5. 검색 결과 확인하기

for n in range(1, 20):
    # 지연시간주기
    time.sleep(1)

    # 컨테이너 dl.lsnx_det
    # stores = html.select("dl.lsnx_det")
    stores = driver.find_elements_by_css_selector("dl.lsnx_det")

    for s in stores:
        name = s.find_element_by_css_selector("dt > a").text
        addr = s.find_element_by_css_selector("dd.addr").text

        try:
            tel = s.find_element_by_css_selector("dd.tel").text
        except:
            tel = "전화번호 없음"
        # 가게 이름 dt > a
        # 가게 주소 dd.addr
        # 전화번호 dd.tel

        print(name)
        print(addr)
        print(tel)

    # 페이지버튼 div.paginate > *
    page_bar = driver.find_elements_by_css_selector("div.paginate > *")

    try:
        if n%5 != 0:
            page_bar[n%5+1].click()
        else:
            page_bar[6].click()
    except:
        print("수집완료")
        break