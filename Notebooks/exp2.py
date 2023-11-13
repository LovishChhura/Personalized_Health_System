import requests
import json
import pprint
from datetime import date
from datetime import timedelta

# today = date.today() # or you can do today = date.today() for today's date
today = date(2014, 10, 9)
weekdate=str(today-timedelta(days=7))

response=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=health&from={weekdate}&sortBy=publishedAt&apiKey=64f00867b3db40f79eb479d459468b84')

# mydict=json.loads(response.text)
# pprint.pprint(mydict)
mydict=response.json()
pprint.pprint(mydict)