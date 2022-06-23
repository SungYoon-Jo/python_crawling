from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "./chromedriver"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
url = 'https://www.nuricops.org/declaration/webreg/webregWriteView.do'
driver.get(url)

# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTEMP"
#따로 실행가능 대신 cmd로 따로 크롬을 따로 켜주고 실행 해야함

