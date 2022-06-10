from selenium import webdriver

driver_path = './chromedriver'

driver = webdriver.Chrome(driver_path, options=options)
variable = driver.current_url

print(variable)