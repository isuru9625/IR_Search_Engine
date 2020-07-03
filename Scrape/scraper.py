from bs4 import BeautifulSoup
import requests
with open('test.html',encoding="utf8") as html_file:
    soup = BeautifulSoup(html_file,'lxml')


for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)
                             
