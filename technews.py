from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text


soup = BeautifulSoup(yc_web_page, "html.parser")

article_news = soup.find_all(name="a", class_="titlelink")

article_text = [text.getText() for text in article_news]

article_link = [link.get("href") for link in article_news]

article_upvote = [int(upvote.getText().split()[0]) for upvote in soup.find_all(name="span", class_="score")]

largest_score = max(article_upvote)

largest_index = article_upvote.index(largest_score)
print(f"Upvote score: {article_upvote[largest_index]}\nTitle: {article_text[largest_index]}\nLink:{article_link[largest_index]}")







# with open("website.html", errors="ignore") as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, "html.parser")
#
# all_p_tags = soup.find_all(name="p")
# print(all_p_tags)
# for tag in all_p_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
#
#
#
#
# # print(soup.prettify())
# # print(soup.p)
#
#
# # print(soup.title)
# # print(soup.title.string)


# heading = soup.find(name="h1", id="name")
#
#
# section_heading = soup.find(name="h3", class_="heading")
#
#
# company_url = soup.select_one(selector="p a")