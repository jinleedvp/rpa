from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
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

# jinleedvp@gmail.com
# December12@
# Get a new domain
time.sleep(30)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]

for char1 in consonants:
    for char2 in vowels:
        for char3 in consonants:
            for char4 in vowels:
                for char5 in consonants:
                    driver.find_element_by_xpath('//*[@id="mat-input-0"]').click()
                    ActionChains(driver).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).send_keys(Keys.BACKSPACE).perform()# open in new tab
                    driver.find_element_by_xpath('//*[@id="mat-input-0"]').send_keys(char1 + char2 + char3 + char4 + char5 + ".com")
                    driver.find_element_by_xpath('//*[@id="domainsAppContent"]/main/dreg-router-outlet/div/search-root/responsive-centered-container/div/div/search-bar-container/findy-bar-container/div/search-bar/findy-bar/form/button[1]').click()
                    time.sleep(5)
                    try:# Add to favorites
                        driver.find_element_by_xpath('//*[@id="mat-tab-content-0-0"]/div/related-search-results/exact-match-card/div/search-result-card-header/search-result-card-header-desktop/mat-card/div/div[4]/row-add-to-favorites/div/button').click()
                    except:
                        pass
