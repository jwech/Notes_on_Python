import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Grab max tempreture from file
filename_dv = 'd:/p/projects_trials/grab_data/data/death_valley_2014.csv'
filename_sitka = 'd:/p/projects_trials/grab_data/data/sitka_weather_2014.csv'
with open(filename_dv) as f:
    reader = csv.reader(f)
    header_row = next(reader) # read the 1st line
    dates_dv, highs_dv, lows_dv= [], [], []
    dates_sitka, highs_sitka, lows_sitka= [], [], []
    for row in reader: # start from the 2nd line
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, ' missing data')
        else:
            dates_dv.append(current_date)
            highs_dv.append(high)
            lows_dv.append(low)

with open(filename_sitka) as f:
    reader = csv.reader(f)
    header_row = next(reader) # read the 1st line
    dates, highs, lows= [], [], []
    for row in reader: # start from the 2nd line
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, ' missing data')
        else:
            dates_sitka.append(current_date)
            highs_sitka.append(high)
            lows_sitka.append(low)

# plot the high tempreture
fig = plt.figure(figsize=(12, 6))
plt.title("Daily high and low tempreture -2014 Death Valley and Sitka", fontsize=24)
plt.xlabel("", fontsize=14)

# Format x axis info
fig.autofmt_xdate()
plt.ylabel("Tempreture (F)", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.plot(dates_dv, highs_dv, c='red', alpha=0.5)
plt.plot(dates_dv, lows_dv, c='blue', alpha=0.5)
plt.fill_between(dates_dv, highs_dv, lows_dv, facecolor='blue', alpha=0.1)
plt.plot(dates_sitka, highs_sitka, c='red', alpha=0.5)
plt.plot(dates_sitka, lows_sitka, c='blue', alpha=0.5)
plt.fill_between(dates_sitka, highs_sitka, lows_sitka, facecolor='blue', alpha=0.1)

plt.show()