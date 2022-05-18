from bs4 import BeautifulSoup
from selenium import webdriver
import time

query_keyword = input("크롤링 키워드는?")

driver = webdriver.Chrome()
driver.get("https://korean.visitkorea.or.kr/main/main.do")
time.sleep(4)

driver.find_element_by_id('chkForm01').click()

driver.find_element_by_id("btn_search").click()

element = driver.find_element_by_id("inp_search")
element.send_keys(query_keyword)

driver.find_element_by_link_text("검색").click()


full_html = driver.page_source

soup = BeautifulSoup( full_html, 'html.parser' )

time.sleep(2)