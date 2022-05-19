from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth

# from openpyxl import Workbook

import time

driver = webdriver.Chrome()
driver.get("https://domains.google/")
driver.maximize_window()

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

# # driver.find_element_by_link_text("문자")
# # driver.find_elements_by_link_text("문자")[0]
driver.find_element_by_xpath('//*[@id="header"]/div[1]/div[2]/div[1]/a').click()
driver.find_element_by_xpath('//*[@id="identifierId"]').click()
driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys("jinleedvp@gmail.com")

# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="next"]/div/button'))).click()# search
time.sleep(10)

driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').click()
driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys("#February28")

time.sleep(30)

driver.find_element_by_xpath('//*[@id="dregSidenavContainer"]/dreg-sidenav/div/mat-nav-list/div/a[1]').click()
time.sleep(3)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]



for domain in attemptting
    driver.find_element_by_xpath('//*[@id="mat-input-0"]').click()
    driver.find_element_by_xpath('//*[@id="mat-input-0"]').send_keys("jinleedvp")

    try:# Add to favorites
        driver.find_element_by_xpath('//*[@id="mat-tab-content-0-0"]/div/related-search-results/exact-match-card/div/search-result-card-header/search-result-card-header-desktop/mat-card/div/div[4]/row-add-to-favorites/div/button').click()
    except:
        pass




# driver.find_element_by_xpath('//*[@id="srchSubmitHome"]').click()
# try:
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="0"]/footer/ul[1]/li[1]/h3')))
# finally:
#     None
#
# wb = Workbook() # new workbook
# ws = wb.active # call a sheet
# ws_y=9626
#
# for i in range(9626,19200):#19195
#     driver.find_element_by_xpath('//*[@id="licenseNumber"]').clear()
#     driver.find_element_by_xpath('//*[@id="licenseNumber"]').send_keys(i)
#     driver.find_element_by_xpath('//*[@id="srchSubmit"]').click()
#     licnum = i
#     ws.cell(column=1, row=ws_y, value=licnum)
#     try:
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="0"]/footer/ul[1]/li[1]/h3')))# Name
#         driver.find_element_by_xpath('//*[@id="mD0"]').click()# More Detail
#         time.sleep(1)
#         driver.switch_to.window(driver.window_handles[1])# tab switch
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="clntType"]')))
#
#
#         try:
#             name = driver.find_element_by_xpath('//*[@id="name"]').text
#             ws.cell(column=2, row=ws_y, value=name)
#         except:
#             pass
#
#         try:
#             lictyp = driver.find_element_by_xpath('//*[@id="licType"]').text
#             ws.cell(column=3, row=ws_y, value=lictyp)
#         except:
#             pass
#
#         try:
#             licstu = driver.find_element_by_xpath('//*[@id="primaryStatus"]').text
#             ws.cell(column=4, row=ws_y, value=licstu)
#         except:
#             pass
#
#         try:
#             licstu2 = driver.find_element_by_xpath('//*[@id="secondaryStatus"]').text
#             ws.cell(column=5, row=ws_y, value=licstu2)
#         except:
#             pass
#
#         try:
#             prename = driver.find_element_by_xpath('//*[@id="prevName"]').text
#             ws.cell(column=6, row=ws_y, value=prename)
#         except:
#             pass
#
#         try:
#             address = driver.find_element_by_xpath('//*[@id="address"]/p[2]').text
#             ws.cell(column=7, row=ws_y, value=address)
#         except:
#             pass
#
#         try:
#             liciss = driver.find_element_by_xpath('//*[@id="issueDate"]').text
#             ws.cell(column=8, row=ws_y, value=liciss)
#         except:
#             pass
#
#         try:
#             licexp = driver.find_element_by_xpath('//*[@id="expDate"]').text
#             ws.cell(column=9, row=ws_y, value=licexp)
#         except:
#             pass
#
#         wb.save("1.xlsx")
#         time.sleep(1)
#         driver.close()
#         time.sleep(1)
#         driver.switch_to.window(driver.window_handles[0])
#         time.sleep(1)
#         ws_y += 1
#         # input("Press Enter to continue...")
#     except:
#         wb.save("1.xlsx")
#         time.sleep(1)
#         driver.switch_to.window(driver.window_handles[0])
#         time.sleep(1)
#         ws_y += 1
#         # input("Press Enter to continue...")
