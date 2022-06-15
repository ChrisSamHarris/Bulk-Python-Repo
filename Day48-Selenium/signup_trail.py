from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = '/Users/christopher.harris/Documents/Python/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, 'fName')
first_name.send_keys('Chris')

last_name = driver.find_element(By.NAME, 'lName')
last_name.send_keys('Harris')

email = driver.find_element(By.NAME, 'email')
email.send_keys('chris.harris@test.com')

submit_button = driver.find_element(By.CLASS_NAME, 'btn')
submit_button.send_keys(Keys.RETURN) ##OR submit_button.click()



