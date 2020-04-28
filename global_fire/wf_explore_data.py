"""World Fire"""
import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

def main(input_file_path, output_file_path):
    """Visualize global fire data with csv files."""
    filename = input_file_path
    fhand = open(filename)
    reader = csv.reader(fhand)
    header_row = next(reader)

    header= {}
    for index, column_header in enumerate(header_row):
        header[column_header] = index

    lats, lons, brightnesses, hover_texts = [], [], [], []
    for row in reader:
        try:
            lat = float(row[header['latitude']])
            lon = float(row[header['longitude']])
            brightness = float(row[header['brightness']])
            hover_text = f"{row[header['acq_date']]}, {row[header['acq_time']]}, "
            hover_text += f" {row[header['daynight']]}"
        except ValueError:
            print(f"Missing data for {row[header['acq_date']]}")
        else:
            lats.append(lat)
            lons.append(lon)
            brightnesses.append(brightness)
            hover_texts.append(hover_text)

    #Map the earthquake
    data = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_texts,
        'marker': {
            #'size': [0.1*brightness for brightness in brightnesses],
            'color': brightnesses,
            'colorscale': 'Agsunset',
            'reversescale': True,
            'colorbar': {'title': 'Brightness'},
        },
    }]
    my_layout = Layout(title='Global Active Fire Past Day')

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename=output_file_path)
    fhand.close()

# input_file_path = 'global_fire/data/MODIS_C6_Global_24h.csv'
# output_file_path = 'global_fire/output/global_fire_past_day.html'
# main(input_file_path, output_file_path)
