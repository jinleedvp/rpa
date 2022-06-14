# coding=utf8
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
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

# jinleedvp0@gmail.com
# January01)!
# Get a new domain
# driver.find_element_by_xpath('').click()

driver.find_element_by_xpath('/html/body/div[2]/section[1]/div/section/div[1]/div[3]/form/input').click()
driver.find_element_by_xpath('/html/body/div[2]/section[1]/div/section/div[1]/div[3]/form/input').send_keys("test")
driver.find_element_by_xpath('/html/body/div[2]/section[1]/div/section/div[1]/div[3]/form/button').click()
time.sleep(5)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]

# wb = Workbook() # new workbook
# ws = wb.active # call a sheet
# ws_y=1

for char1 in ["j"]:
    for char2 in alphabet:
        for char3 in alphabet:
            for char4 in alphabet:
                for char5 in alphabet:
                    nsearch = char1 + char2 + char3 + char4 + char5 + ".com"
                    driver.find_element_by_xpath('//*[@id="mat-input-0"]').click()
                    ActionChains(driver).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).perform()# delete previous search text
                    driver.find_element_by_xpath('//*[@id="mat-input-0"]').send_keys(nsearch)# combination search text
                    driver.find_element_by_xpath('//*[@id="domainsAppContent"]/main/dreg-router-outlet/div/search-root/responsive-centered-container/div/div/search-bar-container/findy-bar-container/div/search-bar/findy-bar/form/button[1]').click()# search
                    print(nsearch)
                    time.sleep(3)
                    try:#registered
                        jfail = driver.find_element_by_xpath('//*[@id="mat-tab-content-0-0"]/div/related-search-results/exact-match-card/search-result-card-notification/message-bar/div/xap-callout/div/div/xap-callout-body/span').text
                        txtfile = open('j.txt', 'a')
                        time.sleep(0.5)
                        txtfile.write(jfail + "\n")
                        time.sleep(0.5)
                        txtfile.close()
                        time.sleep(0.5)
                    except:
                        try:#nice
                            jdomain = driver.find_element_by_xpath('//*[@id="mat-tab-content-0-0"]/div/related-search-results/exact-match-card/div/search-result-card-header/search-result-card-header-desktop/mat-card/div/div[2]/div/search-result-card-domain-name/span').text
                            jprice = driver.find_element_by_xpath('//*[@id="mat-tab-content-0-0"]/div/related-search-results/exact-match-card/div/search-result-card-header/search-result-card-header-desktop/mat-card/div/div[3]/row-price/domain-price/span[1]').text
                            txtfile = open('j.txt', 'a')
                            time.sleep(0.5)
                            txtfile.write(jdomain + "	" + jprice + "\n")
                            time.sleep(0.5)
                            txtfile.close()
                            time.sleep(0.5)
                        except:#error
                            txtfile = open('j.txt', 'a')
                            time.sleep(0.5)
                            txtfile.write(nsearch + "	" + "error" + "\n")
                            time.sleep(0.5)
                            txtfile.close()
                            time.sleep(0.5)
