from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '/Users/christopher.harris/Documents/Python/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_nums = driver.find_element_by_xpath("""//*[@id="articlecount"]/a[1]""") ##Can also use driver.find_element_by_css_selector("#articleclount a") || its in a div with the id "articlecount" and the value is the first anchor tag
print(f"Total number of Wikipedia articles : {article_nums.text}")
# article_nums.click()

featured_pictures = driver.find_element_by_link_text("More featured pictures")
# featured_pictures.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.RETURN)

# driver.quit()
