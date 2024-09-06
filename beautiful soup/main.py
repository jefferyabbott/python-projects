from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())

# all_list_items = soup.find_all(name="li")
# for item in all_list_items:
#     print(item.getText())

# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading.string)

# using CSS selectors
# company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))
#
# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(selector=".heading")
# print(headings)
