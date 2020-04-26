from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
time.sleep(1)
driver.find_element_by_id("kw").send_keys("帅哥明")
time.sleep(3)
driver.find_element_by_id("su").click()
time.sleep(10)
driver.quit()