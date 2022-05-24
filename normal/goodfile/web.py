
from selenium import webdriver as wd

## 작업폴더가 아닌 다른 폴더에 넣어뒀을 경우 경로를 적어준다.
driver = wd.Chrome(executable_path = './chromedriver')

## 사이트접속
driver.get('https://importer.ec21.com/shoe.html')

## 페이지 하나씩 훑어가기 (1~9)

for page in range(1,2):
    
    ## 'div.listLs_L.buyerL > div > h2 > a' 에 해당하는 elements를 모두 받아온다
    li = driver.find_elements_by_css_selector('div.listLs_L.buyerL > div > h2 > a')
    
    ## li에 저장된 elements에서 loop를 돌리며 제목을 print한다.
    for buyer in li:
        print(buyer.text)

    ## 다음 페이지 클릭
    driver.find_element_by_xpath('//*[@id="pageingWrap"]/div/div[1]/a[%s]' %page).click()

