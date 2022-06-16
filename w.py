# coding=utf8
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
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

driver.find_element(By.XPATH, '/html/body/div[2]/section[1]/div/section/div[1]/div[3]/form/input').click()
driver.find_element(By.XPATH, '/html/body/div[2]/section[1]/div/section/div[1]/div[3]/form/input').send_keys("test")
driver.find_element(By.XPATH, '/html/body/div[2]/section[1]/div/section/div[1]/div[3]/form/button').click()
time.sleep(5)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]
test = ["a", "e", "!reset",]
consonants = [
    "b", "c", "d", "!reset",
    "f", "g", "h", "!reset",
    "j", "k", "l", "!reset",
    "m", "n", "p", "!reset",
    "q", "r", "s", "!reset",
    "t", "v", "w", "!reset",
    "x", "y", "z", "!reset",
    ]
prefix = "w"

for char2 in vowels:
    for char3 in consonants:
        if char3 == "!reset":
            driver.close()
            time.sleep(5)
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
            driver.find_element(By.XPATH, '/html/body/div[2]/section[1]/div/section/div[1]/div[3]/form/input').click()
            driver.find_element(By.XPATH, '/html/body/div[2]/section[1]/div/section/div[1]/div[3]/form/input').send_keys("test")
            driver.find_element(By.XPATH, '/html/body/div[2]/section[1]/div/section/div[1]/div[3]/form/button').click()
            time.sleep(5)
        else:
            for char4 in vowels:
                for char5 in alphabet:
                    nsearch = prefix + char2 + char3 + char4 + char5 + ".com"
                    driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').click()
                    ActionChains(driver).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).perform()# delete previous search text
                    driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys(nsearch)# combination search text
                    driver.find_element(By.XPATH, '//*[@id="domainsAppContent"]/main/dreg-router-outlet/div/search-root/responsive-centered-container/div/div/search-bar-container/findy-bar-container/div/search-bar/findy-bar/form/button[1]').click()# search
                    print(nsearch)
                    time.sleep(3)
                    try:#registered
                        jfail = driver.find_element(By.XPATH, '//*[@id="mat-tab-content-0-0"]/div/related-search-results/exact-match-card/search-result-card-notification/message-bar/div/xap-callout/div/div/xap-callout-body/span').text
                        # txtfile = open(f'{prefix}.txt', 'a')
                        # time.sleep(0.5)
                        # txtfile.write(jfail + "\n")
                        # time.sleep(0.5)
                        # txtfile.close()
                        # time.sleep(0.5)
                    except:
                        try:#nice
                            jdomain = driver.find_element(By.XPATH, '//*[@id="mat-tab-content-0-0"]/div/related-search-results/exact-match-card/div/search-result-card-header/search-result-card-header-desktop/mat-card/div/div[2]/div/search-result-card-domain-name/span').text
                            jprice = driver.find_element(By.XPATH, '//*[@id="mat-tab-content-0-0"]/div/related-search-results/exact-match-card/div/search-result-card-header/search-result-card-header-desktop/mat-card/div/div[3]/row-price/domain-price/span[1]').text
                            txtfile = open(f'{prefix}.txt', 'a')
                            time.sleep(0.5)
                            txtfile.write(jdomain + "	" + jprice + "\n")
                            time.sleep(0.5)
                            txtfile.close()
                            time.sleep(0.5)
                        except:#error
                            txtfile = open(f'{prefix}.txt', 'a')
                            time.sleep(0.5)
                            txtfile.write(nsearch + "	" + "error" + "\n")
                            time.sleep(0.5)
                            txtfile.close()
                            time.sleep(0.5)
