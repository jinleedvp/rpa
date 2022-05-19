from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

browser = webdriver.Chrome()
browser.get("https://www.koicd.kr/kcd/kcd.do?degree=08")
browser.maximize_window()

# browser.find_element_by_link_text("문자")
# browser.find_elements_by_link_text("문자")[0]

for i in range(73000):
    browser.find_element_by_class_name('icon-arrow-right').click()
    time.sleep(1)
# browser.find_element_by_xpath('//*[@id="licenseNumber"]').send_keys("1")
# browser.find_element_by_xpath('//*[@id="srchSubmitHome"]').click()
# try:
#     WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="0"]/footer/ul[1]/li[1]/h3')))
# finally:
#     None
#
#
# lic = ["1", "2", "3", "4", "5"]
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
