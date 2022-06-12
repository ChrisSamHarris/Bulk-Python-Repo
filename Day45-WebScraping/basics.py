from bs4 import BeautifulSoup

#### Parsing the HTML file 

with open("./website.html") as web:
    website = web.read()  ##read vs readlines?

soup = BeautifulSoup(website, 'html.parser') ##IF parser doesn't work, import lxml and use that instead 

print(soup.title.string)
#print(soup.prettify())
print(soup.li.string) ##Only gets hold of the FIRST iteration

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags: 
    print(tag.getText()) ##get the text 
    print(tag.get('href'))

heading = soup.find(name="h1", id="name")
print(heading.text)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.text)
print(section_heading.getText())
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
print(company_url)
name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings)
