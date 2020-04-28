"""Github Python Project Visualization"""
import requests

from plotly.graph_objs import Bar
from plotly import offline

import hidden # import personal access token

def main(search_url, headers):
    """Visualize the Most-Starred Python Projects on Github."""
    # Make an API call to store the response.
    r = requests.get(search_url, headers=headers)
    print(f"Status code: {r.status_code}")

    # Store API response in a variable
    response_dict = r.json()

    # # Process results.
    # print(response_dict.keys())

    # Explore information about the repositories.
    repo_dicts = response_dict['items']
    print(f"Repositories returned: {len(repo_dicts)}")

    # Summary for the repositories.
    # print("\nSelected information about each repository:")
    # for repo_dict in repo_dicts:
    #     print(f"Name: {repo_dict['name']}")
    #     print(f"Owner: {repo_dict['owner']['login']}")
    #     print(f"Stars: {repo_dict['stargazers_count']}")
    #     print(f"Repository: {repo_dict['html_url']}")
    #     print(f"Created: {repo_dict['created_at']}")
    #     print(f"Updated: {repo_dict['updated_at']}")
    #     print(f"Description: {repo_dict['description']}\n")

    repo_links, stars, labels = [], [], []
    for repo_dict in repo_dicts:
        # x_axis
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)
        # y_axis
        stars.append(repo_dict['stargazers_count'])
        # hover_text
        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        label = f"{owner}<br />{description}"
        labels.append(label)

    # Make Visualization
    data = [{
        'type': 'bar',
        'x': repo_links,
        'y': stars,
        'hovertext': labels,
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
        'opacity': 0.6,
    }]

    my_layout = {
        'title': 'Most-Starred Python Projects on Github',
        'titlefont': {'size': 28},
        'xaxis': {
            'title': 'Repository',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },
        'yaxis': {
            'title': 'Stars',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },
    }

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='github_visual/python_repos.html')

def rate_limit(rate_url, headers):
    """Check the remaining rate limit for search."""
    r_rate = requests.get(rate_url, headers=headers)
    rate_dict = r_rate.json()
    rate_remaining = rate_dict['resources']['search']['remaining']
    print(f"Remaining Rate: {rate_remaining}")

search_url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
rate_url = 'https://api.github.com/rate_limit'
headers = {
    'Accept': 'application/vnd.github.vs+json',
    'Authorization': 'token ' + f'{hidden.token_secret()}'
    }

main(search_url, headers)
rate_limit(rate_url, headers)
