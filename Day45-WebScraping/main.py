from bs4 import BeautifulSoup
import requests
import json
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

article_upvote_raw = [score.getText() for score in soup.find_all(name='span', class_='score')]
article_upvote_raw.append("X Points") ##Upvotes added, initally an issue as for some reason the scrape only brings 29 out of 30 values 

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

article_dict = {"articles" : [] }

index_num = 0
for item in articles:
    article_dict["articles"].append({
        "Title" : item.getText(),
        "Link": item.get('href'),
        "Votes": article_upvote_raw[index_num]
    })
    index_num += 1

with open(f'HackerNewsToday.json', 'w') as outfile:
            json.dump(article_dict, outfile)

most_viewed_votes = max(article_upvote)
most_viewed_index = article_upvote.index(most_viewed_votes)

print('\n')
print(f'Most viewed article of {today}:')
print(article_titles[most_viewed_index])
print(article_links[most_viewed_index])
print(f'Upvote Count: {most_viewed_votes}')
