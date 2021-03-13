from bs4 import BeautifulSoup
import requests



page = requests.get("https://www.bonarea.com/ca/default/locatefuelstation")
print(page.content)

soup = BeautifulSoup(page.content, features="html.parser")
print(soup.prettify())