"""Hacker News API"""
from operator import itemgetter

import requests
import json
import sqlite3

conn = sqlite3.connect('hacker_news/data/submissions.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Submissions;

CREATE TABLE Submissions (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    submission_id  TEXT UNIQUE,
    title TEXT  UNIQUE,
    discussion_link TEXT UNIQUE,
    comments INTEGER
);
''')

# Make an API call to store the response.
id_url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(id_url)
print(f"Status Code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
print(f"Retrieved ids: {len(submission_ids)}\n")
submission_dicts = []
count = 1

for submission_id in submission_ids[:50]:
    # Make a seperate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"{count} - id: {submission_id}\tStatus Code: {r.status_code}")
    response_dict = r.json()

    try:
        # Build a dictionary for each article.
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
        submission_dicts.append(submission_dict)
    except KeyError:
        print(f"Failure to Find the corresponding key: {submission_id}")
        continue
    else:
        cur.execute(
            '''INSERT OR REPLACE INTO Submissions
            (submission_id, title, discussion_link, comments)
            VALUES ( ?, ?, ?, ? )''',
            (submission_id, submission_dict['title'], submission_dict['hn_link'], submission_dict['comments']))

    count += 1
    if count % 5 == 0:
        conn.commit()
