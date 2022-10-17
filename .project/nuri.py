from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

chrome_options = Options()  
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

url = 'https://www.nuricops.org/declaration/webreg/webregWriteView.do'
driver.get(url)

def clickRadio():

    driver.find_element(By.XPATH, """//*[@id="radio1"]""").click()


    print("radio")
