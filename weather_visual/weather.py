"""Weather"""
import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'weather_visual/data/death_valley_2018_simple.csv'
fhand = open(filename)
reader = csv.reader(fhand)
header_row = next(reader)

header= {}
for index, column_header in enumerate(header_row):
    header[column_header] = index

dates, lows, highs = [], [], []
for row in reader:
    current_date = datetime.strptime(row[header['DATE']], '%Y-%m-%d')
    name = row[header['NAME']]
    try:
        high = int(row[header['TMAX']])
        low = int(row[header['TMIN']])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
title = f"Daily high and low temperatures - 2018\n{name}"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

#plt.show()
plt.savefig('death_valley_high_low_temp.png', bbox_inches='tight')
fhand.close()
