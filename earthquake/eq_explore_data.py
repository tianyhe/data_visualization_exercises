"""Earthquake Explore"""
import json
import re

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

def main(input_file_path, output_file_path):
    """Visualize earthquake data with geoJson data."""
    # Explore the structure of the data
    filename = input_file_path
    with open(filename) as fhand:
        all_eq_data = json.load(fhand)

    readable_file = 'earthquake/data/readable_eq_data.json'
    with open(readable_file, 'w') as fhand:
        json.dump(all_eq_data, fhand, indent=4)

    all_eq_dicts = all_eq_data['features']
    #print(len(all_eq_dicts)) # numbers of earthquake records
    title = all_eq_data['metadata']['title']

    hover_texts = [eq_dict['properties']['title'] for eq_dict in all_eq_dicts]
    mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
    lons = [eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dicts]
    lats = [eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dicts]

    #Map the earthquake
    data = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_texts,
        'marker': {
            'size': [5*mag for mag in mags], # Set the size of marker based on mag
            'color': mags,
            'colorscale': 'Agsunset',
            'reversescale': True,
            'colorbar': {'title': 'Magnitude'},
        },
    }]
    my_layout = Layout(title=f'{title}')

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename=output_file_path)

# input_file_path = 'earthquake/data/m4.5+_eq_data_past_month.json'
# output_file_path = 'earthquake/output/global_m4.5+_earthquakes_past_month.html'
# main(input_file_path, output_file_path)
