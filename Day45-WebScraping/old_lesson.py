from bs4 import BeautifulSoup
import requests
from datetime import date

today = date.today().strftime("%B %d, %Y")
## Scrape the hackernews website 
response = requests.get("https://news.ycombinator.com/")
hacker_news = response.text

soup = BeautifulSoup(hacker_news, "html.parser")


### soup.find will retrieve a single occurance  | find_all will recieve all 
articles = soup.find_all(name='a', class_="titlelink")

# article_text = article.getText() #Requires a For Loop 
# article_link = article.get("href") #Requires a For Loop 
article_titles = []
article_links = []
for item in articles:
    title = item.getText()
    article_titles.append(title)
    link = item.get('href')
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]


print(article_titles)
print(article_links)
print(article_upvote)

most_viewed_votes = max(article_upvote)
most_viewed_index = article_upvote.index(most_viewed_votes)

print('\n')
print(f'Most viewed article of {today}:')
print(article_titles[most_viewed_index])
print(article_links[most_viewed_index])
print(f'Upvote Count: {most_viewed_votes}')
