"""Visualize the Hacker News Data"""
import json

from plotly.graph_objs import Bar
from plotly import offline

def main(input_file_path, output_file_path):
    """Visualize retrieved Hacker News data."""
    file_path = input_file_path
    submission_dicts = []
    with open(file_path) as fhand:
        submission_dicts = json.load(fhand)

    labels, comments = [], []
    for submission_dict in submission_dicts:
        # x_axis
        title = submission_dict['title']
        hn_link = submission_dict['hn_link']
        label = f"<a href='{hn_link}'>{title}</a>"
        labels.append(label)
        # y_axis
        comments.append(submission_dict['comments'])

    # Make Visualization
    data = [{
        'type': 'bar',
        'x': labels,
        'y': comments,
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
        'opacity': 0.6,
    }]

    my_layout = {
        'title': 'Most-Active Discussion on Hacker News',
        'titlefont': {'size': 28},
        'xaxis': {
            'title': 'Repository',
            'titlefont': {'size': 24},
            'tickfont': {'size': 10},
        },
        'yaxis': {
            'title': 'Stars',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },
    }

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename=output_file_path)

INPUT_FILE_PATH = 'hacker_news/data/submissions.json'
OUTPUT_FILE_PATH = 'hacker_news/hacker_news.html'
main(INPUT_FILE_PATH, OUTPUT_FILE_PATH)
