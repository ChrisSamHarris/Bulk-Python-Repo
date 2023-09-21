from bs4 import BeautifulSoup
import requests
import json

## Scrape the hackernews website 
response = requests.get("https://news.ycombinator.com/")
hacker_news = response.text
print(hacker_news)

soup = BeautifulSoup(hacker_news, "html.parser")

### soup.find will retrieve a single occurance  | find_all will recieve all 
articles = soup.find_all("a", rel="noreferrer")
print(articles)

# article_text = article.getText() #Requires a For Loop 
# article_link = article.get("href") #Requires a For Loop 
article_titles = []
article_links = []
for item in articles:
    title = item.getText()
    print(title)
    article_titles.append(title)
    link = item.get('href')
    print(link)
    article_links.append(link)

article_upvote_raw = [score.getText() for score in soup.find_all(name='span', class_='score')]
#upvote(s) only return 29 values in contrast to the 30 provided elsewhere:: FIX Below 
article_upvote_raw.append("X Points")

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

article_dict = {"articles" : [] }

print(len(articles))
print(len(article_upvote_raw))
print(len(article_upvote))
print(len(article_titles))
print(len(article_links))

##Upvotes added, initally an issue as for some reason the scrape only brings 29 out of 30 values 
index_num = 0
for item in articles:
    article_dict["articles"].append({
        "Title" : item.getText(),
        "Link": item.get('href'),
        "Votes": article_upvote_raw[index_num]
    })
    print(article_upvote_raw[index_num])
    index_num += 1


with open(f'HackerNewsToday.json', 'w') as outfile:
            json.dump(article_dict, outfile)
