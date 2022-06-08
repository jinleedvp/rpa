from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://en.wiktionary.org/w/index.php?title=Category:English_2-syllable_words&pagefrom=a-hole#mw-pages")
driver.maximize_window()

for r in range(1,1000):
    t = driver.find_element_by_xpath('//*[@id="mw-pages"]/div/div').text
    print(r)
    print(t)
    time.sleep(1)
    f = open('1.txt', 'a')
    time.sleep(1)
    f.write(t)
    time.sleep(1)
    f.close()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="mw-pages"]/a[2]').click()
    time.sleep(1)
    print(r)
