from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser = webdriver.Chrome()
browser.get("https://directory.nccaom.org/")
browser.maximize_window()

# browser.find_element_by_link_text("문자")
# browser.find_elements_by_link_text("문자")[0]
time.sleep(100)
browser.find_element_by_xpath('//*[@id="postalcode"]').send_keys("10001")
browser.find_element_by_xpath('//*[@id="sbr"]/div/form/div[3]/h6/button[1]').click()
# try:
#     WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="0"]/footer/ul[1]/li[1]/h3')))
# finally:
#     None
#
#
# lic = ["19000", "19001", "19002", "19003", "19004"]
#
# for i in lic:
#     browser.find_element_by_xpath('//*[@id="licenseNumber"]').clear()
#     browser.find_element_by_xpath('//*[@id="licenseNumber"]').send_keys(i)
#     browser.find_element_by_xpath('//*[@id="srchSubmit"]').click()
#     try:
#         WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="0"]/footer/ul[1]/li[1]/h3')))
#     finally:
#         None
#     name = browser.find_element_by_xpath('//*[@id="0"]/footer/ul[1]/li[1]/h3').text
#     num =  browser.find_element_by_xpath('//*[@id="lic0"]').text
#     print("%s / %s" % (name, num))
