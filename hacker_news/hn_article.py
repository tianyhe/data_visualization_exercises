"""Hacker News API"""
import requests
import json

url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status Code: {r.status_code}")

# Explore the structure of the data.
response_dict = r.json()
readable_file = 'hacker_news_visual/data/readable_hn_data.json'
with open(readable_file, 'w') as fhand:
    json.dump(response_dict, fhand, indent=4)
