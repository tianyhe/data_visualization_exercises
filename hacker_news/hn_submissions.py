"""Hacker News API"""
from operator import itemgetter
import json

import requests

def main(url):
    """Save the most active discussion on Hacker News in json."""
    # Make an API call to store the response.
    id_url = url
    response_obj = requests.get(id_url)
    print(f"Status Code: {response_obj.status_code}")

    # Process information about each submission.
    submission_ids = response_obj.json()
    print(f"Retrieved ids: {len(submission_ids)}\n")
    submission_dicts = []

    for submission_id in submission_ids[:50]:
        # Make a seperate API call for each submission.
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        response_obj = requests.get(url)
        print(f"id: {submission_id}\tStatus Code: {response_obj.status_code}")
        response_dict = response_obj.json()

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

    submission_dicts = sorted(
        submission_dicts, key=itemgetter('comments'), reverse=True)

    for submission_dict in submission_dicts:
        print(f"\nTitle: {submission_dict['title']}")
        print(f"Discussion Links: {submission_dict['hn_link']}")
        print(f"Comments: {submission_dict['comments']}")

    # Save the retrieved data in json file.
    saved_file = 'hacker_news/data/submissions.json'
    with open(saved_file, 'w') as fhand:
        json.dump(submission_dicts, fhand)

URL = 'https://hacker-news.firebaseio.com/v0/topstories.json'
main(URL)
