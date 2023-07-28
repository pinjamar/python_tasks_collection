
from bs4 import BeautifulSoup
import requests

def getPage(url):
    try:
        resp = requests.get(url).content
        return BeautifulSoup(resp, "html.parser")
    except requests.RequestException as e:
        print(e)

def getAllNews(newsPage):
    return newsPage.find_all("div", {"class" : "content"})

def getNewsTitle(news):
    return news.find("h3", {"class" : "title"}).text 

def getNewsSummary(news):
    return news.find("span", {"class" : "summary"}).text 

def getNewsList(allNews):
    newsList = []
    for news in allNews:
        newsList.append({"title" : getNewsTitle(news), "summary" : getNewsSummary(news)})
    return newsList


