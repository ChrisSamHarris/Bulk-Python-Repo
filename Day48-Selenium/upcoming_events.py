##Scrape Python.org for the 5 Upcoming events into a Dictionary format 

from selenium import webdriver

chrome_driver_path = '/Users/christopher.harris/Documents/Python/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org")

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
for time in event_times:
    print(time.text) #convert each item into human-readable format

for name in event_names:
    print(name.text)

events = {}

for n in range(len(event_times)):
    events[n+1] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)


driver.quit()
