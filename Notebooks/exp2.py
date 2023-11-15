import requests
import pprint
from datetime import date
from datetime import timedelta

# today = date.today() # or you can do today = date.today() for today's date
today = date(2014, 10, 9)
weekdate=str(today-timedelta(days=7))

response=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=health&from={weekdate}&sortBy=publishedAt&apiKey=64f00867b3db40f79eb479d459468b84')


mydict=response.json()
# pprint.pprint(mydict)
article1=mydict['articles'][0]
author=article1['author']
title=article1['title']
desc=article1['description']
dateofpub=article1['publishedAt'][:10]
url=article1['url']
urlImg=article1['urlToImage']
print(author)
print(title)
print(desc)
print(dateofpub)
print(url)
print(urlImg)