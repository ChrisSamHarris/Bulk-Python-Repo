##Future improvement/ work - Automatically click additional upgrades 
#REF: https://gist.github.com/angelabauer/affb3ce61bc79ada90dea26052c27c2b

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

chrome_driver_path = '/Users/christopher.harris/Documents/Python/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

auth = driver.find_element(By.ID, "langSelect-EN")
auth.click()

cookie = driver.find_element(By.ID, "bigCookie")


timeout = time.time() + 60*1   # 1 minute from now
while True:
    cookie.click()
    if time.time() < timeout:
        pass
        # money_element = driver.find_element(By.ID, "cookies").text
        # if "," in money_element:
        #     money_element = money_element.replace(",", "")
        # cookie_count = int(money_element)

        # all_prices = driver.find_element(By.ID, "store")
        # item_prices = []

        # for price in all_prices:
        #     price_text = price.text
        #     if price_text != "":
        #         item_cost = int(price_text.split("-")[1].strip().replace(",", ""))
        #         item_prices.append(item_cost)

    elif time.time() > timeout:
        cookie_count = driver.find_element(By.ID, "cookies")
        cookies_second = driver.find_element(By.ID, "cookiesPerSecond")
        print(cookie_count.text)
        print(cookies_second.text)
        break
