from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:/chrome/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)

driver.get('https://naver.com')