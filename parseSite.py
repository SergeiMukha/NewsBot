import requests
from bs4 import BeautifulSoup as BS

def getHtml():

    res = requests.get("https://focus.ua/news")

    soup = BS(res.content, "lxml")

    return soup

def parse():

    soup = getHtml()

    title = soup.find(class_="l-list__item").find(class_="c-card-list__link").text
    description = soup.find(class_="l-list__item").find(class_="c-card-list__description").text

    return {
        "title": title,
        "description": description
    }