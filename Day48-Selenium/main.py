# Requires Selinium and ChromeDriver(relevant to your version of Google Chrome - https://chromedriver.chromium.org/)
#BeautifulSoup SCRAPES website data and brings it to the user
#Selnium Operates the browser as if it WERE the user

from selenium import webdriver

chrome_driver_path = '/Users/christopher.harris/Documents/Python/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org")
#####SELENIUM ATTR ####
# search_bar = driver.find_element_by_name("q") #useful for automating web forms
# print(search_bar) #wont give the HTML, will give the selenium attribute

#### LOGO SPECS ####
# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

#### DOC LINK ####
doc_link = driver.find_element_by_css_selector(".documentation-widget a")
print(doc_link.text)

bug_link = driver.find_element_by_xpath("""//*[@id="site-map"]/div[2]/div/ul/li[3]/a""") #XPATH : Inspect element > Copy > Copy XPATH | SPECIFIC to an individual item
print(bug_link.text)

# driver.close() #closes the active tab
driver.quit() #closes the entire browser
